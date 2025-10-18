# Workshop 1 - Systems Analysis: GEFCom2012 Load Forecasting

## 📋 Descripción del Proyecto

Este repositorio contiene el análisis de sistemas del **Taller #1** del curso de Análisis y Diseño de Sistemas, enfocado en la competencia **Global Energy Forecasting Competition 2012 (GEFCom2012) - Load Forecasting Track**.

## 🎯 Objetivo de la Competencia

La competencia GEFCom2012 fue diseñada para fomentar la innovación en el pronóstico de demanda eléctrica a corto plazo. El objetivo principal era predecir la carga horaria del sistema para una utility estadounidense en múltiples zonas, manteniendo consistencia jerárquica entre las zonas individuales y la carga agregada del sistema.

### Características Clave:
- **Backcasting**: Reconstrucción de valores históricos faltantes
- **Forecasting**: Predicción de demanda futura
- **Consistencia Jerárquica**: Coherencia entre zonas individuales y carga total
- **Importancia Estratégica**: Mejor programación de generación, trading y mantenimiento

## 📊 Estructura del Dataset

### Componentes Principales:

1. **Historial de Carga**
   - Datos horarios de demanda para 20 zonas individuales
   - Zona 21: Carga total del sistema (suma de todas las zonas)
   - Estructura jerárquica explícita

2. **Historial de Temperatura**
   - Registros horarios de múltiples estaciones meteorológicas
   - Relación no lineal con la carga eléctrica
   - Variable crítica para modelado predictivo

3. **Calendario de Festivos**
   - Información de festivos estadounidenses
   - Impacto significativo en patrones de consumo

4. **Pronósticos de Referencia**
   - Baseline para comparación de mejoras

5. **Archivos de Solución**
   - Valores reales para el período de evaluación
   - Datos ocultos durante la competencia

## ⚠️ Restricciones y Desafíos

### Restricciones Explícitas:
- **Consistencia Jerárquica**: Pronósticos coherentes entre zonas y sistema total
- **Información Incompleta**: Datos de temperatura no totalmente disponibles
- **Relación No Lineal**: Efectos de umbral en temperatura-carga
- **Procedimiento de Evaluación**: Split public/private leaderboard
- **Métricas**: RMSE y MAPE como medidas principales
- **Límites de Envío**: Balance entre exploración y optimización

## 🔍 Análisis de Sistemas

### Elementos del Sistema:

**Inputs:**
- Carga eléctrica histórica (20 zonas + agregada)
- Datos de temperatura horarios
- Lista de festivos

**Procesos:**
- Preparación y limpieza de datos
- Modelado de relaciones carga-temperatura
- Ajuste de consistencia jerárquica

**Outputs:**
- Demanda eléctrica pronosticada por zona y sistema
- Valores backcasted reconstruidos

**Evaluación:**
- Métricas: RMSE y MAPE
- Leaderboards público y privado
- Ranking final basado en datos ocultos

## 🌀 Complejidad y Sensibilidad

### Factores de Complejidad:
- Múltiples fuentes de datos
- Dimensión temporal
- Naturaleza jerárquica
- Comportamiento individual por zona
- Interdependencia entre zonas

### Sensibilidad del Sistema:
- Pequeños cambios en variables de entrada → Grandes efectos en pronósticos
- Desviaciones en temperatura → Errores significativos en demanda
- Acumulación de errores en agregación
- Variabilidad por selección de modelos y hyperparámetros

## 🌪️ Comportamiento Caótico y Aleatorio

### Factores Caóticos:
- Actividades humanas irregulares
- Eventos externos impredecibles
- Cambios abruptos en comportamiento del consumidor
- Efectos de retroalimentación no lineal

### Elementos Aleatorios:
- Ruido en datos meteorológicos
- Propagación de errores de temperatura
- Fluctuaciones aleatorias a nivel de zona
- Interacciones de modelado imprevistas

## 📈 Conclusiones del Análisis

### Fortalezas del Sistema:
- Múltiples fuentes de datos disponibles
- Estructura jerárquica bien definida
- Métricas de evaluación claras
- Contexto rico para construcción de modelos

### Debilidades Identificadas:
- Datos faltantes e incompletos
- Alta sensibilidad a fluctuaciones de temperatura
- Acumulación de errores en agregación
- Influencias caóticas de actividades humanas

### Impacto General:
La competencia demostró el balance necesario entre información disponible, elecciones metodológicas y dinámicas impredecibles de la demanda eléctrica real.

## 👥 Autores

- David Santiago Téllez Melo - 20242020107
- Ana Karina Roa Mora - 20232020118  
- Daniela Bustamante Guerra - 20241020131
- Andrés Felipe Correa Méndez - 20221020141

## 🔗 Referencias

- [Global Energy Forecasting Competition 2012](https://www.kaggle.com/competitions?listOption=completed&hostSegmentIdFilter=2)
- Curso: Análisis y Diseño de Sistemas

---

