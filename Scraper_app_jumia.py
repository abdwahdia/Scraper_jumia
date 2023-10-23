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
Pages1 = st.sidebar.selectbox('Smartphones data pages', list([int(p) for p in np.arange(2, 24)]))
Pages2 = st.sidebar.selectbox('TV data pages', list([int(p) for p in np.arange(2, 7)]))
Pages3 = st.sidebar.selectbox('Educative tablets data pages', list([int(p) for p in np.arange(2, 6)]))
Pages4 = st.sidebar.selectbox('House supplies pages', list([int(p) for p in np.arange(2, 5)]))
Pages5 = st.sidebar.selectbox('Decorative furniture pages', list([int(p) for p in np.arange(2, 7)]))
Pages6 = st.sidebar.selectbox('Supplies data pages', list([int(p) for p in np.arange(2, 9)]))
Pages7 = st.sidebar.selectbox('House and desktop data pages', list([int(p) for p in np.arange(2, 11)]))
Pages8 = st.sidebar.selectbox('Bathroom tools data pages', list([int(p) for p in np.arange(2, 9)]))
Pages9 = st.sidebar.selectbox('Bed tools data pages', list([int(p) for p in np.arange(2, 10)]))
Pages10 = st.sidebar.selectbox('Ventilation and heating tools data pages', list([int(p) for p in np.arange(2, 7)]))
Pages11 = st.sidebar.selectbox('House decoration tools data pages', list([int(p) for p in np.arange(2, 21)]))
Pages12 = st.sidebar.selectbox('Perfumes data pages', list([int(p) for p in np.arange(2, 11)]))
Pages13 = st.sidebar.selectbox('Health care tools data pages', list([int(p) for p in np.arange(2, 8)]))
Pages14 = st.sidebar.selectbox('Dental hygiene tools data pages', list([int(p) for p in np.arange(2, 10)]))
Pages15 = st.sidebar.selectbox('Parapharmacy tools data pages', list([int(p) for p in np.arange(2, 9)]))
Pages16 = st.sidebar.selectbox('watch data pages', list([int(p) for p in np.arange(2, 3)]))





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
        Url = f"https://www.jumia.sn/smartphones/?page={p}#catalog-listing"
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('a', class_ ='core')
        links =  []
        link_jumia = 'https://www.jumia.sn'
        for container in containers:
          link_jumia1 = container['href']
          link = link_jumia + link_jumia1
          links.append(link)
        data = []
        for link in links:
          res = get(link)
          soup = BeautifulSoup(res.text, 'html.parser')
          try :
              Marque = soup.find_all('a', class_ ='_more')[1].text
              # Details = soup.find('h1', class_ = '-fs20 -pts -pbxs').text
              Ancien_Prix =soup.find('span', class_ = '-tal -gy5 -lthr -fs16 -pvxs').text.replace(' ', '').replace('FCFA', '')
              Prix = soup.find('span', class_ = '-b -ltr -tal -fs24 -prxs').text.replace(' ', '').replace('FCFA', '')
              # Reduction_Per = soup.find('span', class_ = 'bdg _dsct _dyn -mls').text.replace('%', '')
              Nombre_Avis =soup.find('a', class_ = '-plxs _more').text.split(' ')[0].strip('(')
              Note = soup.find('div', class_ = 'stars _m _al').text.split(' ')[0]

              obj = {       'Marque': Marque,
                            # 'Details': Details,
                            'Ancien_Prix': int(Ancien_Prix),
                            'Prix': int(Prix),
                            # 'Reduction_Per': Reduction_Per,
                            'Nombre_Avis': int(Nombre_Avis), 
                            'Note': float(Note)
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
        Url = f"https://www.jumia.sn/tvs/?page={p}#catalog-listing"
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('a', class_ ='core')
        links =  []
        link_jumia = 'https://www.jumia.sn'
        for container in containers:
          link_jumia1 = container['href']
          link = link_jumia + link_jumia1
          links.append(link)
        data = []
        for link in links:
          res = get(link)
          soup = BeautifulSoup(res.text, 'html.parser')
          try :
              Marque = soup.find_all('a', class_ ='_more')[1].text
              # Details = soup.find('h1', class_ = '-fs20 -pts -pbxs').text
              Ancien_Prix =soup.find('span', class_ = '-tal -gy5 -lthr -fs16 -pvxs').text.replace(' ', '').replace('FCFA', '')
              Prix = soup.find('span', class_ = '-b -ltr -tal -fs24 -prxs').text.replace(' ', '').replace('FCFA', '')
              # Reduction_Per = soup.find('span', class_ = 'bdg _dsct _dyn -mls').text.replace('%', '')
              Nombre_Avis =soup.find('a', class_ = '-plxs _more').text.split(' ')[0].strip('(')
              Note = soup.find('div', class_ = 'stars _m _al').text.split(' ')[0]

              obj = {       'Marque': Marque,
                            # 'Details': Details,
                            'Ancien_Prix': int(Ancien_Prix),
                            'Prix': int(Prix),
                            # 'Reduction_Per': Reduction_Per,
                            'Nombre_Avis': int(Nombre_Avis), 
                            'Note': float(Note)
                            # 'Rate': Rate
                        }
              data.append(obj)
          except:
              pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)
    return df

