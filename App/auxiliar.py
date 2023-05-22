import pandas as pd
import streamlit as st
import requests


def read_file(flile):
    df = pd.read_csv(flile, sep=";")
    return df


@st.experimental_singleton()
def load_model():
    # path = 'data/flower_classification.h5'
    path = './models/sempli-v1.joblib'
    try:
        # url = 'https://machine-learning-services.s3.amazonaws.com/flower_classification/flower_classification.h5'
        url = 'https://github.com/j2sanabriam/Proyecto_Final_ML/blob/main/models/sempli-v1.joblib'
        print("Downloading from S3")
        r = requests.get(url)

        with open(path, 'wb') as file:
            file.write(r.content)

        print("Downloaded from S3")
        return keras.models.load_model(path)
    except:
        return keras.models.load_model(path)