import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset yang sudah dibersihkan
@st.cache_data
def load_data():
    url = "https://drive.google.com/uc?id=1KEHPXqk70Dm3LCRoUvGIJ4HzxZEueiw2" 
    return pd.read_csv(url)

df = load_data()

# Sidebar
st.sidebar.title("Dashboard Pengamatan Kualitas Udara")
st.sidebar.write("Gunakan filter untuk menyesuaikan data.")

# Pilihan Stasiun
stations = df["station"].unique()
selected_station = st.sidebar.selectbox("Pilih Stasiun", stations)

# Filter berdasarkan stasiun
filtered_df = df[df["station"] == selected_station]

# Judul Dashboard
st.title("📊 Dashboard Kualitas Udara")

# Visualisasi Tren PM2.5
st.subheader("Tren PM2.5 dari Tahun ke Tahun")
pm25_trend = filtered_df.groupby(filtered_df['datetime'].str[:4])['PM2.5'].mean()

fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=pm25_trend.index, y=pm25_trend.values, marker='o', ax=ax)
ax.set_xlabel("Tahun")
ax.set_ylabel("Rata-rata PM2.5")
ax.set_title("Tren PM2.5")
st.pyplot(fig)

# Hubungan Suhu vs PM2.5
st.subheader("Hubungan Suhu terhadap Polusi PM2.5")
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(x=filtered_df["TEMP"], y=filtered_df["PM2.5"], alpha=0.5, ax=ax)
sns.regplot(x=filtered_df["TEMP"], y=filtered_df["PM2.5"], scatter=False, ax=ax)
ax.set_xlabel("Suhu (°C)")
ax.set_ylabel("PM2.5")
ax.set_title("Scatter Plot Suhu vs PM2.5")
st.pyplot(fig)

st.write("Dashboard ini menampilkan analisis kualitas udara berdasarkan data yang telah dibersihkan.")
