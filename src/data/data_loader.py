import pandas as pd


class DataLoader:
    def __init__(self, data_path):
        self.data_path = data_path
        
    def load_data(self):
        try:
            data = pd.read_csv(self.data_path)
            
            if not data.empty:
                return data
            return None
        
        except Exception as e:
            raise e
