# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 13:27:04 2020

@author: Ryan
"""


import streamlit as st
import pandas as pd
import numpy as np

st.set_option('deprecation.showfileUploaderEncoding', False)



def main():
  st.title('Welcome to the EDA web application!')
  file = st.file_uploader("Upload .csv file for analysis", type = ['csv'])
  if file:
    data = pd.read_csv(file)
    st.write('Data Summary \n')
    st.write(data.head())
    if st.checkbox('Explore all data \t \t  (Click to expand)\n'):
        st.write(data)
    if st.checkbox('View dataset dimnesion'):
        st.write(data.shape)
    if st.checkbox('View columns'):
        columns = data.columns.to_list()
        st.write(columns)
    if st.checkbox('View numerical data statistics'):
        st.write(data.describe())
    if st.checkbox('View non-numerical data statistics'):
        if data.describe(include=['object', 'bool']):
            st.write(data.describe(include=['object', 'bool']))
        else:
            st.write('No non-numerical data in the dataset')
    
if __name__ == '__main__':
	main()
