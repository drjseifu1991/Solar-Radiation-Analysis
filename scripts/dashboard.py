import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

@st.cache
def load_data(filename):
    file_path = os.path.join(os.path.dirname(__file__), '..', 'dataset', filename)
    return pd.read_csv(file_path)

def plot_time_series(df, country_name):
    st.subheader(f'Solar Irradiance Over Time in {country_name}')
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df['Timestamp'], df['GHI'], label='GHI')
    ax.plot(df['Timestamp'], df['DNI'], label='DNI')
    ax.plot(df['Timestamp'], df['DHI'], label='DHI')
    ax.set_xlabel('Time')
    ax.set_ylabel('Irradiance (W/m²)')
    ax.set_title(f'Solar Irradiance Over Time in {country_name}')
    ax.legend()
    st.pyplot(fig)  # Display the plot in Streamlit

def plot_correlation_heatmap(df, country_name):
    st.subheader(f'Correlation Heatmap for {country_name}')
    corr = df.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
    ax.set_title(f'Correlation Heatmap for {country_name}')
    st.pyplot(fig)  # Display the plot in Streamlit

def main():
    st.title("Solar Radiation Analysis Dashboard")

    country = st.sidebar.selectbox("Select Country", ["benin-malanville", "sierraleone-bumbuna", "togo-dapaong_qc"])
    
    data_file = f"{country.lower().replace(' ', '_')}.csv"
    df = load_data(data_file)

    if st.checkbox("Show Raw Data"):
        st.write(df.head())

    # Convert 'Timestamp' to datetime if necessary
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

    plot_time_series(df, country)
    plot_correlation_heatmap(df, country)

if __name__ == "__main__":
    main()