def load_data_1(mul_page):
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.jumia.sn/tablettes-educatifs/?page={p}#catalog-listing"
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('a', class_ ='core')
        links =  []
        link_jumia = 'https://www.jumia.sn'
        for container in containers:
          link_jumia1 = container['href']
          link = link_jumia + link_jumia1
          links.append(link)
        data = []
        for link in links:
          res = get(link)
          soup = BeautifulSoup(res.text, 'html.parser')
          try :
              Marque = soup.find_all('a', class_ ='_more')[1].text
              # Details = soup.find('h1', class_ = '-fs20 -pts -pbxs').text
              Ancien_Prix =soup.find('span', class_ = '-tal -gy5 -lthr -fs16 -pvxs').text.replace(' ', '').replace('FCFA', '')
              Prix = soup.find('span', class_ = '-b -ltr -tal -fs24 -prxs').text.replace(' ', '').replace('FCFA', '')
              # Reduction_Per = soup.find('span', class_ = 'bdg _dsct _dyn -mls').text.replace('%', '')
              Nombre_Avis =soup.find('a', class_ = '-plxs _more').text.split(' ')[0].strip('(')
              Note = soup.find('div', class_ = 'stars _m _al').text.split(' ')[0]

              obj = {       'Marque': Marque,
                            # 'Details': Details,
                            'Ancien_Prix': int(Ancien_Prix),
                            'Prix': int(Prix),
                            # 'Reduction_Per': Reduction_Per,
                            'Nombre_Avis': int(Nombre_Avis), 
                            'Note': float(Note)
                            # 'Rate': Rate
                        }
              data.append(obj)
          except:
              pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)
    return df


def load_data_2(mul_page):
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.jumia.sn/maison-bureau-appareils-cuisson/?page={p}#catalog-listing"
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('a', class_ ='core')
        links =  []
        link_jumia = 'https://www.jumia.sn'
        for container in containers:
          link_jumia1 = container['href']
          link = link_jumia + link_jumia1
          links.append(link)
        data = []
        for link in links:
          res = get(link)
          soup = BeautifulSoup(res.text, 'html.parser')
          try :
              Marque = soup.find_all('a', class_ ='_more')[1].text
              # Details = soup.find('h1', class_ = '-fs20 -pts -pbxs').text
              Ancien_Prix =soup.find('span', class_ = '-tal -gy5 -lthr -fs16 -pvxs').text.replace(' ', '').replace('FCFA', '')
              Prix = soup.find('span', class_ = '-b -ltr -tal -fs24 -prxs').text.replace(' ', '').replace('FCFA', '')
              # Reduction_Per = soup.find('span', class_ = 'bdg _dsct _dyn -mls').text.replace('%', '')
              Nombre_Avis =soup.find('a', class_ = '-plxs _more').text.split(' ')[0].strip('(')
              Note = soup.find('div', class_ = 'stars _m _al').text.split(' ')[0]

              obj = {       'Marque': Marque,
                            # 'Details': Details,
                            'Ancien_Prix': int(Ancien_Prix),
                            'Prix': Prix,
                            # 'Reduction_Per': Reduction_Per,
                            'Nombre_Avis': int(Nombre_Avis), 
                            'Note': flaot(Note)
                            # 'Rate': Rate
                        }
              data.append(obj)
          except:
              pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)    
    return df 

