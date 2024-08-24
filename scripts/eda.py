import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_data(filename):
    file_path = os.path.join(os.path.dirname(__file__), '..', 'dataset', filename)
    return pd.read_csv(file_path)

def calculate_summary_statistics(df, country_name):
    print(f"\nSummary Statistics for {country_name}:")
    print(df[['GHI', 'DNI', 'DHI', 'Tamb']].agg(['mean', 'median', 'std']))

def check_missing_values(df, country_name):
    print(f"\nMissing Values in {country_name}:")
    print(df.isnull().sum())

def plot_time_series(df, country_name):
    plt.figure(figsize=(10, 6))
    plt.plot(df['Timestamp'], df['GHI'], label='GHI')
    plt.plot(df['Timestamp'], df['DNI'], label='DNI')
    plt.plot(df['Timestamp'], df['DHI'], label='DHI')
    plt.xlabel('Time')
    plt.ylabel('Irradiance (W/m²)')
    plt.title(f'Solar Irradiance Over Time in {country_name}')
    plt.legend()
    plt.show()

def plot_correlation_heatmap(df, country_name):
    plt.figure(figsize=(10, 6))
    corr = df.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title(f'Correlation Heatmap for {country_name}')
    plt.show()

def run_eda():
    # Load the datasets
    benin_df = load_data('benin-malanville.csv')
    sierra_leone_df = load_data('sierraleone-bumbuna.csv')
    togo_df = load_data('togo-dapaong_qc.csv')

    # Perform EDA on each dataset
    for df, country in zip([benin_df, sierra_leone_df, togo_df], 
                           ["Benin", "Sierra Leone", "Togo"]):
        calculate_summary_statistics(df, country)
        check_missing_values(df, country)
        plot_time_series(df, country)
        plot_correlation_heatmap(df, country)

if __name__ == "__main__":
    run_eda()
