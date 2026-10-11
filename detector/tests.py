import os
import subprocess
import sys
from pathlib import Path
from unittest.mock import Mock, patch

from django.test import TestCase, override_settings

from .classification import normalize_label
from .views import MAX_EMAIL_LENGTH

@override_settings(STORAGES={
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {"BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"},
})
class HomeViewTests(TestCase):
    def test_production_rejects_empty_secret_key(self):
        environment = os.environ.copy()
        environment["DJANGO_DEBUG"] = "false"
        environment["DJANGO_SECRET_KEY"] = ""
        project_root = Path(__file__).resolve().parent.parent

        result = subprocess.run(
            [sys.executable, "-c", "import spam_email_project.settings"],
            cwd=project_root,
            env=environment,
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Set DJANGO_SECRET_KEY", result.stderr)

    def test_homepage_loads(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Spam Email Detector")

    def test_empty_message_shows_validation_error(self):
        response = self.client.post("/", {"email_text": "   "})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Enter an email message to check.")

    @patch("detector.views.get_model")
    def test_oversized_message_is_rejected_before_model_load(self, get_model):
        response = self.client.post("/", {"email_text": "x" * (MAX_EMAIL_LENGTH + 1)})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f"Email messages must be {MAX_EMAIL_LENGTH} characters or fewer.")
        get_model.assert_not_called()

    @patch("detector.views.get_model", return_value=None)
    def test_missing_classifier_shows_training_message(self, get_model):
        response = self.client.post("/", {"email_text": "Some email content"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The classifier has not been trained yet.")
        get_model.assert_called_once_with()

    def test_spam_prediction_is_rendered(self):
        model = Mock()
        model.predict.return_value = ["spam"]
        model.decision_function.return_value = [2.0]

        with patch("detector.views.get_model", return_value=model):
            response = self.client.post("/", {"email_text": "Claim your prize"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Spam")
        model.predict.assert_called_once_with(["Claim your prize"])

    def test_ham_prediction_is_rendered(self):
        model = Mock()
        model.predict.return_value = ["ham"]
        model.decision_function.return_value = [-2.0]

        with patch("detector.views.get_model", return_value=model):
            response = self.client.post("/", {"email_text": "Team meeting at 3 PM"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ham")

    def test_low_confidence_prediction_is_marked_uncertain(self):
        model = Mock()
        model.predict.return_value = ["spam"]
        model.decision_function.return_value = [1.0]

        with patch("detector.views.get_model", return_value=model):
            response = self.client.post("/", {"email_text": "An ordinary message"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Uncertain")
        self.assertContains(response, "Review it manually.")

    def test_non_finite_confidence_is_rejected(self):
        model = Mock()
        model.predict.return_value = ["spam"]
        model.decision_function.return_value = [float("nan")]

        with patch("detector.views.get_model", return_value=model):
            response = self.client.post("/", {"email_text": "An ordinary message"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The classifier returned an invalid result.")

    def test_yes_no_prediction_labels_are_normalized(self):
        model = Mock()
        model.predict.return_value = ["no"]
        model.decision_function.return_value = [-2.0]

        with patch("detector.views.get_model", return_value=model):
            response = self.client.post("/", {"email_text": "An ordinary message"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ham")

    def test_service_worker_is_available_at_site_root(self):
        response = self.client.get("/service-worker.js")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/javascript")
        self.assertEqual(response["Service-Worker-Allowed"], "/")
        self.assertEqual(response["Cache-Control"], "no-cache")


class ClassificationLabelTests(TestCase):
    def test_supported_labels_are_normalized(self):
        labels = {
            " HAM ": "ham",
            "no": "ham",
            "0": "ham",
            "YES": "spam",
            "junk": "spam",
            "1": "spam",
        }

        for label, expected in labels.items():
            with self.subTest(label=label):
                self.assertEqual(normalize_label(label), expected)

    def test_unknown_label_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Unsupported label"):
            normalize_label("maybe")