def load_data_3(mul_page):
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.jumia.sn/mobilier-decoration/?page={p}#catalog-listing"
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('a', class_ ='core')
        links =  []
        link_jumia = 'https://www.jumia.sn'
        for container in containers:
          link_jumia1 = container['href']
          link = link_jumia + link_jumia1
          links.append(link)
        data = []
        for link in links:
          res = get(link)
          soup = BeautifulSoup(res.text, 'html.parser')
          try :
              Marque = soup.find_all('a', class_ ='_more')[1].text
              # Details = soup.find('h1', class_ = '-fs20 -pts -pbxs').text
              Ancien_Prix =soup.find('span', class_ = '-tal -gy5 -lthr -fs16 -pvxs').text.replace(' ', '').replace('FCFA', '')
              Prix = soup.find('span', class_ = '-b -ltr -tal -fs24 -prxs').text.replace(' ', '').replace('FCFA', '')
              # Reduction_Per = soup.find('span', class_ = 'bdg _dsct _dyn -mls').text.replace('%', '')
              Nombre_Avis =soup.find('a', class_ = '-plxs _more').text.split(' ')[0].strip('(')
              Note = soup.find('div', class_ = 'stars _m _al').text.split(' ')[0]

              obj = {       'Marque': Marque,
                            # 'Details': Details,
                            'Ancien_Prix': int(Ancien_Prix),
                            'Prix': int( Prix),
                            # 'Reduction_Per': Reduction_Per,
                            'Nombre_Avis': int(Nombre_Avis), 
                            'Note': flaot(Note)
                            # 'Rate': Rate
                        }
              data.append(obj)
          except:
              pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)
    return df


def load_data_4(mul_page):
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.jumia.sn/fournitures/?page={p}#catalog-listing"
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('a', class_ ='core')
        links =  []
        link_jumia = 'https://www.jumia.sn'
        for container in containers:
          link_jumia1 = container['href']
          link = link_jumia + link_jumia1
          links.append(link)
        data = []
        for link in links:
          res = get(link)
          soup = BeautifulSoup(res.text, 'html.parser')
          try :
              Marque = soup.find_all('a', class_ ='_more')[1].text
              # Details = soup.find('h1', class_ = '-fs20 -pts -pbxs').text
              Ancien_Prix =soup.find('span', class_ = '-tal -gy5 -lthr -fs16 -pvxs').text.replace(' ', '').replace('FCFA', '')
              Prix = soup.find('span', class_ = '-b -ltr -tal -fs24 -prxs').text.replace(' ', '').replace('FCFA', '')
              # Reduction_Per = soup.find('span', class_ = 'bdg _dsct _dyn -mls').text.replace('%', '')
              Nombre_Avis =soup.find('a', class_ = '-plxs _more').text.split(' ')[0].strip('(')
              Note = soup.find('div', class_ = 'stars _m _al').text.split(' ')[0]

              obj = {       'Marque': Marque,
                            # 'Details': Details,
                            'Ancien_Prix': int( Ancien_Prix),
                            'Prix': int(Prix),
                            # 'Reduction_Per': Reduction_Per,
                            'Nombre_Avis': int(Nombre_Avis), 
                            'Note': float(Note)
                            # 'Rate': Rate
                        }
              data.append(obj)
          except:
              pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)   
    return df

def load_data_5(mul_page): 
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.jumia.sn/maison-bureau-meubles/?page={p}#catalog-listing"
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('a', class_ ='core')
        links =  []
        link_jumia = 'https://www.jumia.sn'
        for container in containers:
          link_jumia1 = container['href']
          link = link_jumia + link_jumia1
          links.append(link)
        data = []
        for link in links:
          res = get(link)
          soup = BeautifulSoup(res.text, 'html.parser')
          try :
              Marque = soup.find_all('a', class_ ='_more')[1].text
              # Details = soup.find('h1', class_ = '-fs20 -pts -pbxs').text
              Ancien_Prix =soup.find('span', class_ = '-tal -gy5 -lthr -fs16 -pvxs').text.replace(' ', '').replace('FCFA', '')
              Prix = soup.find('span', class_ = '-b -ltr -tal -fs24 -prxs').text.replace(' ', '').replace('FCFA', '')
              # Reduction_Per = soup.find('span', class_ = 'bdg _dsct _dyn -mls').text.replace('%', '')
              Nombre_Avis =soup.find('a', class_ = '-plxs _more').text.split(' ')[0].strip('(')
              Note = soup.find('div', class_ = 'stars _m _al').text.split(' ')[0]

              obj = {       'Marque': Marque,
                            # 'Details': Details,
                            'Ancien_Prix': int(Ancien_Prix),
                            'Prix': int(Prix),
                            # 'Reduction_Per': Reduction_Per,
                            'Nombre_Avis': int(Nombre_Avis), 
                            'Note': float(Note)
                            # 'Rate': Rate
                        }
              data.append(obj)
          except:
              pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)
    return df


