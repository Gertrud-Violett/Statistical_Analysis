# Manufacturing Statistical Analysis Tool

A comprehensive Python tool for manufacturing data analysis using Statistical Process Control (SPC) techniques. Designed for engineers with entry-level statistical knowledge, providing Minitab-like functionality.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/version-1.1.0-green.svg)](CHANGELOG.md)

## Features

- **Process Capability Analysis**: Cp, Cpk, Cpu, Cpl, Pp, Ppk, Cpm, Cpkm calculations
- **Distribution Fitting**: Normal and Weibull distribution analysis  
- **Statistical Tests**: Mann-Whitney U, Kolmogorov-Smirnov tests
- **Multivariate Analysis**: PCA, bivariate distribution plots
- **Visualization**: Multi-vari charts, box plots, normal probability plots
- **Tolerance Intervals**: Statistical tolerance calculation

## Quick Start

### 1. Installation
```bash
pip install pandas numpy matplotlib seaborn scipy scikit-learn plotly
```

### 2. Launch Jupyter Notebook
```bash
jupyter notebook Statistical_Analysis.ipynb
```

Or use the provided batch file:
```bash
run_jupyter.bat
```

### 3. Basic Usage
```python
# Load your data
pc = read_csv_data('data/sample_manufacturing_data.csv', 'Temperature')

# Set specification limits
pc.set_specification_limits(usl=26.0, lsl=24.0, target=25.0)

# Calculate capability
capability_results = pc.calculate_capability()
print(capability_results)
```

## Project Structure

```
Statistical_Analysis/
├── Statistical_Analysis.ipynb    # Main analysis notebook
├── data/                         # Sample data files
│   ├── sample_manufacturing_data.csv
│   ├── basedata.txt
│   └── basedata_deviation.txt
├── utilities/                    # Helper scripts
│   ├── createrandomdata.py      # Generate test data
│   └── data_deviation.py        # Create data variations
├── examples/                     # Example outputs
│   └── basedata.png             # Sample analysis plot
├── run_jupyter.bat              # Windows batch file to start Jupyter
└── export.bat                   # Export notebook to HTML
```

## Sample Data

The `data/` directory contains sample manufacturing data:
- **sample_manufacturing_data.csv**: Multi-variable manufacturing dataset
- **basedata.txt**: Simple baseline data for testing
- **generated_data.csv**: Generated test data

## Utilities

### Generate Test Data
```bash
python utilities/createrandomdata.py
```

### Create Data Variations  
```bash
python utilities/data_deviation.py -h
```

## Key Analysis Methods

### Process Capability
```python
# Calculate Cp, Cpk, Pp, Ppk
capability = pc.calculate_capability()
```

### Distribution Analysis
```python
# Fit normal and Weibull distributions
pc.fit_distributions()
```

### Statistical Tests
```python
# Mann-Whitney U test
result = pc.mann_whitney_test(group1, group2)

# Kolmogorov-Smirnov test
result = pc.ks_test(data, distribution)
```

### Visualization
```python
# Multi-vari chart
pc.create_multivari_chart()

# Normal probability plot
pc.normal_probability_plot()
```

## Requirements

- Python 3.8+
- pandas
- numpy  
- matplotlib
- seaborn
- scipy
- scikit-learn
- plotly

## Requirements

- Python 3.8+
- pandas
- numpy  
- matplotlib
- seaborn
- scipy
- scikit-learn
- plotly

## Version History

See [CHANGELOG.md](CHANGELOG.md) for detailed version history and release notes.

## License

MIT License - See LICENSE file for details.

## Support

For questions or issues, please refer to the examples in the notebook or create an issue in the repository.
