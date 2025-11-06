# Data Directory

This directory contains sample data files for testing and demonstration of the Statistical Analysis Tool.

## Files

### Sample Manufacturing Data
- **`sample_manufacturing_data.csv`** - Multi-variable manufacturing dataset with Temperature, Pressure, Flow Rate, and Diameter measurements
- **`generated_data.csv`** - Generated test data created by the utilities scripts

### Baseline Data  
- **`basedata.txt`** - Simple baseline data for basic statistical testing
- **`basedata_deviation.txt`** - Data with added variations for testing deviation analysis

## Usage

Load any of these files in the main notebook:

```python
# Load sample manufacturing data
pc = read_csv_data('data/sample_manufacturing_data.csv', 'Temperature')

# Load baseline data  
pc = read_csv_data('data/basedata.txt')
```

## Data Format

CSV files should have:
- Header row with column names
- One measurement per row
- Numeric data for analysis columns