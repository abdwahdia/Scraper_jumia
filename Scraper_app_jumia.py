import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup
from requests import get
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


st.markdown("<h1 style='text-align: center; color: black;'>JUMIA DATA SCRAPER APP</h1>", unsafe_allow_html=True)

st.markdown("""
This app performs simple webscraping of data from jumia over multiples pages!
* **Python libraries:** base64, pandas, streamlit, requests, bs4
* **Data source:** [Jumia](https://www.jumia.sn/).
""")

st.sidebar.header('User Input Features')
Pages1 = st.sidebar.selectbox('Phone data pages', list([int(p) for p in np.arange(2, 23)]))
Pages2 = st.sidebar.selectbox('Phone data with rating pages', list([int(p) for p in np.arange(2, 23)]))

# Background function
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

add_bg_from_local('img_file3.jpg') 
# Web scraping of Vehicles data on expat-dakar
@st.cache_data

# Fonction for web scraping vehicle data
def load_phone_data(mul_page):
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.jumia.sn/telephones-smartphones/?page={p}#catalog-listing"
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('article', class_ ='prd _fb col c-prd')
        data = []
        for container in containers:
            try :
                Details = container.find('div', class_ ='info').h3.text
                Price = container.find('div', class_ ='prc').text.replace(' ', '').replace('FCFA', '')
                Old_Price = container.find('div', class_ ='old').text.replace(' ', '').replace('FCFA', '')
                Discount_Percentage = container.find('div', class_ ='bdg _dsct _sm').text.replace('%', '')
                # Rate = container.find('div', class_ ='stars _s').text.replace(' out of 5', '')
                Imagelink = container.find('div', class_ = 'img-c').img.attrs['data-src']

                obj = {
                        'Details': Details,
                        'Price': Price,
                        'Old_Price': Old_Price,
                        'Discount_Percentage': Discount_Percentage,
                        # 'Rate': Rate
                        'Imagelink' : Imagelink
                    }
                data.append(obj)
            except:
               pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)
    return df

def load_phone_data1(mul_page):
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.jumia.sn/telephones-smartphones/?page={p}#catalog-listing"
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('article', class_ ='prd _fb col c-prd')
        data = []
        for container in containers:
            try :
                Details = container.find('div', class_ ='info').h3.text
                Price = container.find('div', class_ ='prc').text.replace(' ', '').replace('FCFA', '')
                Old_Price = container.find('div', class_ ='old').text.replace(' ', '').replace('FCFA', '')
                Discount_Percentage = container.find('div', class_ ='bdg _dsct _sm').text.replace('%', '')
                Rate = container.find('div', class_ ='stars _s').text.replace(' out of 5', '')
                Imagelink = container.find('div', class_ = 'img-c').img.attrs['data-src']


                obj = {
                        'Details': Details,
                        'Price': Price,
                        'Old_Price': Old_Price,
                        'Discount_Percentage': Discount_Percentage,
                        'Rate': Rate, 
                        'Imagelink': Imagelink
                    }
                data.append(obj)
            except:
               pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)
    return df


Phone_data_mul_pag = load_phone_data(Pages1)
Phone_data_mul_pag1 = load_phone_data1(Pages2)


# Download Vehicles data
@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

def load(dataframe, title, key, key1) :
    st.markdown("""
    <style>
    div.stButton {text-align:center}
    </style>""", unsafe_allow_html=True)

    if st.button(title,key1):
        # st.header(title)

        st.subheader('Display data dimension')
        st.write('Data dimension: ' + str(dataframe.shape[0]) + ' rows and ' + str(dataframe.shape[1]) + ' columns.')
        st.dataframe(dataframe)

        csv = convert_df(dataframe)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='Data.csv',
            mime='text/csv',
            key = key)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css('style.css')        


load(Phone_data_mul_pag, 'Telephones-Smartphones data', '1', '101')
load(Phone_data_mul_pag1, 'Telephones-Smartphones data with ratings', '2', '102')
