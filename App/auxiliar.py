import pandas as pd
import streamlit as st
import requests
import joblib
import pickle
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler, FunctionTransformer
from sklearn.compose import ColumnTransformer, make_column_selector
import numpy as np
from scipy.sparse import csr_matrix


def load_original_data():
    data = pd.read_csv("./data/solicitudes_tc_dataset.csv", sep=";")
    data2 = data.drop(['moroso'], axis=1)
    return data2


def read_file(file):
    df = pd.read_csv(file, sep=";")
    return df


# @st.experimental_singleton()
@st.cache_data
def load_model():
    path = './models/SVM.pkl'
    # modelo = pickle.load(path)
    with open(path, 'rb') as f:
        model = pickle.load(f)
    return model
    """
    try:
        
        url = 'https://github.com/j2sanabriam/Proyecto_Final_ML/blob/main/models/SVM.pkl'
        print("Downloading from GitHub")
        r = requests.get(url)

        with open(path, 'wb') as file:
            file.write(r.content)

        print("Downloaded from GitHub")
        
        return joblib.load(path)
    except:
        return joblib.load(path)
    """


@st.cache_data
def load_pipeline():
    """
    path = './models/pipeline_2.pkl'
    with open(path, 'rb') as f:
        pipe = pickle.load(f)
    return pipe
    """
    path = './models/pipeline.pkl'
    with open(path, 'rb') as f:
        pipe = joblib.load(f)
    return pipe

    """
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
    """