def load_data_6(mul_page): 
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.jumia.sn/maison-bureau-salle-bain/?page={p}#catalog-listing"
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('a', class_ ='core')
        links =  []
        link_jumia = 'https://www.jumia.sn'
        for container in containers:
          link_jumia1 = container['href']
          link = link_jumia + link_jumia1
          links.append(link)
        data = []
        for link in links:
          res = get(link)
          soup = BeautifulSoup(res.text, 'html.parser')
          try :
              Marque = soup.find_all('a', class_ ='_more')[1].text
              # Details = soup.find('h1', class_ = '-fs20 -pts -pbxs').text
              Ancien_Prix =soup.find('span', class_ = '-tal -gy5 -lthr -fs16 -pvxs').text.replace(' ', '').replace('FCFA', '')
              Prix = soup.find('span', class_ = '-b -ltr -tal -fs24 -prxs').text.replace(' ', '').replace('FCFA', '')
              # Reduction_Per = soup.find('span', class_ = 'bdg _dsct _dyn -mls').text.replace('%', '')
              Nombre_Avis =soup.find('a', class_ = '-plxs _more').text.split(' ')[0].strip('(')
              Note = soup.find('div', class_ = 'stars _m _al').text.split(' ')[0]

              obj = {       'Marque': Marque,
                            # 'Details': Details,
                            'Ancien_Prix': int(Ancien_Prix),
                            'Prix': int(Prix),
                            # 'Reduction_Per': Reduction_Per,
                            'Nombre_Avis': int(Nombre_Avis), 
                            'Note': float(Note)
                            # 'Rate': Rate
                        }
              data.append(obj)
          except:
              pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)
    return df

def load_data_7(mul_page):
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.jumia.sn/linge-de-lit/?page={p}#catalog-listing"
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('a', class_ ='core')
        links =  []
        link_jumia = 'https://www.jumia.sn'
        for container in containers:
          link_jumia1 = container['href']
          link = link_jumia + link_jumia1
          links.append(link)
        data = []
        for link in links:
          res = get(link)
          soup = BeautifulSoup(res.text, 'html.parser')
          try :
              Marque = soup.find_all('a', class_ ='_more')[1].text
              # Details = soup.find('h1', class_ = '-fs20 -pts -pbxs').text
              Ancien_Prix =soup.find('span', class_ = '-tal -gy5 -lthr -fs16 -pvxs').text.replace(' ', '').replace('FCFA', '')
              Prix = soup.find('span', class_ = '-b -ltr -tal -fs24 -prxs').text.replace(' ', '').replace('FCFA', '')
              # Reduction_Per = soup.find('span', class_ = 'bdg _dsct _dyn -mls').text.replace('%', '')
              Nombre_Avis =soup.find('a', class_ = '-plxs _more').text.split(' ')[0].strip('(')
              Note = soup.find('div', class_ = 'stars _m _al').text.split(' ')[0]

              obj = {       'Marque': Marque,
                            # 'Details': Details,
                            'Ancien_Prix': int(Ancien_Prix),
                            'Prix': int(Prix),
                            # 'Reduction_Per': Reduction_Per,
                            'Nombre_Avis': int(Nombre_Avis), 
                            'Note': float(Note)
                            # 'Rate': Rate
                        }
              data.append(obj)
          except:
              pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)    
    return df 

