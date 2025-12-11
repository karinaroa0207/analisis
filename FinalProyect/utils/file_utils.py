import pandas as pd

def save_submission(predictions, dates, output_path='data/output/submission.csv'):
    try:
        df = pd.DataFrame({'datetime': dates, 'forecast': predictions})
        df.to_csv(output_path, index=False)
        return True
    except Exception as e:
        print(f"Error saving submission: {e}")
        return False
