"""Download and prepare the UCI SMS Spam Collection as a project CSV."""

from argparse import ArgumentParser
from io import BytesIO
from pathlib import Path
from urllib.request import urlopen
from zipfile import ZipFile

import pandas as pd

UCI_SMS_SPAM_URL = "https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip"
DEFAULT_OUTPUT_PATH = Path("data/raw/train.csv")


def parse_sms_collection(content: str) -> pd.DataFrame:
    """Parse UCI's tab-delimited label/message format into the project schema."""
    rows = []
    for line in content.splitlines():
        label, separator, text = line.partition("\t")
        if not separator or label not in {"ham", "spam"}:
            continue
        rows.append({"text": text, "label": label})
    if not rows:
        raise ValueError("The downloaded dataset contains no valid SMS records.")
    return pd.DataFrame(rows, columns=["text", "label"])


def download_dataset(output_path: Path = DEFAULT_OUTPUT_PATH) -> pd.DataFrame:
    """Download the UCI collection, save it locally, and return the data frame."""
    with urlopen(UCI_SMS_SPAM_URL, timeout=30) as response:
        archive = BytesIO(response.read())
    with ZipFile(archive) as zip_file:
        content = zip_file.read("SMSSpamCollection").decode("utf-8", errors="replace")

    dataset = parse_sms_collection(content)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    dataset.to_csv(output_path, index=False)
    return dataset


def main() -> None:
    """Download the dataset from the command line."""
    parser = ArgumentParser(description="Download the UCI SMS Spam Collection.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT_PATH)
    args = parser.parse_args()
    dataset = download_dataset(args.output)
    print(f"Saved {len(dataset):,} labelled messages to {args.output}")


if __name__ == "__main__":
    main()
