def clean_data(df):
    df = df.dropna()
    df = df[df['Average'] >= 0]  # remove negative values if any
    return df
