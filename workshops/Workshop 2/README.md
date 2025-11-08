# Workshop 2 - Systems Analysis & Design: GEFCom2012 Load Forecasting

## 📋 Project Description

This repository contains the development of **Workshop #2** for the Systems Analysis and Design course, focused on designing an electrical load forecasting system for the **Global Energy Forecasting Competition 2012 (GEFCom2012)**.

## 🎯 Workshop Objectives

- Design a robust system architecture for electrical load forecasting
- Apply systems engineering principles considering sensitivity and chaos
- Develop a comprehensive technical design document
- Integrate findings from Workshop #1 into concrete design proposals

## 🏗️ System Architecture

### Main Components

The proposed system follows a modular pipeline architecture with 5 stages:

1. **Data Ingestion** - Multi-source data fusion and validation
2. **Feature Engineering** - Data transformation and cleaning
3. **Model Training** - MLP/LSTM with temporal validation
4. **Forecast Generation** - Consistent hierarchical prediction
5. **Evaluation and Monitoring** - Metrics and continuous feedback

### Included Diagrams

- **Figure 1**: Complete forecasting system architecture
- **Figure 2**: Sensitivity and chaos management mechanisms

## 🛠️ Technology Stack

- **Main Framework**: PyTorch
- **Data Processing**: pandas, NumPy
- **Validation and Metrics**: scikit-learn
- **Visualization**: matplotlib
- **Architecture**: Clean ML Architecture

## 📊 Design Features

### Sensitivity Management
- Continuous validation of input data
- Robust imputation techniques
- Real-time anomaly detection

### Chaotic Behavior Management
- Dropout layers for regularization
- Rolling origin cross-validation
- Ensemble averaging
- Automated feedback mechanisms

### Engineering Principles
- **Modularity**: Decoupled components
- **Scalability**: Pipeline architecture
- **Maintainability**: Clear separation of responsibilities
- **Traceability**: Complete data lineage

## 📄 Main Document

The complete workshop document is located at:
**[Workshop_2.pdf](./Workshop_2.pdf)**

## 👥 Authors

- David Santiago Téllez Melo - 20242020107
- Ana Karina Roa Mora - 20232020118  
- Daniela Bustamante Guerra - 20241020131
- Andrés Felipe Correa Méndez - 20221020141

## 🔗 References

- [Global Energy Forecasting Competition 2012](https://www.kaggle.com/competitions?listOption=completed&hostSegmentIdFilter=2)
- Universidad Distrital Francisco José de Caldas
- Course: Systems Analysis and Design

---
