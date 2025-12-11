import pandas as pd
import os

class DataModel:
    def load_data(self, file_path):
        try:
            # Verificar que el archivo existe
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"El archivo '{file_path}' no existe.")
            
            # Verificar que el archivo no está vacío
            if os.path.getsize(file_path) == 0:
                raise ValueError(f"El archivo '{file_path}' está vacío.")
            
            # Leer el CSV con encoding explícito
            df = pd.read_csv(file_path, encoding='utf-8')
            
            # Verificar columnas requeridas
            required_columns = ['datetime', 'load', 'temperature']
            if not all(col in df.columns for col in required_columns):
                raise ValueError(f"El archivo CSV debe contener las columnas: {required_columns}. Columnas encontradas: {list(df.columns)}")
            
            return df
            
        except FileNotFoundError as e:
            raise FileNotFoundError(str(e))
        except pd.errors.EmptyDataError:
            raise ValueError("El archivo CSV está vacío o tiene un formato incorrecto.")
        except Exception as e:
            raise Exception(f"Error al cargar el archivo: {str(e)}")