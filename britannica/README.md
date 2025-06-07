# Britannica Scraper

This project contains scraper files for extracting data from https://britannica.com/search?query=Technology.

## Files

- `create_scraper_list.py` - Creates a scraper for the website
- `extract_data.py` - Extracts data using the created scraper
- `requirements.txt` - Python dependencies
- `README.md` - This file

## Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Get your Minexa API key from [Minexa.ai](https://minexa.ai)

3. Replace `YOUR_API_KEY` in both Python files with your actual API key

## Usage

### Step 1: Create the scraper
```bash
python create_scraper_list.py
```

This will create a scraper and return a scraper ID. Note this ID for the next step.

### Step 2: Extract data
1. Replace the `scraper_id` value in `extract_data.py` with your actual scraper ID
2. Run the extraction:
```bash
python extract_data.py
```

## Target URLs

The scraper is configured to work with these URLs:
- https://www.britannica.com/search?query=Electric
- https://www.britannica.com/search?query=Water

## Output

The data extraction script will generate:
- `extraction_YYYY_MM_DD_HH_MM.json` - Raw JSON data
- `extraction_YYYY_MM_DD_HH_MM.csv` - CSV format
- `extraction_YYYY_MM_DD_HH_MM.xlsx` - Excel format

## Sample Data

The scraper was trained on this sample data:

```
technology
technology, the application of scientific knowledge to the practical aims of human life—or, as it is sometimes phrased, to the change and manipulation of the human environment. The word technology is a combination of the Greek technē, which means “art, craft,” and logos, which means “word, speech.” ...

History of technology
History of technology, the development over time of systematic techniques for making and doing things. ...

Automation
Automation, application of machines to task...
```

Generated on 2025-06-07 21:16:00
