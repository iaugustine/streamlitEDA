# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 13:27:04 2020

@author: Ryan
"""


import streamlit as st
import pandas as pd
import numpy as np
import io
import seaborn as sns
import matplotlib.pyplot as plt

st.set_option('deprecation.showfileUploaderEncoding', False)

st.set_option('deprecation.showPyplotGlobalUse', False)

def main():
  st.title('Welcome to the EDA web application!')
  file = st.file_uploader("Upload .csv file for analysis", type = ['csv'])
  if file:
    csv = pd.read_csv(file)
    data = pd.DataFrame(csv)
    st.write('Data Successfully Loaded.  \n')
    st.write('Dimensions:')
    st.write(data.shape)
    st.write('Sample data:')
    st.write(data.head())
    columns = data.columns.to_list()
    
    
    
        
    if st.checkbox('Check NULL values count'):
        st.write(data.isnull().sum())
        
    if st.checkbox('Check Unique Value count'):
        st.write(data.nunique())
        
    if st.checkbox('Check datatypes'):
        st.write(data.dtypes)
        
    if st.checkbox('Explore all data \t \t  (Click arrow on top right corner to expand)\n'):
        st.write(data)
        
    # if st.checkbox('Check dataset dimension'):
    #     st.write(data.shape)
 
    if st.checkbox("Explore Selected Column Data"):
        selected_columns = st.multiselect("Select Columns",columns)
        new_df = data[selected_columns]
        st.dataframe(new_df)
    if st.checkbox('Correlation Matrix'):
        st.write(data.corr())
        ax = sns.heatmap(data.corr(),annot=True)
        st.pyplot()
    # Graphical analysis out of scope for current deployment. WIll attempt later
    # if st.checkbox('Graphs'):
    #     gtype = st.selectbox('Select option', ['No Selection','bar', 'line', 'histogram'],index = 0)
    #     if gtype == 'bar':
    #         selX=st.selectbox('Select X axis column', columns)
    #         selY=st.selectbox('Select Y axis column', columns)
    #         Xdf = data[selX]
    #         Ydf = data[selY]
            

            #st.write(chartDF.head())
        #     st.altair_chart(chartDF)
        # if gtype == 'line':
        #     selcol = st.multiselect("Select Columns",columns)
        #     st.pyplot(plt.hist(data[selcol]))
            
        #     # st.pyplot(fig)
        #     st.write(selcol[0])
            
        # if gtype == 'histogram':
        #     selcol=st.radio('Select column', columns)
        #     chart= data[columns].plot(kind='hist')
        #     st.pyplot(chart)
		
		
    
        
    if st.checkbox('Examine column names'):
        st.write(columns)
        
    if st.checkbox('Examine numerical data statistics'):
        st.write(data.describe())
        
    if st.checkbox('Examine non-numerical data statistics(Only applicable if dataset has non-integer data'): #need to handle when no non numeric data exists
        val = data.describe(include=['object', 'bool'])
        if val is not None:
            st.write(data.describe(include=['object', 'bool']))
        else:
            st.write('No non-numerical data in the dataset')
            
    if st.checkbox('Check Other Information'):
        buf = io.StringIO()
        data.info(verbose = True,buf=buf)
        s = buf.getvalue()
        st.write(s)
    
  st.write('\n\nPersonal project created by Immanuel Ryan Augustine. Connect with me on Linked in: https://www.linkedin.com/in/immanuelryan/')
    
if __name__ == '__main__':
	main()
