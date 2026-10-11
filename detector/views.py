from functools import lru_cache

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from joblib import load


@lru_cache(maxsize=1)
def get_model():
    """Load the trained text classifier once per server process."""
    model_path = settings.BASE_DIR / "artifacts" / "spam_classifier.joblib"
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
        else:
            model = get_model()
            if model is None:
                error = "The classifier has not been trained yet. Follow the training instructions in README.md."
            else:
                label = str(model.predict([email_text])[0]).strip().lower()
                prediction = "Spam" if label in {"spam", "1", "junk"} else "Ham"

    return render(request, "detector/index.html", {
        "prediction": prediction,
        "email_text": email_text,
        "error": error,
    })


def service_worker(request):
    worker_path = settings.BASE_DIR / "templates" / "static" / "detector" / "service-worker.js"
    response = HttpResponse(worker_path.read_text(encoding="utf-8"), content_type="application/javascript")
    response["Service-Worker-Allowed"] = "/"
    response["Cache-Control"] = "no-cache"
    return response
