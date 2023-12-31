# pip install streamlit yfinance plotly
import streamlit as st
from datetime import date

import yfinance as yf
from plotly import graph_objs as go

# import library pandas
import pandas as pd

# Import library numpy
import numpy as np

# Import library matplotlib untuk visualisasi
import matplotlib.pyplot as plt

START = "2013-11-19"
END = "2023-06-15"

st.set_page_config(page_title='Visualisasi Data', layout="wide",
    initial_sidebar_state="expanded",)

st.title('Visualisasi Data Saham Provider Indonesia')
st.markdown('Visualisasi 4 Perusahaan Provider di Indonesia')
st.text("""
- PT Telekomunikasi Indonesia Tbk (TLKM.JK)
- PT Indosat Ooredoo Hutchison Tbk (ISAT.JK)
- PT XL Axiata Tbk (EXCL.JK)
- PT Smartfren Telecom Tbk (FREN.JK)
""")


stocks = ('TLKM.JK', 'ISAT.JK', 'EXCL.JK', 'FREN.JK')
selected_stock = st.selectbox('Pilih : ', stocks)


@st.cache
def load_data(ticker):
    data = yf.download(ticker, START, END)
    data.reset_index(inplace=True)
    return data

if st.button("Start"):	
	data_load_state = st.text('Loading data...')
	data = load_data(selected_stock)
	data_load_state.text('')
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="saham"))
	fig.layout.update(title_text='Saham '+selected_stock, xaxis_rangeslider_visible=True)
	st.plotly_chart(fig)
	st.subheader('Historical Data')
	st.text('Berikut adalah dataset saham '+selected_stock+ ' hingga tanggal 15 Juni 2023')
	st.dataframe(data.style.highlight_max(axis=0))
	def convert_df(df):
		return df.to_csv().encode('utf-8')

	csv = convert_df(data)
	st.download_button(
		label="Download data as CSV",
		data=csv,
		file_name=selected_stock+'.csv',
		mime='text/csv',
	)

st.markdown("""Dibuat Oleh:
- Afifuddin Mawardi - 1301194113
- Muhammad Arief  - 1301180265
- Akhmad Izzaturrafi - 1301180114
""")
