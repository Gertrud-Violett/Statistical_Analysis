#!/usr/bin/env python3
"""
Statistical Analysis Tool Setup Script
Helps users install dependencies and run the application
"""

import sys
import subprocess
import os
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8 or higher required")
        print(f"   Current version: {sys.version}")
        return False
    print(f"✅ Python {sys.version.split()[0]} detected")
    return True

def install_requirements():
    """Install Python requirements"""
    try:
        print("📦 Installing Python dependencies...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                      check=True)
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def check_jupyter():
    """Check if Jupyter is available"""
    try:
        subprocess.run([sys.executable, "-m", "jupyter", "--version"], 
                      capture_output=True, check=True)
        print("✅ Jupyter is available")
        return True
    except subprocess.CalledProcessError:
        print("❌ Jupyter not found, installing...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "jupyter"], 
                          check=True)
            print("✅ Jupyter installed successfully")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install Jupyter: {e}")
            return False

def launch_notebook():
    """Launch the Jupyter notebook"""
    try:
        print("🚀 Launching Statistical Analysis notebook...")
        subprocess.run([sys.executable, "-m", "jupyter", "notebook", "Statistical_Analysis.ipynb"])
    except KeyboardInterrupt:
        print("\n👋 Notebook closed by user")
    except Exception as e:
        print(f"❌ Failed to launch notebook: {e}")

def main():
    """Main setup routine"""
    print("🔧 Statistical Analysis Tool Setup")
    print("=" * 40)
    
    # Check prerequisites
    if not check_python_version():
        sys.exit(1)
    
    # Install dependencies
    if not install_requirements():
        sys.exit(1)
    
    # Check Jupyter
    if not check_jupyter():
        sys.exit(1)
    
    print("\n📊 Sample data available in 'data/' directory")
    print("🛠️  Utility scripts available in 'utilities/' directory")
    print("📈 Example outputs available in 'examples/' directory")
    
    # Launch notebook
    print("\n" + "=" * 40)
    choice = input("Launch Statistical Analysis notebook now? (Y/n): ").lower()
    if choice != 'n':
        launch_notebook()
    
    print("\n✅ Setup complete!")
    print("   To run later: jupyter notebook Statistical_Analysis.ipynb")
    print("   Or use: run_jupyter.bat (Windows)")

if __name__ == "__main__":
    main()