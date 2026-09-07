SPAM EMAIL DETECTION WITH MACHINE LEARNING

Overview

This repository contains a spam email / SMS detection project. The production-ready spam detection code and tests are under the `spam-detection/` subdirectory. The root contains helper scripts and exploratory files.

Quick status

- spam-detection/ is runnable and contains:
  - src/spam_detection/download_data.py — downloader for the UCI SMS Spam Collection
  - src/spam_detection/train.py — train / predict CLI, saves model to outputs/models/
  - tests in spam-detection/tests/ and a focused test_train.py
- CI workflow added to run tests on pushes and pull requests.

How to reproduce (recommended)

1. Clone the repository
   git clone https://github.com/Subhashini9210/SPAM-EMAIL-DETECTION-WITH-MACHINE-LEARNING.git
   cd SPAM-EMAIL-DETECTION-WITH-MACHINE-LEARNING

2. (Optional but recommended) Create and activate a virtual environment
   python3 -m venv .venv
   source .venv/bin/activate

3. Install dependencies (root and subproject):
   pip install -r requirements.txt
   pip install -r spam-detection/requirements.txt

4. Download dataset and train the spam model
   cd spam-detection
   python src/spam_detection/download_data.py
   python src/spam_detection/train.py

5. Run tests
   # From repository root
   python -m pytest -q

Files added in this branch (prepare/submission)
- LICENSE (MIT)
- AUTHORS.md (placeholder)
- report.md (project report template)
- slides.md (presentation outline)
- SUBMISSION_CHECKLIST.md (final submission checklist)
- .github/workflows/python-tests.yml (CI to run pytest)
- Updated README.md (this file)

Notes

- Please add your student metadata to AUTHORS.md and generate a PDF report from report.md (or replace it with your final report.pdf). Also add slides.pdf if you produce slides.
- If you want the trained model artifact committed, respond and I will add the joblib file (note it will increase repo size).
