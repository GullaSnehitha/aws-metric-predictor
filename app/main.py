import streamlit as st
from app.aws_utils import list_regions, list_instances, list_metrics, fetch_metric_data
from app.predictor import run_prediction
from app.data_cleaner import clean_data
import pandas as pd

st.set_page_config(page_title="AWS Metric Predictor", layout="wide")
st.title("📊 AWS Metric Predictor")

st.markdown("""
<style>
    .block-container {
        padding: 2rem;
    }
    .metric-select-box, .predict-button, .download-section {
        padding: 1rem;
        margin: 1rem 0;
        border: 1px solid #e6e6e6;
        border-radius: 10px;
        background-color: #f9f9f9;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("## 🔧 Select AWS Configuration")

col1, col2, col3 = st.columns(3)
region = col1.selectbox("🌍 Select AWS Region", list_regions())
instance_id = col2.selectbox("💻 Select EC2 Instance", list_instances(region))
selected_metric = col3.selectbox("📈 Select Metric", list_metrics(region, instance_id))

if st.button("🚀 Fetch & Predict Metric"):
    with st.spinner("Fetching and processing data..."):
        raw_data = fetch_metric_data(region, instance_id, selected_metric)
        df = clean_data(raw_data)

    st.markdown("## 📊 Metric Data Visualization")
    st.line_chart(df['Average'])

    st.markdown("## 🔮 Forecasting")
    fig = run_prediction(df, selected_metric)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("## 📥 Download Cleaned Data")
    st.download_button(
        label="Download CSV",
        data=df.to_csv().encode('utf-8'),
        file_name=f"{selected_metric}_cleaned.csv",
        mime="text/csv"
    )
