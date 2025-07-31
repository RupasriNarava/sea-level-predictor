# Sea Level Predictor

This project is part of the freeCodeCamp Data Analysis with Python certification.  
It analyzes historical sea level data and uses linear regression to predict future sea level changes.

## Project Description

The dataset contains global average sea level measurements from 1880 to 2014, provided by the U.S. Environmental Protection Agency.  
The goal is to visualize the historical trend and estimate the sea level rise by the year 2050 using two regression models.

## Files

| File | Description |
|------|-------------|
| `epa-sea-level.csv` | Dataset containing year and sea level measurements |
| `sea_level_predictor.py` | Main script for data analysis and plotting |
| `main.py` | Script to execute the plot generation |
| `test_module.py` | Unit test file to validate the plot output |

## Features

- Creates a scatter plot of historical sea level data  
- Fits a linear regression line using all available data (1880–2014)  
- Fits a second regression line using data from 2000 onward  
- Predicts sea level rise through the year 2050  
- Saves the final plot as `sea_level_plot.png`

## Requirements

- Python 3.x  
- Pandas  
- Matplotlib  
- SciPy

Install dependencies with:

```bash
pip install pandas matplotlib scipy
