# IT Service Management Visualization Tool

This project provides visualization tools for IT Service Management (ITSM) analysis, focusing on the relationship between SLA violations and business service criticality.

## Features

The tool generates two complementary visualizations:

1. **Service Performance Scatter Plot**
   - Displays individual IT services plotted by their SLA violations and criticality
   - Each service is labeled for easy identification
   - Includes services like CRM Support, Data Analytics, DevOps, Cloud Hosting, and Cybersecurity

2. **Prioritization Matrix Heatmap**
   - Shows a priority matrix based on business impact and SLA violations
   - Color-coded for easy interpretation (green scale)
   - Categorizes business criticality into four levels:
     - Business-vital
     - Business-kritisch
     - Business-wichtig
     - Keinen unmittelbaren Einfluss auf Business

## Requirements

- Python 3.x
- matplotlib
- numpy

## Installation

1. Clone this repository
2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

Run the visualization script:
```bash
python plot.py
```

This will generate a figure with both visualizations side by side, providing a comprehensive view of IT service performance and prioritization.
