# Spam classifier evaluation

- Dataset: Apache SpamAssassin public email corpus, `easy_ham_2` and `spam_2`
- Parsed messages: 2,796 (1,400 ham; 1,396 spam)
- Evaluation: stratified 80/20 hold-out, random seed 42
- Test messages: 560
- Accuracy: **97.86%**
- Confusion matrix (true rows, predicted columns; ham then spam): `[[276, 4], [8, 272]]`
- Spam precision: 0.99
- Spam recall: 0.97
- Spam F1: 0.98
- With the app's minimum absolute decision margin of 1.25, coverage was 75.7% and accuracy among classified test messages was 100%. This threshold was selected after observing the hold-out results, so these are exploratory figures, not independent validation.

The app reports predictions below the 1.25 margin as uncertain rather than presenting a low-confidence ham/spam result. Recreate the base metrics by extracting the same two corpus archives into one folder, then running `python train_model.py path/to/corpus-folder`. The threshold figures are not guaranteed to reproduce as an unbiased estimate because the threshold was selected after observing this hold-out set.

This score measures performance on a held-out portion of this historical corpus. It is not a guarantee for modern email.
