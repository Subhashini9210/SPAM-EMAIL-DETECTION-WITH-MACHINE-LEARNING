# Spam Email Detector

A Django web app that classifies submitted email text with a scikit-learn model. The repository also has a separate SMS classification exercise under `spam-detection/`.

## Web application setup

Create and activate a Python virtual environment, then install the root dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Train the email classifier

Provide a CSV with `label` and `message` columns, or an extracted Apache SpamAssassin corpus directory containing ham and spam folders:

```powershell
python train_model.py path\to\spam_messages.csv
python train_model.py path\to\spamassassin-corpus
```

For different CSV column names, pass `--label-column` and `--text-column`. Training evaluates a stratified 80/20 split, prints accuracy, a confusion matrix, precision, recall, and F1 scores, then saves the pipeline to `spam-detection/outputs/models/spam_classifier.joblib`. It also writes a compatibility copy to `artifacts/spam_classifier.joblib`; the Django app checks both locations. Labels are normalized to `ham` and `spam`; `no`/`yes` and `0`/`1` are accepted, while unknown labels are rejected.

## Run the web app

```powershell
python manage.py migrate
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/). The app reports when no classifier is available. The bundled model can be used for a local demo; retrain it on data appropriate for your evaluation.

## Evaluation reference

The bundled model was trained on 2,796 messages from the SpamAssassin `easy_ham_2` and `spam_2` folders with a stratified 80/20 split and random seed 42. The held-out set scored 97.86% accuracy, with confusion matrix `[[276, 4], [8, 272]]` (true rows, predicted columns; ham then spam). These results come from an older public corpus and do not guarantee performance on current email. The app can return an uncertain result for low-margin predictions. The reported confidence threshold was selected after observing held-out results, so its coverage and accuracy are exploratory rather than an independent validation.

Dataset reference: Apache SpamAssassin [public mail corpus](https://spamassassin.apache.org/old/publiccorpus/readme.html). Do not send corpus samples to live mail systems.

## Standalone SMS classifier

From the `spam-detection/` directory, download the UCI SMS Spam Collection, train, and make a sample prediction:

```powershell
python -m pip install -r requirements.txt
python src\spam_detection\download_data.py
python src\spam_detection\train.py
python src\spam_detection\train.py --predict "Congratulations! You won a free prize."
```

The SMS project uses `data/raw/train.csv` with `text` and `label` columns. It saves a model under `outputs/models/` and a confusion matrix under `outputs/figures/`. Run its tests from the same directory with `python -m pytest -q`.

## Deployment

`render.yaml` configures a Render web service. Set `DJANGO_DEBUG=false`, provide a unique non-empty `DJANGO_SECRET_KEY`, and set `DJANGO_ALLOWED_HOSTS` to the hostnames that should serve the app. In production the app enables HTTPS redirects, secure cookies, and HSTS. Render supplies HTTPS and the proxy header is configured for it. The free service may sleep when idle, and its local SQLite database is ephemeral.
