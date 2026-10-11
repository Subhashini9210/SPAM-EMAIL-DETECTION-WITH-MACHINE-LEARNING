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

Recreate these metrics by extracting the same two corpus archives into one folder, then running `python train_model.py path/to/corpus-folder`.

This score measures performance on a held-out portion of this historical corpus. It is not a guarantee for modern email.
