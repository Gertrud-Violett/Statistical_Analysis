# Utilities Directory

This directory contains helper scripts for generating and manipulating test data.

## Scripts

### `createrandomdata.py`
Generates synthetic manufacturing data for testing purposes.

**Usage:**
```bash
python utilities/createrandomdata.py
```

**Features:**
- Creates realistic manufacturing data with controlled parameters
- Generates Temperature, Pressure, Flow Rate, and Diameter measurements
- Adds realistic noise and variations
- Outputs to `data/generated_data.csv`

### `data_deviation.py`  
Creates variations and deviations in existing datasets for testing statistical methods.

**Usage:**
```bash
python utilities/data_deviation.py -h  # Show help
python utilities/data_deviation.py input_file.txt
```

**Features:**
- Reads data from text files
- Applies controlled deviations
- Useful for testing process control limits
- Supports various input formats

## Purpose

These utilities help you:
1. **Generate test data** when you don't have real manufacturing data
2. **Create controlled variations** for testing statistical methods  
3. **Validate analysis tools** with known data characteristics
4. **Learn statistical concepts** with predictable datasets