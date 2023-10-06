import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup
from requests import get
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('JUMIA DATA SCRAPER')

st.markdown("""
This app performs simple webscraping of data from jumia over multiples pages!
* **Python libraries:** base64, pandas, streamlit, requests, bs4
* **Data source:** [Jumia](https://www.jumia.sn/).
""")

st.sidebar.header('User Input Features')
Pages1 = st.sidebar.selectbox('Phone data pages', list([int(p) for p in np.arange(2, 23)]))
Pages2 = st.sidebar.selectbox('Phone data with rating pages', list([int(p) for p in np.arange(2, 23)]))
# Pages3 = st.sidebar.selectbox('Apartment data pages', list([int(p) for p in np.arange(2, 300)]))
# Pages4 = st.sidebar.selectbox('Furnished Apartment data pages', list([int(p) for p in np.arange(2, 200)]))
# Pages5= st.sidebar.selectbox('Land data pages', list([int(p) for p in np.arange(2, 200)]))
# Pages6 = st.sidebar.selectbox('House data pages', list([int(p) for p in np.arange(2, 100)]))
# Pages7 = st.sidebar.selectbox('Car rental data pages', list([int(p) for p in np.arange(2, 100)]))
# Pages8 = st.sidebar.selectbox('Equipements-pieces data pages', list([int(p) for p in np.arange(2, 100)]))
# Pages9 = st.sidebar.selectbox('Laptop data pages', list([int(p) for p in np.arange(2, 500)]))
# Pages10 = st.sidebar.selectbox('Phone data pages', list([int(p) for p in np.arange(2, 500)]))
# Pages11 = st.sidebar.selectbox('accessories-multimedia data pages', list([int(p) for p in np.arange(2, 200)]))
# Pages12 = st.sidebar.selectbox('Tv data pages', list([int(p) for p in np.arange(2, 150)]))
# Pages13 = st.sidebar.selectbox('Videos games consoles data pages', list([int(p) for p in np.arange(2, 100)]))
# Pages14 = st.sidebar.selectbox('Tablet data pages', list([int(p) for p in np.arange(2, 100)]))
# Pages15 = st.sidebar.selectbox('Audio-videos equipment data pages', list([int(p) for p in np.arange(2, 60)]))
# Pages16 = st.sidebar.selectbox('Printer-scanners data pages', list([int(p) for p in np.arange(2, 60)]))
# Pages17 = st.sidebar.selectbox('Camera data pages', list([int(p) for p in np.arange(2, 50)]))
# Pages18 = st.sidebar.selectbox('electromenager data pages', list([int(p) for p in np.arange(2, 500)]))

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

                obj = {
                        'Details': Details,
                        'Price': Price,
                        'Old_Price': Old_Price,
                        'Discount_Percentage': Discount_Percentage,
                        # 'Rate': Rate
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

                obj = {
                        'Details': Details,
                        'Price': Price,
                        'Old_Price': Old_Price,
                        'Discount_Percentage': Discount_Percentage,
                        'Rate': Rate
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
# Apartment_data_mul_pag = load_apartment_data(Pages3)
# Furnished_apartment_data_mul_pag = load_furnished_apartment_data(Pages4)
# Land_data_mul_pag = load_land_data(Pages5)
# House_data_mul_pag = load_house_data(Pages6)
# load_car_rental_mul_pag = load_car_rental_data(Pages7)
# load_equipment_pieces_data_mul_pag = load_equipment_pieces_data(Pages8)
# load_laptop_data_mul_pag = load_laptop_data(Pages9)
# load_phone_data_mul_pag = load_phone_data(Pages10)
# load_accessories_multimedia_data_mul_pag = load_accessories_multimedia_data(Pages11)
# load_tv_data_mul_pag = load_tv_data(Pages12)
# load_vid_gam_consol_data_mul_pag = load_vid_gam_consol_data(Pages13)
# load_tablet_data_mul_pag = load_tablet_data(Pages14)
# load_aud_vid_equipment_mul_pag = load_aud_vid_equipment(Pages15)
# load_printer_scanners_data_mul_pag = load_printer_scanners_data(Pages16)
# load_camera_data_mul_pag = load_camera_data(Pages17)
# load_electromenager_data_mul_pag = load_electromenager_data(Pages18)

# Download Vehicles data
@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

def load(dataframe, title, key) :

    st.header(title)

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


load(Phone_data_mul_pag, 'Telephones-Smartphones data', '1')
load(Phone_data_mul_pag1, 'Telephones-Smartphones data with rating', '2')
# load(Apartment_data_mul_pag, 'Scrape apartment data', '3')
# load(Furnished_apartment_data_mul_pag, 'Scrape furnished apartment data', '4')    
# load(Land_data_mul_pag, 'Scrape land data','5')
# load(House_data_mul_pag, 'Scrape house data', '6')
# load(load_car_rental_mul_pag, 'Scrape car rental data', '7')
# load(load_equipment_pieces_data_mul_pag, 'Scrape equipements-pieces data', '8')
# load(load_laptop_data_mul_pag, 'Scrape laptop data', '9')
# load(load_phone_data_mul_pag, 'Scrape phone data', '10')
# load(load_accessories_multimedia_data_mul_pag, 'Scrape accessories-multimedia data', '11')
# load(load_tv_data_mul_pag, 'Scrape tv data', '12')
# load(load_vid_gam_consol_data_mul_pag, 'Scrape videos games consoles data', '13')
# load(load_tablet_data_mul_pag, 'Scrape tablet data','14')
# load(load_aud_vid_equipment_mul_pag, 'Scrape audio-videos equipment data', '15')
# load(load_printer_scanners_data_mul_pag, 'Scrape Printer-scanners data','16')
# load(load_camera_data_mul_pag, 'Scrape camera data', '17')
# load(load_electromenager_data_mul_pag, 'Scrape electromenager data', '18')
