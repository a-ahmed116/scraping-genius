# Rightmove Scraper

This project contains scraper files for extracting data from https://www.rightmove.co.uk/property-for-sale/find.html?searchLocation=London&useLocationIdentifier=true&locationIdentifier=REGION%5E87490&radius=0.0&_includeSSTC=on.

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
- https://www.rightmove.co.uk/property-for-sale/find.html?useLocationIdentifier=true&locationIdentifier=REGION%5E74254&radius=0.0&_includeSSTC=on&index=0&sortType=2&channel=BUY&transactionType=BUY&displayLocationIdentifier=Raleigh.html
- https://www.rightmove.co.uk/property-for-sale/find.html?useLocationIdentifier=true&locationIdentifier=REGION%5E1405&radius=0.0&_includeSSTC=on&index=0&sortType=2&channel=BUY&transactionType=BUY&displayLocationIdentifier=Washington.html

## Output

The data extraction script will generate:
- `extraction_YYYY_MM_DD_HH_MM.json` - Raw JSON data
- `extraction_YYYY_MM_DD_HH_MM.csv` - CSV format
- `extraction_YYYY_MM_DD_HH_MM.xlsx` - Excel format

## Sample Data

The scraper was trained on this sample data:

```
|
1/8
FEATURED PROPERTY
£260,000
Guide Price
Streatham High Road, London
Apartment
1
1
Reduced on 03/06/2025
Call
Contact
Save

|
1/15
£80,000,000
Guide Price
The Knightsbridge Apartments, 199 Knightsbridge, London, SW7
Penthouse
5
5
Added on 02/09/2024
Call
Contact
Save

1/6
£60,000,000
One Hyde Park, Knightsbridge
Apartment
5
5
Added on 05/07/2024
Call
Contact
Save

1/24
£59,950,000
PREMIUM LISTING
Avenue Road, St John's Wood, London, NW8, United Kingdom
House
10
8
Added on 25/11/2024
Call
Con...
```

Generated on 2025-06-07 23:36:07
