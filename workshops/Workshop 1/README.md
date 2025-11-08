# Workshop 1 - Systems Analysis: GEFCom2012 Load Forecasting

## 📋 Project Description

This repository contains the systems analysis for **Workshop #1** of the Systems Analysis and Design course, focused on the **Global Energy Forecasting Competition 2012 (GEFCom2012) - Load Forecasting Track**.

## 🎯 Competition Objective

The GEFCom2012 competition was designed to foster innovation in short-term electricity demand forecasting. The main objective was to predict hourly system load for a US utility across multiple zones, while maintaining hierarchical consistency between individual zones and the aggregated system load.

### Key Features:
- **Backcasting**: Reconstruction of missing historical values
- **Forecasting**: Prediction of future demand
- **Hierarchical Consistency**: Coherence between individual zones and total load
- **Strategic Importance**: Improved generation scheduling, trading, and maintenance

## 📊 Dataset Structure

### Main Components:

1. **Load History**
   - Hourly demand data for 20 individual zones
   - Zone 21: Total system load (sum of all zones)
   - Explicit hierarchical structure

2. **Temperature History**
   - Hourly records from multiple weather stations
   - Non-linear relationship with electrical load
   - Critical variable for predictive modeling

3. **Holiday Calendar**
   - US holiday information
   - Significant impact on consumption patterns

4. **Reference Forecasts**
   - Baseline for improvement comparison

5. **Solution Files**
   - Actual values for the evaluation period
   - Data hidden during the competition

## ⚠️ Constraints and Challenges

### Explicit Constraints:
- **Hierarchical Consistency**: Coherent forecasts between zones and total system
- **Incomplete Information**: Temperature data not fully available
- **Non-linear Relationship**: Threshold effects in temperature-load relationship
- **Evaluation Procedure**: Public/private leaderboard split
- **Metrics**: RMSE and MAPE as main measures
- **Submission Limits**: Balance between exploration and optimization

## 🔍 Systems Analysis

### System Elements:

**Inputs:**
- Historical electrical load (20 zones + aggregated)
- Hourly temperature data
- Holiday list

**Processes:**
- Data preparation and cleaning
- Load-temperature relationship modeling
- Hierarchical consistency adjustment

**Outputs:**
- Forecasted electrical demand by zone and system
- Reconstructed backcasted values

**Evaluation:**
- Metrics: RMSE and MAPE
- Public and private leaderboards
- Final ranking based on hidden data

## 🌀 Complexity and Sensitivity

### Complexity Factors:
- Multiple data sources
- Temporal dimension
- Hierarchical nature
- Individual zone behavior
- Interdependence between zones

### System Sensitivity:
- Small changes in input variables → Large effects on forecasts
- Temperature deviations → Significant demand errors
- Error accumulation in aggregation
- Variability due to model selection and hyperparameters

## 🌪️ Chaotic and Random Behavior

### Chaotic Factors:
- Irregular human activities
- Unpredictable external events
- Abrupt changes in consumer behavior
- Non-linear feedback effects

### Random Elements:
- Noise in meteorological data
- Temperature error propagation
- Random fluctuations at zone level
- Unforeseen modeling interactions

## 📈 Analysis Conclusions

### System Strengths:
- Multiple available data sources
- Well-defined hierarchical structure
- Clear evaluation metrics
- Rich context for model building

### Identified Weaknesses:
- Missing and incomplete data
- High sensitivity to temperature fluctuations
- Error accumulation in aggregation
- Chaotic influences from human activities

### Overall Impact:
The competition demonstrated the necessary balance between available information, methodological choices, and unpredictable dynamics of real electricity demand.

## 👥 Authors

- David Santiago Téllez Melo - 20242020107
- Ana Karina Roa Mora - 20232020118  
- Daniela Bustamante Guerra - 20241020131
- Andrés Felipe Correa Méndez - 20221020141

## 🔗 References

- [Global Energy Forecasting Competition 2012](https://www.kaggle.com/competitions?listOption=completed&hostSegmentIdFilter=2)
- Course: Systems Analysis and Design

---
