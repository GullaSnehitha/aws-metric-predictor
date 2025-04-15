from prophet import Prophet
import plotly.graph_objects as go

def run_prediction(df, metric):
    df = df.rename(columns={"Average": "y"})
    df['ds'] = df.index
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=24, freq='H')
    forecast = model.predict(future)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], mode='lines', name='Forecast'))
    fig.add_trace(go.Scatter(x=df['ds'], y=df['y'], mode='markers', name='Historical'))
    return fig
