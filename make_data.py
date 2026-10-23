import pandas as pd

# Small sales dataset with deliberate errors for the checks to find
data = {
    "order_id": [1, 2, 3, 3, 5, 6, 7, 8],
    "customer": ["Ravi", "Anita", None, "Kiran", "Kiran", "Sita", "Mohan", "Priya"],
    "amount": [250, 400, 300, 300, -50, 99999, 450, None],
    "date": ["2026-01-05", "2026-01-06", "2026-01-07", "2026-01-07",
             "05/01/2026", "2026-01-09", "2026-01-10", "2026-01-11"],
}

pd.DataFrame(data).to_csv("sales.csv", index=False)
print("sales.csv created")
