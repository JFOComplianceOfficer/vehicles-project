# Análisis de anuncios de vehículos en EE. UU.

Aplicación web desarrollada con **Streamlit** y desplegada en **Render** que permite explorar de forma interactiva el conjunto de datos `vehicles_us.csv`, compuesto por anuncios de venta de coches usados en Estados Unidos.

**Aplicación en línea:** https://TU-APP.onrender.com (reemplazar por la URL de Render)

## ¿Para qué sirve?
La aplicación ofrece una vista rápida del mercado de vehículos usados a partir de los anuncios publicados: cuánto kilometraje suelen tener los coches ofertados y cómo se relaciona ese kilometraje con el precio de venta según la condición del vehículo.

## Datos
51.525 anuncios publicados entre mayo de 2018 y abril de 2019, con 13 columnas (precio, año, modelo, condición, cilindros, combustible, kilometraje, transmisión, tipo, color, tracción 4x4, fecha de publicación y días publicados).

Para los gráficos se excluye el 1,75 % de los registros: precios de relleno (menos de 100 USD), precios extremos (más de 100.000 USD) y kilometrajes superiores a 500.000 millas. El detalle está en `notebooks/EDA.ipynb`.

## Funcionalidades
- **Vista previa de los datos:** muestra los primeros registros del conjunto de datos.
- **Histograma:** distribución del kilometraje (`odometer`) de los vehículos anunciados.
- **Gráfico de dispersión:** relación entre kilometraje y precio, coloreada por la condición del vehículo.

Cada visualización se activa con una casilla de verificación (`st.checkbox`), de modo que el usuario decide qué gráficos mostrar.

## Tecnologías
- Python
- pandas
- plotly
- streamlit
- Render (despliegue)

## Estructura del proyecto
```
vehicles-project/
├── .streamlit/
│   └── config.toml      # Configuración del servidor para Render
├── notebooks/
│   └── EDA.ipynb        # Análisis exploratorio de datos
├── app.py               # Aplicación Streamlit
├── vehicles_us.csv      # Conjunto de datos
├── requirements.txt     # Dependencias
├── README.md
└── .gitignore
```

## Ejecución local
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Autor
Juan Felipe Ochoa Ojeda
