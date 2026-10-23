import pandas as pd


def find_issues(df):
    """Run rule-based data checks (normal code, no AI) and return a list of issues."""
    issues = []

    # Missing values
    for col, count in df.isnull().sum().items():
        if count > 0:
            issues.append(f"Column '{col}' has {count} missing value(s)")

    # Duplicate IDs
    dups = df[df["order_id"].duplicated(keep=False)]
    if not dups.empty:
        issues.append(f"Duplicate order_id values: {dups['order_id'].unique().tolist()}")

    # Negative amounts
    neg = df[df["amount"] < 0]
    if not neg.empty:
        issues.append(f"{len(neg)} row(s) have a negative amount")

    # Outliers (far above the typical value)
    median = df["amount"].median()
    big = df[df["amount"] > median * 10]
    if not big.empty:
        issues.append(f"{len(big)} row(s) have a suspiciously large amount")

    # Date format
    parsed = pd.to_datetime(df["date"], format="%Y-%m-%d", errors="coerce")
    bad_dates = parsed.isnull().sum()
    if bad_dates > 0:
        issues.append(f"{bad_dates} date(s) are not in YYYY-MM-DD format")

    return issues


if __name__ == "__main__":
    df = pd.read_csv("sales.csv")
    for issue in find_issues(df):
        print("-", issue)