def load_data_8(mul_page):
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.jumia.sn/climatiseur-chauffe-eau/?page={p}#catalog-listing"
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('a', class_ ='core')
        links =  []
        link_jumia = 'https://www.jumia.sn'
        for container in containers:
          link_jumia1 = container['href']
          link = link_jumia + link_jumia1
          links.append(link)
        data = []
        for link in links:
          res = get(link)
          soup = BeautifulSoup(res.text, 'html.parser')
          try :
              Marque = soup.find_all('a', class_ ='_more')[1].text
              # Details = soup.find('h1', class_ = '-fs20 -pts -pbxs').text
              Ancien_Prix =soup.find('span', class_ = '-tal -gy5 -lthr -fs16 -pvxs').text.replace(' ', '').replace('FCFA', '')
              Prix = soup.find('span', class_ = '-b -ltr -tal -fs24 -prxs').text.replace(' ', '').replace('FCFA', '')
              # Reduction_Per = soup.find('span', class_ = 'bdg _dsct _dyn -mls').text.replace('%', '')
              Nombre_Avis =soup.find('a', class_ = '-plxs _more').text.split(' ')[0].strip('(')
              Note = soup.find('div', class_ = 'stars _m _al').text.split(' ')[0]

              obj = {       'Marque': Marque,
                            # 'Details': Details,
                            'Ancien_Prix': int(Ancien_Prix),
                            'Prix': int(Prix),
                            # 'Reduction_Per': Reduction_Per,
                            'Nombre_Avis': int(Nombre_Avis), 
                            'Note': float(Note)
                            # 'Rate': Rate
                        }
              data.append(obj)
          except:
              pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)
    return df

def load_data_9(mul_page):
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.jumia.sn/maison-decoration/?page={p}#catalog-listing"
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('a', class_ ='core')
        links =  []
        link_jumia = 'https://www.jumia.sn'
        for container in containers:
          link_jumia1 = container['href']
          link = link_jumia + link_jumia1
          links.append(link)
        data = []
        for link in links:
          res = get(link)
          soup = BeautifulSoup(res.text, 'html.parser')
          try :
              Marque = soup.find_all('a', class_ ='_more')[1].text
              # Details = soup.find('h1', class_ = '-fs20 -pts -pbxs').text
              Ancien_Prix =soup.find('span', class_ = '-tal -gy5 -lthr -fs16 -pvxs').text.replace(' ', '').replace('FCFA', '')
              Prix = soup.find('span', class_ = '-b -ltr -tal -fs24 -prxs').text.replace(' ', '').replace('FCFA', '')
              # Reduction_Per = soup.find('span', class_ = 'bdg _dsct _dyn -mls').text.replace('%', '')
              Nombre_Avis =soup.find('a', class_ = '-plxs _more').text.split(' ')[0].strip('(')
              Note = soup.find('div', class_ = 'stars _m _al').text.split(' ')[0]

              obj = {       'Marque': Marque,
                            # 'Details': Details,
                            'Ancien_Prix': int(Ancien_Prix),
                            'Prix': int(Prix),
                            # 'Reduction_Per': Reduction_Per,
                            'Nombre_Avis': int(Nombre_Avis), 
                            'Note': float(Note)
                            # 'Rate': Rate
                        }
              data.append(obj)
          except:
              pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)    
    return df

def load_data_10(mul_page): 
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.jumia.sn/sante-beaute-parfums/?page={p}#catalog-listing"
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('a', class_ ='core')
        links =  []
        link_jumia = 'https://www.jumia.sn'
        for container in containers:
          link_jumia1 = container['href']
          link = link_jumia + link_jumia1
          links.append(link)
        data = []
        for link in links:
          res = get(link)
          soup = BeautifulSoup(res.text, 'html.parser')
          try :
              Marque = soup.find_all('a', class_ ='_more')[1].text
              # Details = soup.find('h1', class_ = '-fs20 -pts -pbxs').text
              Ancien_Prix =soup.find('span', class_ = '-tal -gy5 -lthr -fs16 -pvxs').text.replace(' ', '').replace('FCFA', '')
              Prix = soup.find('span', class_ = '-b -ltr -tal -fs24 -prxs').text.replace(' ', '').replace('FCFA', '')
              # Reduction_Per = soup.find('span', class_ = 'bdg _dsct _dyn -mls').text.replace('%', '')
              Nombre_Avis =soup.find('a', class_ = '-plxs _more').text.split(' ')[0].strip('(')
              Note = soup.find('div', class_ = 'stars _m _al').text.split(' ')[0]

              obj = {       'Marque': Marque,
                            # 'Details': Details,
                            'Ancien_Prix': int(Ancien_Prix),
                            'Prix': int(Prix),
                            # 'Reduction_Per': Reduction_Per,
                            'Nombre_Avis': int(Nombre_Avis), 
                            'Note': float(Note)
                            # 'Rate': Rate
                        }
              data.append(obj)
          except:
              pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)
    return df

