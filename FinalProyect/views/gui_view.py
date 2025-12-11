import tkinter as tk
from tkinter import ttk, filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.dates as mdates
import numpy as np
import pandas as pd

class GUIView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sistema de Pronóstico de Demanda Eléctrica")
        self.root.geometry("1000x700")

        self.file_path = None

        # Crear frames principales
        self.left_frame = tk.Frame(self.root, width=300, bg='#f0f0f0')
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)
        self.left_frame.pack_propagate(False)  # Mantener el ancho fijo

        self.right_frame = tk.Frame(self.root)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Crear botones naranjas en left_frame
        self.btn_load = tk.Button(
            self.left_frame, 
            text="Cargar Dataset", 
            command=self.load_dataset,
            bg='#FF8C00',
            fg='white',
            font=('Arial', 11, 'bold'),
            width=20,
            height=2,
            cursor='hand2'
        )
        
        self.btn_train = tk.Button(
            self.left_frame, 
            text="Entrenar y Predecir", 
            command=self.train_predict,
            bg='#FF8C00',
            fg='white',
            font=('Arial', 11, 'bold'),
            width=20,
            height=2,
            cursor='hand2'
        )
        
        self.btn_export = tk.Button(
            self.left_frame, 
            text="Exportar Resultados", 
            command=self.export_results,
            bg='#FF8C00',
            fg='white',
            font=('Arial', 11, 'bold'),
            width=20,
            height=2,
            cursor='hand2'
        )

        # Posicionar botones en left_frame con más espacio
        self.btn_load.pack(pady=20, padx=10)
        self.btn_train.pack(pady=20, padx=10)
        self.btn_export.pack(pady=20, padx=10)

        # Campo de entrada para días futuros
        self.label_days = tk.Label(self.left_frame, text="Días a predecir:", bg='#f0f0f0', font=('Arial', 10))
        self.days_entry = tk.Entry(self.left_frame, width=10)
        self.days_entry.insert(0, "7")  # Valor por defecto

        self.btn_predict_future = tk.Button(
            self.left_frame,
            text="Predecir Futuro",
            command=self.predict_future,
            bg='#FF8C00',
            fg='white',
            font=('Arial', 11, 'bold'),
            width=20,
            height=2,
            cursor='hand2'
        )

        # Posicionar nuevos elementos
        self.label_days.pack(pady=10)
        self.days_entry.pack(pady=10)
        self.btn_predict_future.pack(pady=10)

        # Área de texto para logs en right_frame (parte superior)
        self.text_area = tk.Text(self.right_frame, height=10, width=80, bg='#ffffff', font=('Consolas', 9))
        self.text_area.pack(fill=tk.BOTH, padx=5, pady=5)

        # Frame para gráficas en right_frame (parte inferior)
        self.plot_frame = tk.Frame(self.right_frame, bg='white')
        self.plot_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Progress bar en la parte inferior de toda la ventana
        self.progress_bar = ttk.Progressbar(self.root, mode='indeterminate')

    def load_dataset(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.file_path = file_path
            self.show_message(f"Dataset cargado: {file_path}")

    def train_predict(self):
        self.show_message("Función en desarrollo")

    def export_results(self):
        self.show_message("Función en desarrollo")

    def predict_future(self):
        self.show_message("Predicción de futuro en desarrollo")

    def show_message(self, message):
        self.text_area.insert(tk.END, message + "\n")
        self.text_area.see(tk.END)

    def plot_predictions(self, dates, actual, predicted):
        # Limpiar el plot_frame
        for widget in self.plot_frame.winfo_children():
            widget.destroy()

        # Crear figura
        fig = Figure(figsize=(9, 5))
        ax = fig.add_subplot(111)

        # Convertir fechas a datetime si no lo son
        dates = pd.to_datetime(dates)

        # Convertir a numpy arrays para comparación
        actual_array = np.array(actual)
        predicted_array = np.array(predicted)

        # Si actual y predicted son iguales, solo graficar predicciones (futuro)
        if np.array_equal(actual_array, predicted_array):
            ax.plot(dates, predicted, label='Predicción Futura', color='green', linewidth=2, linestyle='-')
            ax.set_title("Predicción de Demanda Futura", fontsize=14, fontweight='bold')
        else:
            # Graficar ambas líneas (modo normal)
            ax.plot(dates, actual, label='Real', color='blue', linewidth=2)
            ax.plot(dates, predicted, label='Predicción', color='red', linewidth=2, linestyle='--')
            ax.set_title("Demanda Real vs Predicha", fontsize=14, fontweight='bold')

        # Configurar etiquetas
        ax.set_xlabel("Fecha", fontsize=11)
        ax.set_ylabel("Demanda (MW)", fontsize=11)
        ax.grid(True, alpha=0.3)

        # Agregar leyenda
        ax.legend(fontsize=10)

        # Formatear fechas en el eje X
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
        ax.xaxis.set_major_locator(mdates.AutoDateLocator())
        
        # Rotar etiquetas de fecha para mejor legibilidad
        fig.autofmt_xdate(rotation=45)

        # Insertar gráfica en plot_frame
        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def show_progress(self):
        self.progress_bar.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)
        self.progress_bar.start()

    def hide_progress(self):
        self.progress_bar.stop()
        self.progress_bar.pack_forget()

    def run(self):
        self.root.mainloop()