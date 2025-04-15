import streamlit as st
from datetime import datetime
import requests
import pandas as pd


API_URL = "http://localhost:8000"


def analytics_months_tab():
    response = requests.get(f"{API_URL}/monthly_summary/")
    try:
        monthly_summary = response.json()
    except json.JSONDecodeError:
        print("Failed to parse JSON. Response content:")
        print(response.text)
        monthly_summary = None

    df = pd.DataFrame(monthly_summary)
    df.rename(columns={
        "expense_month": "Month Number",
        "month_name": "Month Name",
        "total": "Total"
    }, inplace=True)
    df_sorted = df.sort_values(by="Month Number", ascending=False)
    df_sorted.set_index("Month Number", inplace=True)

    st.title("Expense Breakdown By Months")

    st.bar_chart(data=df_sorted.set_index("Month Name")['Total'], width=0, height=0, color = '#FFA500', use_container_width=True)

    df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)

    st.table(df_sorted.sort_index())

