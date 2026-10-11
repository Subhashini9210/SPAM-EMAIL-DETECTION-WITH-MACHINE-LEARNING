# Spam Email Detector

A Django web app that classifies submitted email text with a scikit-learn model. The repository also contains a standalone SMS classification exercise under `spam-detection/`; the web application and standalone exercise have separate training commands and artifacts.

## Web application setup

Create and activate a virtual environment, then install the root requirements:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Train the web app classifier

Provide either a CSV with `label` and `message` columns, or an extracted Apache SpamAssassin corpus directory containing ham and spam folders:

```powershell
python train_model.py path\to\spam_messages.csv
python train_model.py path\to\spamassassin-corpus
```

For a CSV with different column names, pass `--label-column` and `--text-column`. Training evaluates a stratified holdout split and saves a complete vectorizer/classifier pipeline to `artifacts/spam_classifier.joblib`.

## Run the web app

```powershell
python manage.py migrate
python manage.py runserver
```

Open <http://127.0.0.1:8000/>. The app reports when the classifier has not been trained yet. The bundled artifact can be used for a quick local demo, but retrain it on the dataset you intend to evaluate. The development settings are for local use. For deployment, set `DJANGO_DEBUG=false`, provide a unique non-empty `DJANGO_SECRET_KEY`, and configure `DJANGO_ALLOWED_HOSTS` with the hostnames that should serve the app.

## Standalone SMS classifier

The separate `spam-detection/` project downloads the UCI SMS Spam Collection and writes `data/raw/train.csv` with `text` and `label` columns. From that project directory:

```powershell
python -m pip install -r requirements.txt
python src\spam_detection\download_data.py
python src\spam_detection\train.py
python src\spam_detection\train.py --predict "Congratulations! You won a free prize."
```

It saves a pipeline under `outputs/models/` and a confusion matrix under `outputs/figures/`. The test suite for this standalone project is run from its directory with `python -m pytest -q`.

## Deployment

The included `render.yaml` configures a free Render web service. Push the project to a GitHub repository, connect that repository in Render using **New > Blueprint**, and apply the blueprint. Render generates `DJANGO_SECRET_KEY`, collects static files, runs migrations, and starts Gunicorn. With `DJANGO_DEBUG=false`, the app rejects an empty or development-only secret key and enables HTTPS redirects, secure cookies, and one-year HSTS with subdomains and the preload directive; the HTTPS proxy header is configured for Render. The preload directive advertises preload eligibility but does not automatically submit the hostname to browser preload lists. Use a custom domain and verify preload requirements before submitting it. The Render URL uses HTTPS, which is required for installing the PWA. The free service may sleep when idle, and its local SQLite database is ephemeral; the classifier itself is included in `artifacts/`.
