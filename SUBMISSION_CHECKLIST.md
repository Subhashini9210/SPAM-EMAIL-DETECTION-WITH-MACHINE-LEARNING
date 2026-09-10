Submission checklist — finalize before submitting to university

## Core Requirements

- [x] AUTHORS.md filled with full name, roll number, supervisor, institution
- [ ] report.pdf (generated from report.md or replaced by final report) included
- [ ] slides.pdf included
- [x] README.md updated (describes how to run and reproduce results)
- [x] SETUP_INSTRUCTIONS.md verified and accurate
- [x] LICENSE present (MIT added)
- [x] Unit tests pass (`python -m pytest -q`)
- [x] CI workflow present and passing on GitHub Actions
- [ ] Optional: outputs/models/spam_classifier.joblib included (if required by assessor)

## How to Convert Markdown to PDF

### Report
```bash
# Using pandoc (recommended)
pandoc report.md -o report.pdf

# Or use VS Code: "Markdown Preview Enhanced" extension → Export to PDF
# Or use online tools like Markdown to PDF converter
```

### Slides
```bash
# Option 1: Using Marp CLI
marp slides.md --pdf -o slides.pdf

# Option 2: Export from presentation software
# - Copy slides.md content into Google Slides, PowerPoint, or Keynote
# - Export to PDF

# Option 3: Using reveal.js or similar
npx reveal.md slides.md --to pdf
```

## Final Submission Checklist

Before submitting to your university:

1. **Update AUTHORS.md:**
   - [ ] Full name entered
   - [ ] Student/Roll number entered
   - [ ] Supervisor name entered
   - [ ] Institution/Department entered
   - [ ] Contact email entered

2. **Generate PDF files:**
   - [ ] report.pdf created from report.md
   - [ ] slides.pdf created from slides.md
   - [ ] Both PDFs committed to repository

3. **Run experiments:**
   - [ ] Download dataset: `cd spam-detection && python src/spam_detection/download_data.py`
   - [ ] Train model: `python src/spam_detection/train.py`
   - [ ] Note down accuracy, F1, and cross-validation scores
   - [ ] Update report.md with actual results (replace placeholders)

4. **Verify all tests pass:**
   - [ ] `python -m pytest -q` from repository root
   - [ ] All 7+ tests pass (spam-detection/tests/test_train.py)

5. **Check CI/CD:**
   - [ ] All GitHub Actions workflows passing
   - [ ] View at: https://github.com/Subhashini9210/SPAM-EMAIL-DETECTION-WITH-MACHINE-LEARNING/actions

6. **Final review:**
   - [ ] README.md is complete and clear
   - [ ] All code is commented and professional
   - [ ] No debug files or temporary code left
   - [ ] No secrets or credentials in repository
   - [ ] .gitignore excludes data/ and outputs/ correctly

## Submission Package

If your university requires a ZIP file, prepare:
```
submission.zip
├── AUTHORS.md
├── LICENSE
├── README.md
├── report.pdf
├── slides.pdf
├── spam-detection/
│   ├── src/
│   ├── tests/
│   └── requirements.txt
└── SUBMISSION_CHECKLIST.md
```

Create with:
```bash
zip -r submission.zip AUTHORS.md LICENSE README.md report.pdf slides.pdf spam-detection/ SUBMISSION_CHECKLIST.md
```

## Common Issues & Solutions

**Issue:** Tests fail when running locally
- **Solution:** Ensure all dependencies installed: `pip install -r spam-detection/requirements.txt`

**Issue:** Can't download UCI dataset
- **Solution:** Check internet connection; UCI servers may be temporarily down. Try downloading manually from: https://archive.ics.uci.edu/dataset/228/sms+spam+collection

**Issue:** Model training is slow
- **Solution:** This is normal for the first run (5,574 messages). Subsequent runs are cached.

**Issue:** Can't convert markdown to PDF
- **Solution:** 
  - Install pandoc: `pip install pypandoc` or use online converter
  - Or manually copy content into Word/Google Docs and export as PDF

## Questions or Issues?

Refer to:
- `spam-detection/README.md` — ML project specifics
- `report.md` — Full technical report template
- `slides.md` — Presentation structure
- GitHub Actions logs — CI/CD troubleshooting
