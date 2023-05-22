import streamlit as st
import auxiliar as aux

st.set_page_config(page_title="SEMPLI App", layout="wide")

st.image("./img/sempli.jpg")
st.write("Esta aplicación permite predecir si un cliente potencial de Semplí incorrirá en mora, para así tomar la decisión de otorgarle un crédito o no. Puede realizar la predicción para uno o varios cliente potenciales cargando un archivo en formato CSV.")

if 'images' not in st.session_state:
    st.session_state['file'] = list()
    st.session_state['model'] = None

if not st.session_state['file']:
    # st.session_state['model'] = aux.load_model()

    uploaded_file = st.file_uploader("Carga un Archivo", type=['csv'], accept_multiple_files=False)
    if st.button("Cargar datos") and uploaded_file is not None:
        df = aux.read_file(uploaded_file)
        st.write(df)
    """
    upload_file = st.file_uploader("Carga un Archivo", type=['csv'], accept_multiple_files=False)
    if st.button("Realizar Predicción"):
        placeholder = st.empty()
        with placeholder.container():
            st.write("Leyendo datos")
            my_bar = st.progress(0)
            for i, uploaded_file in enumerate(upload_file):
                # To read file as bytes:
                bytes_data = uploaded_file.getvalue()
                name = uploaded_file.name
                # st.session_state['images'].append(aux.decode_image(bytes_data, name))
                percent_complete = (i + 1) / len(upload_file)
                my_bar.progress(percent_complete)

        placeholder.empty()
        st.experimental_rerun()
    """
else:
    if st.button("Reiniciar"):
        st.session_state['file'] = list()
        st.experimental_rerun()
    # for path in st.session_state['images']:
    # image, y_pred = aux.predict(path)
    # st.image(image)
    # st.dataframe(y_pred)
    # st.bar_chart(y_pred.transpose())
