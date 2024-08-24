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
    plt.figure(figsize=(12, 6))
    plt.plot(df['Timestamp'], df['GHI'], label='GHI')
    plt.plot(df['Timestamp'], df['DNI'], label='DNI')
    plt.plot(df['Timestamp'], df['DHI'], label='DHI')
    plt.xlabel('Time')
    plt.ylabel('Irradiance (W/m²)')
    plt.title(f'Solar Irradiance Over Time in {country_name}')
    plt.legend()
    plt.show()

def plot_correlation_heatmap(df, country_name):
    plt.figure(figsize=(10, 8))
    corr = df.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title(f'Correlation Heatmap for {country_name}')
    plt.show()

def clean_data(df):
    # Drop irrelevant columns (like Comments if fully missing)
    if 'Comments' in df.columns:
        df = df.drop(columns=['Comments'])

    # Handle negative or near-zero DNI, GHI, and DHI values
    df['DNI'] = df['DNI'].apply(lambda x: max(x, 0))
    df['GHI'] = df['GHI'].apply(lambda x: max(x, 0))
    df['DHI'] = df['DHI'].apply(lambda x: max(x, 0))

    return df

def run_eda():
    # Load the datasets
    datasets = {
        "Benin": load_data('benin-malanville.csv'),
        "Sierra Leone": load_data('sierraleone-bumbuna.csv'),
        "Togo": load_data('togo-dapaong_qc.csv')
    }

    # Perform EDA on each dataset
    for country, df in datasets.items():
        print(f"\n=== {country} ===")
        print(f"Processing {country} dataset...")
        
        # Summary statistics
        calculate_summary_statistics(df, country)
        
        # Missing values
        check_missing_values(df, country)
        
        # Data Cleaning
        df = clean_data(df)
        
        # Time Series Analysis
        plot_time_series(df, country)
        
        # Correlation Analysis
        plot_correlation_heatmap(df, country)

        print(f"Finished processing {country} dataset.")

if __name__ == "__main__":
    run_eda()



# benin_df = load_data('benin-malanville.csv')
# sierra_leone_df = load_data('sierraleone-bumbuna.csv')
# togo_df = load_data('togo-dapaong_qc.csv')