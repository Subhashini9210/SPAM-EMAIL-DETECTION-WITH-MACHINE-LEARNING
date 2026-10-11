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

For a CSV with different column names, pass `--label-column` and `--text-column`. The script holds out 20% of the data for evaluation and prints accuracy, a confusion matrix, and precision/recall/F1 scores. Labels are normalized to `ham` and `spam`; `no`/`yes` and `0`/`1` are also supported, and unknown labels are rejected. Training saves a complete vectorizer/classifier pipeline to `artifacts/spam_classifier.joblib`, which the web app loads automatically.

## Current evaluation

The included model was trained using the SpamAssassin `easy_ham_2` and `spam_2` folders (2,796 parsed emails), with a stratified 80/20 train/test split and random seed 42. It scored **97.86% accuracy** on the 560-message held-out test set. Its confusion matrix (true rows, predicted columns; ham then spam) was `[[276, 4], [8, 272]]`. The web app labels predictions with a decision margin below 1.25 as uncertain and asks users to review them manually. On this same test split, that threshold yielded 75.7% coverage and 100% accuracy among messages it classified; the threshold was selected after observing held-out results, so these figures are exploratory, not an independent validation. This is an older public corpus and does not guarantee accuracy on current email; evaluate on representative, separately labeled email before relying on it.

Dataset reference: Apache SpamAssassin [public mail corpus](https://spamassassin.apache.org/old/publiccorpus/readme.html). The corpus contains labeled email messages; message text remains copyrighted by its original senders. The corpus maintainers warn against sending these samples to live mail systems.

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
