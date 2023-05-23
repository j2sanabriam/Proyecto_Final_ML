import streamlit as st
import auxiliar as aux
import joblib
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler, FunctionTransformer
from sklearn.compose import ColumnTransformer, make_column_selector
import numpy as np
from scipy.sparse import csr_matrix


data = pd.read_csv("./data/solicitudes_tc_dataset.csv", sep=";")
data2 = data.drop(['moroso'], axis=1)


def eliminar_columnas_no_utiles(X):
    columnas_no_utiles = ['contract_number','card_type','business_dni_type','city','mora_ultimos_6meses','created_at']
    return X.drop(columnas_no_utiles, axis=1)

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(),  make_column_selector(dtype_include=np.number)),
        ("cat", OneHotEncoder(), make_column_selector(dtype_include=object)),
    ]
)
pipeline = Pipeline(steps=[
    ('eliminar_columnas', FunctionTransformer(eliminar_columnas_no_utiles)),
    ('column_transformer',preprocessor)
])

pipeline.fit(data2)


cat_names = pipeline['column_transformer'].transformers_[1][1].get_feature_names_out()
num_names = pipeline['column_transformer'].transformers_[0][1].feature_names_in_
col_names = list(num_names) + list(cat_names)


def convertir(pipeline, X):
    df_1 = pd.DataFrame.sparse.from_spmatrix(pipeline.transform(X))
    df_1.columns = col_names
    return df_1


st.set_page_config(page_title="SEMPLI App", layout="wide")

st.image("./img/sempli.png")
st.write("Esta aplicación permite predecir si un cliente potencial de Sempli incorrirá en mora, para así apoyar la decisión de otorgarle un crédito o no. Puede realizar la predicción para uno o varios cliente potenciales cargando un archivo en formato CSV.")

if 'images' not in st.session_state:
    st.session_state['file'] = list()
    st.session_state['model'] = None

if not st.session_state['file']:
    st.session_state['model'] = aux.load_model()
    # st.session_state['pipeline'] = aux.load_pipeline()
    # pipe = aux.load_pipeline()

    uploaded_file = st.file_uploader("Carga un Archivo", type=['csv'], accept_multiple_files=False)
    if st.button("Realizar Predicción") and uploaded_file is not None:
        df = aux.read_file(uploaded_file)
        st.write(df)
        # placeholder = st.empty()

        st.write("Limpieza y Trasformación de Datos")
        result = pipeline.transform(df)
        datos = result.data
        indices = result.indices
        indptr = result.indptr

        csr_matrix_data = csr_matrix((datos, indices, indptr), shape=(1711, 106))
        df_p = pd.DataFrame(csr_matrix_data.toarray())
        df_p.columns = col_names

        st.write(df_p)

        st.write("Predicción")

        # Realizar predicciones en el conjunto de prueba con el mejor modelo
        y_pred = st.session_state['model'].predict(df_p.values)
        df['moroso'] = y_pred
        st.write(df)

        st.session_state['file'].append(df)

        # placeholder.empty()
        # st.experimental_rerun()

        if st.button("Descargar Predicción"):
            st.write("Archivo Descargando")

else:
    if st.button("Reiniciar"):
        st.session_state['file'] = list()
        st.experimental_rerun()
    # for path in st.session_state['images']:
    # image, y_pred = aux.predict(path)
    # st.image(image)
    # st.dataframe(y_pred)
    # st.bar_chart(y_pred.transpose())
