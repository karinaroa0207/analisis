## Overview
This repository contains the deliverables for the first workshop of the Systems Analysis course.  
The analysis is based on the closed Kaggle competition:  
[Global Energy Forecasting Competition 2012 - Load Forecasting](https://www.kaggle.com/competitions/global-energy-forecasting-competition-2012-load-forecasting)

The goal of the competition was to forecast hourly electricity demand for 20 geographical zones and the total aggregated system using historical load, weather data, and calendar information.

## Authors

David Santiago Téllez Melo – 20242020107

Ana Karina Roa Mora – 20232020118

Daniela Bustamante Guerra – 20241020131

Andrés Felipe Correa Méndez – 20221020141


# Electricity Demand Forecasting System

Electricity demand prediction application based on machine learning, inspired by the GEFCom2012 - Load Forecasting competition.

##  Description

Educational system that predicts hourly electricity consumption using Random Forest. The application includes a graphical interface to facilitate data loading, model training, and exporting results.


## Architecture

The project follows the **MVC (Model-View-Controller)** pattern:
```
electricity_demand_project/
├── data/
│   ├── raw/              # Original datasets
│   └── output/           # Results (submission.csv)
├── models/               # Data models and ML
├── views/                # Graphical user interface (GUI)
├── controllers/          # Control logic
├── utils/                # Utilities
├── tests/                # Test results
├── docs/                 # Documentation
└── main.py               # Entry point
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip

### Installation steps

1. Clone or download the project

2. Install dependencies:
```bash
pip install -r requirements.txt
```

##  Usage

### Run the application
```bash
python main.py
```


### Workflow

1. **Load Dataset**: Click “Load Dataset” and select a CSV file.
   - The CSV must have columns: `datetime`, `load`, `temperature`

2. **Train and Predict**: Click on “Train and Predict.”
   - The system will process the data automatically.
   - You will see a graph comparing actual values vs. predictions.

3. **Export Results**: Click on “Export Results.”
   - `data/output/submission.csv` will be generated with the predictions

##  Included Datasets

The project includes 3 test datasets in `data/raw/`:

- **data_small.csv** (~100 rows): Small dataset for quick testing
- **data_large.csv** (~1000 rows): Large dataset for evaluation
- **data_extreme.csv**: Dataset with extreme cases (missing values, abnormal temperatures)

##  How does it work?

### 1. Data loading
- Reads CSV files with demand and temperature history

### 2. Preprocessing
- **Imputation**: Fills in missing values with the mean
- **Temporal features**: Generates time, day of the week, day of the year, is_weekend
- **Normalization**: Scales temperature between 0 and 1

### 3. Machine learning model
- **Algorithm**: Random Forest Regressor
- **Features**: Temporal features + normalized temperature
- **Target**: Electricity demand (load)

### 4. Prediction and export
- Generate predictions for the dates in the dataset
- Export results in CSV format compatible with competitions


## Main components

### Models (models/)
- `data_model.py`: Data loading and validation
- `preprocessing_model.py`: Feature cleaning and generation
- `ml_model.py`: Training and prediction with Random Forest

### Views (views/)
- `gui_view.py`: Graphical interface with tkinter and matplotlib

### Controllers (controllers/)
- `main_controller.py`: Coordinates all application logic

### Utils (utils/)
- `file_utils.py`: Functions for exporting results

##  Tests

To test the application:

1. Run with `data_small.csv` (quick test)
2. Run with `data_large.csv` (full evaluation)
3. Run with `data_extreme.csv` (extreme cases)

Document the results in `tests/test_results.txt`

##  Output format

The `submission.csv` file has the following format:
```csv
datetime,forecast
2024-01-01 00:00,1500.5
2024-01-01 01:00,1450.3...

```

##  Technologies used

- **Python 3.8+**
- **pandas**: Data manipulation
- **scikit-learn**: Machine Learning (Random Forest)
- **matplotlib**: Graph visualization
- **tkinter**: Graphical interface

##  Notes

- This is an **educational** project focused on learning the complete cycle of an ML system
- The model uses basic parameters; it is not optimized for competition
- The data is simulated/simplified from the actual GEFCom2012 competition

##  Future improvements

- Hyperparameter optimization
- Cross-validation
- More algorithms (XGBoost, LSTM)
- Feature importance analysis
- Evaluation metrics (RMSE, MAE)
=======
