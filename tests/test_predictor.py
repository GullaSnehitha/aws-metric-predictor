from app import predictor
import pandas as pd

sample_data = pd.DataFrame({
    'Average': [10, 15, 20, 30, 25, 20, 10],
    'Timestamp': pd.date_range(end=pd.Timestamp.now(), periods=7)
}).set_index('Timestamp')

def test_run_prediction():
    fig = predictor.run_prediction(sample_data, "CPUUtilization")
    assert fig is not None
