# Changelog

All notable changes to the Manufacturing Statistical Analysis Tool will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.1] - 2025-11-04 (WIP)
Minor Feature addition to main.(WIP)

### WIP (Work In Progress)
- **Uniform Probability Plot**
  - plot_uniform_probability method added
  - 

## [1.1.0] - 2025-11-02

### 🎉 Major Repository Reorganization

This release focuses on improving user experience through better organization and documentation.

### Added
- **Automated Setup Script** (`setup.py`)
  - Checks Python version compatibility
  - Installs all dependencies automatically
  - Launches Jupyter notebook with one command
  
- **Requirements File** (`requirements.txt`)
  - Easy dependency management
  - Version-pinned packages for stability
  - Includes all necessary libraries

- **Organized Directory Structure**
  - `data/` - All sample data files in one location
  - `utilities/` - Helper scripts for data generation
  - `examples/` - Reference outputs and visualizations

- **Comprehensive Documentation**
  - Updated main README.md with quick start guide
  - Added README.md in each subdirectory
  - Clear usage examples and code snippets

- **Git Configuration**
  - Added `.gitignore` to prevent clutter
  - Excludes cache files, outputs, and IDE files

### Changed
- **Improved README.md**
  - Simplified structure with essential information
  - Added badges for license and Python version
  - Clear project structure visualization
  - Step-by-step usage instructions

- **Enhanced Batch Files**
  - Updated `run_jupyter.bat` to launch specific notebook
  - Added user-friendly console messages

- **Better File Organization**
  - Moved sample data files to `data/` directory
  - Relocated utility scripts to `utilities/` directory
  - Organized example outputs in `examples/` directory

### Fixed
- Removed matplotlib style deprecation warning by updating to current seaborn style syntax
- Cleaned up `.ipynb_checkpoints` directories
- Fixed file path references to work with new directory structure

### Removed
- Scattered data files from root directory
- Unnecessary checkpoint directories
- Redundant or outdated documentation

## [1.0.0] - 2025-10-01

### Initial Public Release

### Added
- **Core Statistical Analysis Features**
  - Process Control class with comprehensive SPC methods
  - Capability analysis (Cp, Cpk, Cpu, Cpl, Pp, Ppk, Cpm, Cpkm)
  - Distribution fitting (Normal and Weibull)
  - Tolerance interval calculations
  - Normal probability plotting

- **Statistical Tests**
  - Mann-Whitney U test
  - Kolmogorov-Smirnov test
  - Anderson-Darling test
  - Normality tests

- **Multivariate Analysis**
  - Principal Component Analysis (PCA)
  - Partial Least Squares Regression (PLS)
  - Bivariate distribution analysis
  - Correlation plotting

- **Visualization Tools**
  - Multi-vari charts
  - Box plots with statistical annotations
  - Control charts
  - Probability plots
  - Interactive Plotly visualizations

- **Data Generation Utilities**
  - `createrandomdata.py` - Generate synthetic manufacturing data
  - `data_deviation.py` - Create controlled data variations

- **Sample Data**
  - `sample_manufacturing_data.csv` - Multi-variable dataset
  - `basedata.txt` - Simple baseline data
  - `basedata_deviation.txt` - Variation testing data

- **Documentation**
  - Comprehensive Jupyter notebook with examples
  - Inline code documentation
  - Sample usage demonstrations

### Features
- **Minitab-like Interface**
  - Similar input/output parameters to Minitab
  - Familiar terminology for engineers
  - Easy transition from commercial software

- **Entry-level Friendly**
  - Designed for engineers with basic statistical knowledge
  - Clear explanations and examples
  - Visual outputs for better understanding

- **Production Ready**
  - Tested with real manufacturing data
  - Robust error handling
  - Efficient algorithms for large datasets

## Version History Summary

| Version | Date       | Key Changes |
|---------|------------|-------------|
| 1.1.0   | 2025-11-02 | Repository reorganization, improved documentation |
| 1.0.0   | 2025-10-01 | Initial public release with core features |

---

## How to Upgrade

### From 1.0.0 to 1.1.0

1. **Pull latest changes:**
   ```bash
   git pull origin main
   ```

2. **Install new dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Update file paths in custom scripts:**
   - Sample data is now in `data/` directory
   - Use `data/sample_manufacturing_data.csv` instead of `sample_manufacturing_data.csv`

4. **Run setup script (optional):**
   ```bash
   python setup.py
   ```

## Contributing

We welcome contributions! Please see our contribution guidelines for details on:
- Reporting bugs
- Suggesting features
- Submitting pull requests

## License

This project is licensed under the BSD-2-Clause License - see the [LICENSE](LICENSE) file for details.

## Support

For questions, issues, or feature requests:
- Open an issue on GitHub
- Check existing documentation in the README files
- Review example outputs in the `examples/` directory

---

**Note:** This changelog is maintained to help users track changes and understand the evolution of the tool. For detailed commit history, please refer to the Git log.