# Educational Electricity Load Forecasting System

## 📋 Project Description

This repository contains the academic project for the **Systems Analysis and Design** course, implementing a modular electricity load forecasting system based on the GEFCom2012 competition. The project demonstrates the application of systems engineering principles to build a robust and reproducible forecasting framework.

## 🎯 Project Objectives

- Design and implement a modular forecasting system for electricity demand prediction
- Apply systems analysis and design principles to handle complex forecasting challenges
- Develop a reproducible framework suitable for educational purposes
- Integrate modern deep learning approaches with traditional forecasting methods

## 🏗️ System Architecture

### Modular Pipeline
The system follows a structured five-stage architecture:

1. **Data Ingestion** - Collection and validation of multi-source data
2. **Feature Engineering** - Creation of temporal, weather, and calendar features
3. **Model Training** - Implementation of MLP and LSTM models using PyTorch
4. **Forecast Generation** - Production of hierarchical consistent predictions
5. **Evaluation & Monitoring** - Continuous performance assessment and feedback

### Technical Implementation
- **Framework**: PyTorch-based deep learning implementation
- **Architecture**: Clean ML principles with clear separation of concerns
- **Models**: Multilayer Perceptron (MLP) and Long Short-Term Memory (LSTM)
- **Validation**: Rolling-origin cross-validation for realistic evaluation

## 📊 Key Features

### System Design
- **Modularity**: Independent, testable components
- **Reproducibility**: Transparent and well-documented workflow
- **Flexibility**: Easy model interchangeability
- **Robustness**: Handling of sensitive and chaotic data patterns

### Technical Capabilities
- Dual-model approach (MLP for tabular data + LSTM for sequences)
- Hierarchical forecasting consistency
- Comprehensive feature engineering
- Continuous validation and monitoring

## 📚 Academic Deliverables

This repository contains the complete academic project including:

- **Workshop 1**: Systems analysis of GEFCom2012 competition
- **Workshop 2**: System design and architecture specification  
- **Research Paper**: IEEE format technical paper
- **Technical Report**: Comprehensive project documentation
- **Academic Poster**: Visual project summary
- **Source Code**: Modular implementation

## 🛠️ Technology Stack

- **Deep Learning**: PyTorch
- **Data Processing**: pandas, NumPy
- **Validation**: scikit-learn
- **Visualization**: matplotlib
- **Development**: Python 3.x

## 👥 Team Members

- David Santiago Téllez Melo - 20242020107
- Ana Karina Roa Mora - 20232020118  
- Daniela Bustamante Guerra - 20241020131
- Andrés Felipe Correa Méndez - 20221020141

**Systems Engineering Program**  
Faculty of Engineering  
Universidad Distrital Francisco José de Caldas  
Bogotá, Colombia

## 📖 Academic Context

Course: **Systems Analysis and Design**  
Project: **Educational Electricity Load Forecasting System**  
Case Study: **GEFCom2012 Load Forecasting Competition**

## 🔗 References

- Global Energy Forecasting Competition 2012 (GEFCom2012)
- PyTorch Deep Learning Library
- Clean Architecture Principles
- Universidad Distrital Francisco José de Caldas

---

*This project demonstrates the application of systems engineering principles to build an educational forecasting framework, emphasizing modularity, reproducibility, and practical implementation.*
