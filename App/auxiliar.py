import pandas as pd
import streamlit as st
import requests
import joblib

# from sklearn.externals import joblib



def read_file(flile):
    df = pd.read_csv(flile, sep=";")
    return df


# @st.experimental_singleton()
@st.cache_data
def load_model():
    path = './models/RandomForest.pkl'
    try:
        url = 'https://github.com/j2sanabriam/Proyecto_Final_ML/blob/main/models/RandomForest.pkl'
        print("Downloading from GitHub")
        r = requests.get(url)

        with open(path, 'wb') as file:
            file.write(r.content)

        print("Downloaded from GitHub")
        return joblib.load(path)
    except:
        return joblib.load(path)

@st.cache_data
def load_pipeline():
    path = './models/pipeline.pkl'
    try:
        url = 'https://github.com/j2sanabriam/Proyecto_Final_ML/blob/main/models/pipeline.pkl'
        print("Downloading from GitHub")
        r = requests.get(url)

        with open(path, 'wb') as file:
            file.write(r.content)

        print("Downloaded from GitHub")
        return joblib.load(path)
    except:
        return joblib.load(path)