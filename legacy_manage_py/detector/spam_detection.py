from django.shortcuts import render


def home(request):
    prediction = None
    email_text = ""

    if request.method == "POST":

        email_text = request.POST.get("email_text", "").strip()

        if email_text:

            # Temporary prediction
            # We will connect your trained ML model here next.
            prediction = "Spam"

    context = {
        "prediction": prediction,
        "email_text": email_text,
    }

    return render(request, "detector/index.html", context)