def load_data_11(mul_page): 
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.jumia.sn/soin-de-sante/?page={p}#catalog-listing"
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('a', class_ ='core')
        links =  []
        link_jumia = 'https://www.jumia.sn'
        for container in containers:
          link_jumia1 = container['href']
          link = link_jumia + link_jumia1
          links.append(link)
        data = []
        for link in links:
          res = get(link)
          soup = BeautifulSoup(res.text, 'html.parser')
          try :
              Marque = soup.find_all('a', class_ ='_more')[1].text
              # Details = soup.find('h1', class_ = '-fs20 -pts -pbxs').text
              Ancien_Prix =soup.find('span', class_ = '-tal -gy5 -lthr -fs16 -pvxs').text.replace(' ', '').replace('FCFA', '')
              Prix = soup.find('span', class_ = '-b -ltr -tal -fs24 -prxs').text.replace(' ', '').replace('FCFA', '')
              # Reduction_Per = soup.find('span', class_ = 'bdg _dsct _dyn -mls').text.replace('%', '')
              Nombre_Avis =soup.find('a', class_ = '-plxs _more').text.split(' ')[0].strip('(')
              Note = soup.find('div', class_ = 'stars _m _al').text.split(' ')[0]

              obj = {       'Marque': Marque,
                            # 'Details': Details,
                            'Ancien_Prix': int(Ancien_Prix),
                            'Prix': int(Prix),
                            # 'Reduction_Per': Reduction_Per,
                            'Nombre_Avis': int(Nombre_Avis), 
                            'Note': float(Note)
                            # 'Rate': Rate
                        }
              data.append(obj)
          except:
              pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)
    return df

def load_data_12(mul_page): 
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.jumia.sn/hygiene-dentaire/?page={p}#catalog-listing"
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('a', class_ ='core')
        links =  []
        link_jumia = 'https://www.jumia.sn'
        for container in containers:
          link_jumia1 = container['href']
          link = link_jumia + link_jumia1
          links.append(link)
        data = []
        for link in links:
          res = get(link)
          soup = BeautifulSoup(res.text, 'html.parser')
          try :
              Marque = soup.find_all('a', class_ ='_more')[1].text
              # Details = soup.find('h1', class_ = '-fs20 -pts -pbxs').text
              Ancien_Prix =soup.find('span', class_ = '-tal -gy5 -lthr -fs16 -pvxs').text.replace(' ', '').replace('FCFA', '')
              Prix = soup.find('span', class_ = '-b -ltr -tal -fs24 -prxs').text.replace(' ', '').replace('FCFA', '')
              # Reduction_Per = soup.find('span', class_ = 'bdg _dsct _dyn -mls').text.replace('%', '')
              Nombre_Avis =soup.find('a', class_ = '-plxs _more').text.split(' ')[0].strip('(')
              Note = soup.find('div', class_ = 'stars _m _al').text.split(' ')[0]

              obj = {       'Marque': Marque,
                            # 'Details': Details,
                            'Ancien_Prix': int(Ancien_Prix),
                            'Prix': int(Prix),
                            # 'Reduction_Per': Reduction_Per,
                            'Nombre_Avis': int(Nombre_Avis), 
                            'Note': float(Note)
                            # 'Rate': Rate
                        }
              data.append(obj)
          except:
              pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)
    return df 

