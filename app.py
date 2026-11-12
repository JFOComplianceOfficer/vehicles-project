import pandas as pd
import plotly.express as px
import streamlit as st

# Lectura de datos
car_data = pd.read_csv('vehicles_us.csv')

# Limpieza básica (misma lógica del notebook EDA.ipynb)
car_data['is_4wd'] = car_data['is_4wd'].fillna(0).astype(int)
clean_data = car_data[
    car_data['price'].between(100, 100000)
    & ((car_data['odometer'] <= 500000) | car_data['odometer'].isna())
]

# Encabezado
st.header('Análisis de anuncios de venta de vehículos en EE. UU.')
total_ads = f'{len(clean_data):,}'.replace(',', '.')
st.write(
    f'Explora {total_ads} anuncios de coches usados. '
    'Selecciona los gráficos que quieres ver.'
)
st.caption(
    'Se excluyen los anuncios con precio fuera del rango 100–100.000 USD '
    'y con kilometraje superior a 500.000 millas.'
)

# Vista previa opcional de los datos
if st.checkbox('Mostrar los primeros registros del conjunto de datos'):
    st.dataframe(clean_data.head(20))

# Casilla 1: histograma
build_histogram = st.checkbox('Construir un histograma del kilometraje (odometer)')

if build_histogram:
    st.write('Distribución del kilometraje de los vehículos anunciados')
    fig_hist = px.histogram(
        clean_data,
        x='odometer',
        nbins=50,
        title='Distribución del kilometraje (odometer)',
        labels={'odometer': 'Kilometraje (millas)'},
    )
    st.plotly_chart(fig_hist)

# Casilla 2: gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión: kilometraje vs. precio')

if build_scatter:
    st.write('Relación entre el kilometraje y el precio, por condición del vehículo')
    fig_scatter = px.scatter(
        clean_data,
        x='odometer',
        y='price',
        color='condition',
        opacity=0.4,
        title='Kilometraje vs. precio',
        labels={'odometer': 'Kilometraje (millas)', 'price': 'Precio (USD)', 'condition': 'Condición'},
    )
    st.plotly_chart(fig_scatter)
