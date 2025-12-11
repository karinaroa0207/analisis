import pandas as pd
from sklearn.preprocessing import MinMaxScaler

class PreprocessingModel:
    def impute_missing_values(self, df):
        # Imputar 'load' solo si la columna existe (para datos históricos)
        if 'load' in df.columns:
            df['load'] = df['load'].fillna(df['load'].mean())
        
        # Imputar 'temperature' siempre (existe tanto en históricos como futuros)
        df['temperature'] = df['temperature'].fillna(df['temperature'].mean())
        
        return df

    def normalize_temperature(self, df):
        scaler = MinMaxScaler()
        df['temperature_normalized'] = scaler.fit_transform(df[['temperature']])
        return df

    def preprocess(self, df):
        # Primero imputar valores faltantes
        df = self.impute_missing_values(df)

        # Convertir la columna 'datetime' a formato datetime
        df['datetime'] = pd.to_datetime(df['datetime'])

        # Generar nuevas columnas a partir de datetime
        df['hour'] = df['datetime'].dt.hour
        df['day_of_week'] = df['datetime'].dt.dayofweek
        df['day_of_year'] = df['datetime'].dt.dayofyear
        df['is_weekend'] = df['datetime'].dt.dayofweek.apply(lambda x: 1 if x >= 5 else 0)

        # Finalmente normalizar temperatura
        df = self.normalize_temperature(df)

        return df