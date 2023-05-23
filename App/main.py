import streamlit as st
import auxiliar as aux



st.set_page_config(page_title="SEMPLI App", layout="wide")
image_url = 'https://github.com/j2sanabriam/Proyecto_Final_ML/blob/main/App/img/sempli.png?raw=true'
st.image(image_url)
# st.image("img/sempli.png")
# st.title("Sempli App")
st.write("Esta aplicación permite predecir si un cliente potencial de Sempli incorrirá en mora, para así apoyar la decisión de otorgarle un crédito o no. Puede realizar la predicción para uno o varios cliente potenciales cargando un archivo en formato CSV.")

if 'file' not in st.session_state:
    st.session_state['file'] = list()
    st.session_state['model'] = None

if not st.session_state['file']:
    st.session_state['model'] = aux.load_model()

    uploaded_file = st.file_uploader("Carga un Archivo", type=['csv'], accept_multiple_files=False)
    if st.button("Realizar Predicción") and uploaded_file is not None:

        st.subheader("Datos Cargados")
        df = aux.read_file(uploaded_file)
        st.write(df)
        st.session_state['file'].append(df)

        st.subheader("Datos Luego de Limpieza y Trasformación")
        df_p = aux.transform(df)
        st.write(df_p)

        st.subheader("Datos con Predicción")
        y_pred = st.session_state['model'].predict(df_p.values)
        df['prediccion_incurrira_mora'] = y_pred
        df['prediccion_incurrira_mora'] = df['prediccion_incurrira_mora'].replace([0, 1], ['No', 'Si'])
        st.write(df)

        csv = df.to_csv(index=False, sep=";").encode('utf-8')
        filename = uploaded_file.name.split('.')[0] + "_predict.csv"
        if st.download_button(
            "Descargar Predicción",
            csv,
            filename,
            "text/csv",
            key='download-csv'
        ):
            st.write("Archivo Descargando")

else:
    if st.button("Reiniciar"):
        st.session_state['file'] = list()
        st.experimental_rerun()