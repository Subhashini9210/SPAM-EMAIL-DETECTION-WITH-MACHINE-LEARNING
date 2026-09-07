Submission checklist — finalize before submitting to university

- [ ] AUTHORS.md filled with full name, roll number, supervisor, institution
- [ ] report.pdf (generated from report.md or replaced by final report) included
- [ ] slides.pdf included
- [ ] README updated (root) describing how to run and reproducing results
- [ ] SETUP_INSTRUCTIONS.md verified and accurate
- [ ] LICENSE present (MIT added)
- [ ] Unit tests pass (`python -m pytest -q`)
- [ ] CI workflow present and passing (after merging PR)
- [ ] Optional: outputs/models/spam_classifier.joblib included (if required by assessor)

Notes:
- To generate PDF from markdown: `pandoc report.md -o report.pdf` or export from your editor.
- If your university requires a separate code zip, prepare a zip that includes `spam-detection/` and report.pdf
