document.addEventListener("DOMContentLoaded", function () {

    const textarea = document.getElementById("email_text");
    const form = document.querySelector("form");

    if (form) {

        form.addEventListener("submit", function (event) {

            const text = textarea.value.trim();

            if (text.length === 0) {

                alert("Please enter an email or message.");

                event.preventDefault();

            }

        });

    }

    const installButton = document.getElementById("install-app");
    const installHint = document.getElementById("install-hint");
    const isStandalone = window.matchMedia("(display-mode: standalone)").matches
        || window.navigator.standalone === true;
    const isIOS = /iphone|ipad|ipod/i.test(window.navigator.userAgent);
    let installPrompt;

    if (isIOS && !isStandalone && installHint) {
        installHint.hidden = false;
    }

    window.addEventListener("beforeinstallprompt", function (event) {
        event.preventDefault();
        installPrompt = event;
        if (installButton) installButton.hidden = false;
    });

    if (installButton) {
        installButton.addEventListener("click", async function () {
            if (!installPrompt) return;
            installPrompt.prompt();
            await installPrompt.userChoice;
            installPrompt = null;
            installButton.hidden = true;
        });
    }

    window.addEventListener("appinstalled", function () {
        if (installButton) installButton.hidden = true;
        if (installHint) installHint.hidden = true;
    });

});