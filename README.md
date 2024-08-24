# Solar Radiation Analysis: Unveiling Insights from Benin, Sierra Leone, and Togo

## Overview

Welcome to the Solar Radiation Analysis project, where we delve into the intricate details of solar radiation data collected from three West African countries: Benin, Sierra Leone, and Togo. This project is an exploration into the key trends and insights that can be gleaned from solar irradiance, temperature, and other environmental factors that play a crucial role in understanding and optimizing solar energy systems.

This project is divided into two main components:

1. **Exploratory Data Analysis (EDA)**: We perform a thorough analysis of the datasets to extract meaningful insights, identify patterns, and understand the distribution and relationships within the data.

2. **Interactive Dashboard Development**: We build an interactive dashboard using Streamlit that allows users to explore the data dynamically, visualize key trends, and gain insights into solar radiation across the three countries.

### Why This Project Matters

As the world moves towards more sustainable energy sources, understanding solar radiation patterns is essential for optimizing solar energy systems. This project provides a framework for analyzing such data, which can be crucial for researchers, engineers, and policymakers working in the field of renewable energy.

## Project Structure

The project is organized as follows:

````plaintext
├── .vscode/                # VS Code settings
├── .github/                # GitHub Actions workflows
│   └── workflows/
│       ├── unittests.yml   # CI/CD pipeline for running unit tests
├── data/                   # Directory containing the dataset files
│   ├── benin.csv
│   ├── sierra_leone.csv
│   └── togo.csv
├── scripts/                # Python scripts for EDA and dashboard
│   ├── eda.py              # Script for performing exploratory data analysis
│   └── dashboard.py        # Script for running the Streamlit dashboard
├── tests/                  # Unit tests for the project
│   ├── test_eda.py         # Unit tests for the EDA functions
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation (this file)

## Datasets

The datasets used in this project are stored in the `data` directory and include:

- **benin.csv**: Solar radiation data for Benin.
- **sierra_leone.csv**: Solar radiation data for Sierra Leone.
- **togo.csv**: Solar radiation data for Togo.

Each dataset contains the following columns:

- **Timestamp**: Date and time of each observation.
- **GHI**: Global Horizontal Irradiance (W/m²).
- **DNI**: Direct Normal Irradiance (W/m²).
- **DHI**: Diffuse Horizontal Irradiance (W/m²).
- **Tamb**: Ambient Temperature (°C).
- **RH**: Relative Humidity (%).
- **WS**: Wind Speed (m/s).
- **BP**: Barometric Pressure (hPa).
- **TModA**: Temperature of Module A (°C).
- **TModB**: Temperature of Module B (°C).
- **Comments**: Additional notes (if any).

## Exploratory Data Analysis (EDA)
ntal Irradiance (W/m²).
- **Tamb**: Ambient Temperature (°C).
- **RH**: Relative Humidity (%).
- **WS**: Wind Speed (m/s).
- **BP**: Barometric Pressure (hPa).
- **TModA**: Temperature of Module A (°C).
- **TModB**: Temperature of Module B (°C).
- **Comments**: Additional notes (if any).

## Exploratory Data Analysis (EDA)

### Goals

The primary goal of the EDA is to uncover key insights and trends within the datasets. We focus on the following:

- **Summary Statistics**: Understanding the distribution of key variables like GHI, DNI, DHI, and temperature.
- **Missing Values**: Identifying any missing data that could affect the analysis.
- **Time Series Analysis**: Exploring how solar irradiance and other factors vary over time.
- **Correlation Analysis**: Investigating relationships between different variables, such as the correlation between temperature and solar irradiance.

This script will:

- Load the datasets from the `data` directory.
- Calculate summary statistics for each country.
- Identify and report any missing values.
- Generate time series plots and correlation heatmaps for each dataset.

### Interpreting the Results

The EDA will produce outputs in the terminal and display visualizations, helping you to:

- Identify which periods have the highest solar irradiance.
- Understand how temperature and humidity affect solar radiation.
- Detect any anomalies or patterns that warrant further investigation.

### Running the EDA

To run the exploratory data analysis, use the following command:

```bash
python scripts/eda.py

## Interactive Dashboard

### Purpose

The Streamlit dashboard provides an interactive way to explore the data. Users can select a country and dynamically visualize key metrics, enabling them to gain insights without delving into the code.

### Features

- **Time Series Plots**: Visualize how solar irradiance changes over time.
- **Correlation Heatmaps**: Understand the relationships between different environmental factors.

### Running the Dashboard

To launch the dashboard, run:

```bash
streamlit run scripts/dashboard.py

## Setting Up the Project

### Prerequisites

Ensure you have Python 3.x installed. Then, create a virtual environment and install the required dependencies:

```bash
python -m venv env
source env/bin/activate  # On Windows use `.\env\Scripts\activate`
pip install -r requirements.txt
````
