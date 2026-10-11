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

Open <http://127.0.0.1:8000/>. The app reports when the classifier has not been trained yet. The bundled artifact can be used for a quick local demo, but retrain it on the dataset you intend to evaluate.

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

`render.yaml` configures a Render web service. Set a secret `DJANGO_SECRET_KEY` and `DJANGO_DEBUG=false` for deployment. The included SQLite database is local and ephemeral on hosts that do not provide persistent disks.
