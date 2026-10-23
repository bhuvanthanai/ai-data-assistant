# AI Data Validation and Report Assistant

A small AI workflow that checks a messy CSV file for problems and uses an
LLM to explain them in plain English and write a summary report.

## How it works
1. Python (pandas) checks the data: missing values, duplicates, outliers, bad dates
2. An LLM explains each issue and suggests a fix
3. An LLM writes a short summary report
4. A human reviews the final output

## Why the checks are normal code
Validation needs to be accurate and repeatable, so it uses plain Python.
The AI is used only for explanation and writing.

## Run it
```bash
pip install -r requirements.txt
python make_data.py
python checks.py
```

## Tech
Python, pandas, Anthropic API

## Status
- [x] Data checks
- [ ] AI explanation step
- [ ] Report generation
- [ ] Streamlit upload page
