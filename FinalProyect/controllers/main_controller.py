import pandas as pd
import numpy as np

from models.data_model import DataModel
from models.preprocessing_model import PreprocessingModel
from models.ml_model import MLModel
from utils.file_utils import save_submission

class MainController:
    def __init__(self, view):
        self.view = view
        self.data_model = DataModel()
        self.preprocessing_model = PreprocessingModel()
        self.ml_model = MLModel()
        self.df = None
        self.predictions = None
        self.future_predictions = None
        self.future_dates = None

    def load_dataset(self):
        self.view.load_dataset()  # Primero abre el diálogo
        if self.view.file_path:  # Ahora sí verifica si se seleccionó algo
            try:
                self.df = self.data_model.load_data(self.view.file_path)
                self.view.show_message("Dataset cargado exitosamente.")
                self.preprocess_data()  # Preprocesar automáticamente
            except Exception as e:
                self.view.show_message(f"Error al cargar dataset: {str(e)}")

    def preprocess_data(self):
        if self.df is not None:
            try:
                self.df = self.preprocessing_model.preprocess(self.df)
                self.view.show_message("Datos preprocesados exitosamente.")
            except Exception as e:
                self.view.show_message(f"Error en preprocesamiento: {str(e)}")
        else:
            self.view.show_message("No hay datos cargados.")

    def train_and_predict(self):
        if self.df is not None:
            try:
                self.view.show_progress()
                # Separar features (X) del target (y)
                X = self.df[['hour', 'day_of_week', 'day_of_year', 'is_weekend', 'temperature_normalized']]
                y = self.df['load']
                self.ml_model.train(X, y)
                self.predictions = self.ml_model.predict(X)
                self.view.hide_progress()
                self.view.show_message("Entrenamiento y predicción completados.")
                # Mostrar gráfica
                dates = self.df['datetime']
                actual = self.df['load']
                self.view.plot_predictions(dates, actual, self.predictions)
            except Exception as e:
                self.view.hide_progress()
                self.view.show_message(f"Error en entrenamiento/predicción: {str(e)}")
        else:
            self.view.show_message("No hay datos cargados.")

    def export_results(self):
        if self.predictions is not None and self.df is not None:
            try:
                dates = self.df['datetime']
                save_submission(self.predictions, dates, 'data/output/submission.csv')
                self.view.show_message("Resultados exportados a data/output/submission.csv")
            except Exception as e:
                self.view.show_message(f"Error al exportar resultados: {str(e)}")
        else:
            self.view.show_message("No hay predicciones para exportar.")

    def predict_future_dates(self):
        if self.df is None:
            self.view.show_message("Primero debes cargar y entrenar un modelo.")
            return
        
        try:
            # Obtener número de días del campo de entrada
            days = int(self.view.days_entry.get())
            
            if days <= 0 or days > 365:
                self.view.show_message("Por favor ingresa un número entre 1 y 365 días.")
                return
            
            self.view.show_message(f"Generando predicción para los próximos {days} días...")

            # Obtener la última fecha del dataset
            last_date = pd.to_datetime(self.df['datetime'].iloc[-1])
            self.view.show_message(f"Última fecha del dataset: {last_date}")

            # Generar fechas futuras (24 horas por día)
            future_dates = []
            for day in range(1, days + 1):
                for hour in range(24):
                    future_date = last_date + pd.Timedelta(days=day, hours=hour)
                    future_dates.append(future_date)

            # Generar temperaturas sintéticas realistas
            base_temp = self.df['temperature'].mean()
            temp_variation = self.df['temperature'].std()
            future_temps = np.random.normal(base_temp, temp_variation, len(future_dates))

            self.view.show_message(f"Fechas generadas: {len(future_dates)} registros")

            # Crear DataFrame con fechas y temperaturas futuras
            future_df = pd.DataFrame({
                'datetime': future_dates,
                'temperature': future_temps
            })
            self.view.show_message("DataFrame futuro creado correctamente.")

            # Generar features usando el preprocessing model
            future_df = self.preprocessing_model.preprocess(future_df)
            self.view.show_message("Features generadas correctamente.")

            # Extraer features para predicción
            X_future = future_df[['hour', 'day_of_week', 'day_of_year', 'is_weekend', 'temperature_normalized']]
            self.view.show_message(f"Features extraídas: {X_future.shape[0]} registros con {X_future.shape[1]} columnas.")

            # Hacer predicciones
            self.view.show_progress()
            future_predictions = self.ml_model.predict(X_future)
            self.view.hide_progress()

            self.view.show_message(f"Predicción completada: {len(future_predictions)} valores generados.")

            # Mostrar gráfica de predicciones futuras
            self.view.plot_predictions(future_df['datetime'], future_predictions, future_predictions)

            # Guardar predicciones futuras
            self.future_predictions = future_predictions
            self.future_dates = future_df['datetime']

            # Exportar automáticamente
            save_submission(future_predictions, future_df['datetime'], 'data/output/future_predictions.csv')
            self.view.show_message("Predicciones futuras exportadas a data/output/future_predictions.csv")

        except ValueError as ve:
            self.view.show_message(f"Error de valor: {str(ve)}")
        except KeyError as ke:
            self.view.show_message(f"Error: columna no encontrada - {str(ke)}")
        except Exception as e:
            self.view.hide_progress()
            self.view.show_message(f"Error en predicción futura: {type(e).__name__} - {str(e)}")