def load_data_13(mul_page):
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.jumia.sn/parapharmacie/?page={p}#catalog-listing"
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('a', class_ ='core')
        links =  []
        link_jumia = 'https://www.jumia.sn'
        for container in containers:
          link_jumia1 = container['href']
          link = link_jumia + link_jumia1
          links.append(link)
        data = []
        for link in links:
          res = get(link)
          soup = BeautifulSoup(res.text, 'html.parser')
          try :
              Marque = soup.find_all('a', class_ ='_more')[1].text
              # Details = soup.find('h1', class_ = '-fs20 -pts -pbxs').text
              Ancien_Prix =soup.find('span', class_ = '-tal -gy5 -lthr -fs16 -pvxs').text.replace(' ', '').replace('FCFA', '')
              Prix = soup.find('span', class_ = '-b -ltr -tal -fs24 -prxs').text.replace(' ', '').replace('FCFA', '')
              # Reduction_Per = soup.find('span', class_ = 'bdg _dsct _dyn -mls').text.replace('%', '')
              Nombre_Avis =soup.find('a', class_ = '-plxs _more').text.split(' ')[0].strip('(')
              Note = soup.find('div', class_ = 'stars _m _al').text.split(' ')[0]

              obj = {       'Marque': Marque,
                            # 'Details': Details,
                            'Ancien_Prix': int(Ancien_Prix),
                            'Prix': int(Prix),
                            # 'Reduction_Per': Reduction_Per,
                            'Nombre_Avis': int(Nombre_Avis), 
                            'Note': float(Note)
                            # 'Rate': Rate
                        }
              data.append(obj)
          except:
              pass
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis = 0)
    df.reset_index(drop = True, inplace = True)
    return df

def load_data_14(mul_page): 
    df = pd.DataFrame()
    for p in range(1, int(mul_page)):
        Url = f"https://www.jumia.sn/montres/?page={p}#catalog-listing"
        res = get(Url)
        soup = BeautifulSoup(res.text, 'html.parser')
        containers = soup.find_all('a', class_ ='core')
        links =  []
        link_jumia = 'https://www.jumia.sn'
        for container in containers:
          link_jumia1 = container['href']
          link = link_jumia + link_jumia1
          links.append(link)
        data = []
        for link in links:
          res = get(link)
          soup = BeautifulSoup(res.text, 'html.parser')
          try :
              Marque = soup.find_all('a', class_ ='_more')[1].text
              # Details = soup.find('h1', class_ = '-fs20 -pts -pbxs').text
              Ancien_Prix =soup.find('span', class_ = '-tal -gy5 -lthr -fs16 -pvxs').text.replace(' ', '').replace('FCFA', '')
              Prix = soup.find('span', class_ = '-b -ltr -tal -fs24 -prxs').text.replace(' ', '').replace('FCFA', '')
              # Reduction_Per = soup.find('span', class_ = 'bdg _dsct _dyn -mls').text.replace('%', '')
              Nombre_Avis =soup.find('a', class_ = '-plxs _more').text.split(' ')[0].strip('(')
              Note = soup.find('div', class_ = 'stars _m _al').text.split(' ')[0]

              obj = {       'Marque': Marque,
                            # 'Details': Details,
                            'Ancien_Prix': int(Ancien_Prix),
                            'Prix': int(Prix),
                            # 'Reduction_Per': Reduction_Per,
                            'Nombre_Avis': int(Nombre_Avis), 
                            'Note': float(Note)
                            # 'Rate': Rate
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
Data_1 = load_data_1(Pages3)
Data_2 = load_data_2(Pages4)
Data_3 = load_data_3(Pages5)
Data_4 = load_data_4(Pages6)
Data_5 = load_data_5(Pages7)
Data_6 = load_data_6(Pages8)
Data_7 = load_data_7(Pages9)
Data_8 = load_data_8(Pages10)
Data_9 = load_data_9(Pages11)
Data_10 = load_data_10(Pages12)
Data_11 = load_data_11(Pages13)
Data_12= load_data_12(Pages14)
Data_13 = load_data_13(Pages15)
Data_14 = load_data_14(Pages16)

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
load(Phone_data_mul_pag1, 'TV data', '2', '102')
load(Data_1, 'Educative Tablets data', '3', '103')
load(Data_2, 'House supplies data', '4', '104')
load(Data_3, 'Decorative furniture data ', '5', '105')
load(Data_4, 'Supplies data', '6', '106')
load(Data_5, 'House and desktop furnitures data', '7', '107')
load(Data_6, 'Bathroom tools data', '8', '108')
load(Data_7, 'Bed tools data', '9', '109')
load(Data_8, 'Ventilation and Heating tools data', '10', '110')
load(Data_9, 'House decaration tools data', '11', '111')
load(Data_10, 'Perfumes data', '12', '112')
load(Data_11, 'Health care tools data', '13', '113')
load(Data_12, 'Dental hygiene tools data', '14', '114')
load(Data_13, 'Parapharmacy tools data', '15', '115')
load(Data_14, 'watch data', '16', '116')
