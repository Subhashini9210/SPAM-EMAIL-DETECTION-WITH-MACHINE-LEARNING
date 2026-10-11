def normalize_label(label):
    """Convert supported dataset labels to the app's canonical classes."""
    normalized = str(label).strip().casefold()
    if normalized in {"ham", "legitimate", "no", "0", "0.0"}:
        return "ham"
    if normalized in {"spam", "junk", "yes", "1", "1.0"}:
        return "spam"
    raise ValueError(
        f"Unsupported label {label!r}; use ham/spam, no/yes, or 0/1."
    )
