
import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Bank Churn Analytics", layout="wide")
st.title("Customer Segmentation & Churn Pattern Analytics")
st.subheader("European Banking")

file_path = "European_Bank (1).csv"

if Path(file_path).exists():
    df = pd.read_csv(file_path)
    churn_rate = df["Exited"].mean() * 100
    total = len(df)
    churned = int(df["Exited"].sum())

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Customers", f"{total:,}")
    c2.metric("Customers Exited", f"{churned:,}")
    c3.metric("Overall Churn Rate", f"{churn_rate:.2f}%")

    st.header("Churn by Country")
    st.bar_chart(df.groupby("Geography")["Exited"].mean() * 100)

    st.header("Dataset Preview")
    st.dataframe(df.head(20), use_container_width=True)
else:
    st.error("Dataset CSV file not found. Please check the file name.")
