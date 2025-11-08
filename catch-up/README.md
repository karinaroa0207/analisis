# Design and Implementation of an Educational Electricity Load Forecasting System: A Modular and Adaptive Approach

## 📋 Project Overview

This repository contains the complete academic project for the Systems Analysis and Design course, presenting a modular and adaptive framework for electricity load forecasting based on the GEFCom2012 competition dataset.

## 🎯 Project Objectives

- Design and implement a robust, modular forecasting system for electricity demand prediction
- Integrate MLP and LSTM models within a clean architecture framework
- Ensure reproducibility and educational value through transparent implementation
- Address sensitivity and chaotic behavior in load forecasting systems

## 🏗️ System Architecture

### Modular Pipeline Design
The system follows a five-stage modular architecture:

1. **Data Ingestion** - Multi-source data collection and validation
2. **Feature Engineering** - Temporal, weather, and calendar feature generation
3. **Model Training** - MLP and LSTM implementation with PyTorch
4. **Forecast Generation** - Hierarchical consistent prediction
5. **Evaluation & Monitoring** - Continuous performance assessment

### Clean ML Implementation
- **Data Layer**: Standardization and preprocessing
- **Feature Layer**: Engineered features (HDD/CDD, lagged variables)
- **Model Layer**: PyTorch-based MLP and LSTM networks
- **Validation Layer**: Rolling-origin cross-validation
- **Application Layer**: End-to-end workflow coordination

## 📊 Key Features

### Technical Innovations
- **Dual-Model Approach**: MLP for tabular data + LSTM for sequential patterns
- **Hierarchical Consistency**: Zone-level and aggregated forecasting
- **Robust Validation**: Rolling-origin cross-validation mimicking real-world conditions
- **Sensitivity Management**: Dropout regularization and ensemble averaging

### Educational Value
- Reproducible, well-documented codebase
- Clear separation of concerns in architecture
- Comprehensive documentation and reporting
- Suitable for academic and research purposes



## 🛠️ Technology Stack

- **Deep Learning**: PyTorch
- **Data Processing**: pandas, NumPy
- **Validation**: scikit-learn
- **Visualization**: matplotlib
- **Architecture**: Clean ML principles

## 👥 Authors

- **David Santiago Téllez Melo** (20242020107)
- **Ana Karina Roa Mora** (20232020118)  
- **Daniela Bustamante Guerra** (20241020131)
- **Andrés Felipe Correa Méndez** (20221020141)

**Faculty of Engineering, Systems Engineering Program**  
Universidad Distrital Francisco José de Caldas  
Bogotá, Colombia

## 📚 Academic Context

This project was developed as part of the **Systems Analysis and Design** course, focusing on applying engineering principles to complex forecasting systems using the GEFCom2012 Load Forecasting competition as a case study.

## 🔗 References

- Global Energy Forecasting Competition 2012 (GEFCom2012)
- PyTorch Deep Learning Library
- Clean Machine Learning Architecture principles
- Universidad Distrital Francisco José de Caldas

---

*This project represents a comprehensive educational approach to electricity load forecasting, combining modern deep learning techniques with robust systems engineering principles.*
