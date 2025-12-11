from views.gui_view import GUIView
from controllers.main_controller import MainController

def main():
    view = GUIView()
    controller = MainController(view)
    
    # Conectar botones con métodos del controller
    view.btn_load.config(command=controller.load_dataset)
    view.btn_train.config(command=controller.train_and_predict)
    view.btn_export.config(command=controller.export_results)
    view.btn_predict_future.config(command=controller.predict_future_dates)
    
    view.run()

if __name__ == "__main__":
    main()