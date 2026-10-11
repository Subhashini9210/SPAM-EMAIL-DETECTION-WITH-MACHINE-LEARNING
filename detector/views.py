from functools import lru_cache
from math import isfinite

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from joblib import load

from .classification import normalize_label

MAX_EMAIL_LENGTH = 20000
MINIMUM_CONFIDENCE_MARGIN = 1.25


def get_model_path():
    """Return the current model location, with a compatibility fallback for older project layouts."""
    candidates = [
        settings.BASE_DIR / "spam-detection" / "outputs" / "models" / "spam_classifier.joblib",
        settings.BASE_DIR / "artifacts" / "spam_classifier.joblib",
    ]
    for model_path in candidates:
        if model_path.exists():
            return model_path
    return candidates[0]


@lru_cache(maxsize=1)
def get_model():
    """Load the trained text classifier once per server process."""
    model_path = get_model_path()
    if not model_path.exists():
        return None
    return load(model_path)


def home(request):
    prediction = None
    error = None
    email_text = ""

    if request.method == "POST":
        email_text = request.POST.get("email_text", "").strip()
        if not email_text:
            error = "Enter an email message to check."
        elif len(email_text) > MAX_EMAIL_LENGTH:
            error = f"Email messages must be {MAX_EMAIL_LENGTH} characters or fewer."
        else:
            model = get_model()
            if model is None:
                error = "The classifier has not been trained yet. Follow the training instructions in README.md."
            else:
                try:
                    label = normalize_label(model.predict([email_text])[0])
                    margin = float(model.decision_function([email_text])[0])
                except (AttributeError, IndexError, TypeError, ValueError):
                    error = "The classifier returned an invalid result. Please try again later."
                else:
                    if not isfinite(margin):
                        error = "The classifier returned an invalid result. Please try again later."
                    elif abs(margin) < MINIMUM_CONFIDENCE_MARGIN:
                        prediction = "Uncertain"
                    else:
                        prediction = label.title()

    return render(request, "detector/index.html", {
        "prediction": prediction,
        "email_text": email_text,
        "error": error,
    })


def service_worker(_request):
    worker_path = settings.BASE_DIR / "templates" / "static" / "detector" / "service-worker.js"
    response = HttpResponse(worker_path.read_text(encoding="utf-8"), content_type="application/javascript")
    response["Service-Worker-Allowed"] = "/"
    response["Cache-Control"] = "no-cache"
    return response
