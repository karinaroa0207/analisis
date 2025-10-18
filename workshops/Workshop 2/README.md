# Workshop 2 - Systems Analysis & Design: GEFCom2012 Load Forecasting

## 📋 Descripción del Proyecto

Este repositorio contiene el desarrollo del **Taller #2** del curso de Análisis y Diseño de Sistemas, enfocado en el diseño de un sistema de pronóstico de carga eléctrica para la **Global Energy Forecasting Competition 2012 (GEFCom2012)**.

## 🎯 Objetivos del Taller

- Diseñar una arquitectura de sistema robusta para pronóstico de carga eléctrica
- Aplicar principios de ingeniería de sistemas considerando sensibilidad y caos
- Desarrollar un documento de diseño técnico completo
- Integrar los hallazgos del Taller #1 en propuestas de diseño concretas


## 🏗️ Arquitectura del Sistema

### Componentes Principales

El sistema propuesto sigue una arquitectura de pipeline modular con 5 etapas:

1. **Ingesta de Datos** - Fusión y validación de datos multi-fuente
2. **Ingeniería de Features** - Transformación y limpieza de datos
3. **Entrenamiento de Modelos** - MLP/LSTM con validación temporal
4. **Generación de Pronósticos** - Predicción jerárquica consistente
5. **Evaluación y Monitoreo** - Métricas y retroalimentación continua

### Diagramas Incluidos

- **Figura 1**: Arquitectura completa del sistema de pronóstico
- **Figura 2**: Mecanismos de manejo de sensibilidad y caos

## 🛠️ Stack Tecnológico

- **Framework Principal**: PyTorch
- **Procesamiento de Datos**: pandas, NumPy
- **Validación y Métricas**: scikit-learn
- **Visualización**: matplotlib
- **Arquitectura**: Clean ML Architecture

## 📊 Características del Diseño

### Manejo de Sensibilidad
- Validación continua de datos de entrada
- Técnicas de imputación robusta
- Detección de anomalías en tiempo real

### Gestión de Comportamiento Caótico
- Capas de dropout para regularización
- Validación cruzada de origen rodante
- Promediado de ensembles
- Mecanismos de retroalimentación automática

### Principios de Ingeniería
- **Modularidad**: Componentes desacoplados
- **Escalabilidad**: Arquitectura pipeline
- **Mantenibilidad**: Separación clara de responsabilidades
- **Trazabilidad**: Linaje completo de datos

## 📄 Documento Principal

El documento completo del taller se encuentra en:
**[Workshop_2.pdf](./Workshop_2.pdf)**

## 👥 Autores

- David Santiago Téllez Melo - 20242020107
- Ana Karina Roa Mora - 20232020118  
- Daniela Bustamante Guerra - 20241020131
- Andrés Felipe Correa Méndez - 20221020141


## 🔗 Referencias

- [Global Energy Forecasting Competition 2012](https://www.kaggle.com/competitions?listOption=completed&hostSegmentIdFilter=2)
- Universidad Distrital Francisco José de Caldas
- Curso: Análisis y Diseño de Sistemas

---

