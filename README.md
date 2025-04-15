# AWS Metric Predictor

An AI-powered Streamlit dashboard to fetch, clean, and predict EC2 metrics like CPUUtilization using AWS CloudWatch data.

## Features

- 📦 AWS region & instance discovery
- 📊 CloudWatch metric selection
- 🧹 Automatic data cleaning
- 🔮 AI/ML forecasting using Prophet
- 📥 Download option for cleaned dataset
- 🐳 Dockerized deployment

## Tech Stack

- Streamlit (for UI)
- Prophet (for time-series forecasting)
- Boto3 (for AWS API calls)
- Plotly (for interactive charts)
- Docker (for containerization)

## To Run

```bash
git clone <repo-url>
cd aws-metric-predictor
pip install -r requirements.txt
streamlit run app/main.py
