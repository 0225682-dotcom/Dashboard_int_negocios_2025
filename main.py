import streamlit as st
import pandas as pd
# -----------------------------------------------------------
# CONFIGURACIÓN INICIAL
# -----------------------------------------------------------
st.set_page_config(
    page_title="Tablero de Inteligencia de Negocios",
    page_icon="📊",
    layout="wide"
)
st.title("📊 Tablero Interactivo – Inteligencia de Negocios")
st.caption("Universidad Panamericana · Campus CDMX")

# -----------------------------------------------------------
# CARGA DE DATOS
# -----------------------------------------------------------
@st.cache_data 
def load_data():# Habilidad de crear cache, Carga de datos 1 vez para no volver a cargar los datos
  url = UBERdataset.xlsx
    all_sheets=pd.read_excel(url,sheet_name=None)
  return all_sheets["Switchbaks"]
df = load_data()
# -----------------------------------------------------------
# PESTAÑAS PRINCIPALES
# -----------------------------------------------------------
tab1, tab2, tab3 = st.tabs(["📈 Documentación General", "🔍 Datos", "📊 Gráficas"])
with tab1:
  st.subheader("Documentacion General del tablero")
  st.markdown(
"""
# 🚀 Business Intelligence Dashboard

**Análisis, visualización y toma de decisiones inteligentes**

Este repositorio contiene el tablero desarrollado para la materia de **Inteligencia de Negocios**, cuyo objetivo es convertir datos crudos en decisiones rápidas, claras y accionables. Nada de humo: solo insights útiles y visualizaciones que dicen la verdad sin maquillarla.

---

## 📊 Objetivo del proyecto

Diseñar y construir un dashboard que permita:

* Identificar patrones clave en los datos.
* Evaluar métricas críticas para la toma de decisiones.
* Detectar oportunidades, anomalías y áreas de mejora.
* Presentar la información de manera visual, intuitiva y lista para ejecutivos con prisa… o estudiantes con entrega mañana.

---

## 🧠 ¿Qué resuelve este tablero?

* **Centraliza** la información relevante.
* **Reduce el tiempo de análisis** al mínimo (sí, tu futuro yo te lo va a agradecer).
* **Facilita decisiones basadas en datos**, no en corazonadas.
* **Aporta claridad inmediata** gracias a visualizaciones limpias y ordenadas.

---

## 🛠️ Tecnologías utilizadas

* Lenguaje: Python 
* Visualización:  Matplotlib
* Procesamiento: Pandas /

---

## 📁 Estructura del repositorio

```
├── data/
│   ├── raw/             # Datos originales
│   └── cleaned/         # Datos procesados listos para análisis
├── src/
│   ├── preprocessing/   # Scripts de limpieza y transformación
│   ├── analysis/        # Cálculos, KPIs, modelos
│   └── visuals/         # Código para gráficos o dashboards
├── dashboard/           # Archivo(s) del tablero final
└── README.md            # Este documento
```

---

## 📈 Principales métricas del tablero


* KPIs clave (ventas, margen, rotación, eficiencia, etc.)
* Segmentación por cliente, categoría o canal
* Comparativas temporales
)
* Análisis de comportamiento (tendencias, estacionalidad
* Indicadores operativos o estratégicos
"""
)
with tab2:
  st.subheader("Datos")
  st.dataframe(df)

with tab3:
  st.subheader("Visualizaciones ")
  st.write("Hola Mundo")
