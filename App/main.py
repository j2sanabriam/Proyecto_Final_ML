import streamlit as st
import auxiliar as aux

st.set_page_config(page_title="SEMPLI App", layout="wide")

st.image("./img/sempli.jpg")
st.write("Esta aplicación permite predecir si un cliente potencial de Sempli incorrirá en mora, para así apoyar la decisión de otorgarle un crédito o no. Puede realizar la predicción para uno o varios cliente potenciales cargando un archivo en formato CSV.")

if 'images' not in st.session_state:
    st.session_state['file'] = list()
    st.session_state['model'] = None

if not st.session_state['file']:
    st.session_state['model'] = aux.load_model()
    # st.session_state['pipeline'] = aux.load_pipeline()

    uploaded_file = st.file_uploader("Carga un Archivo", type=['csv'], accept_multiple_files=False)
    if st.button("Realizar Predicción") and uploaded_file is not None:
        df = aux.read_file(uploaded_file)
        st.write(df)
        # placeholder = st.empty()
        st.session_state['file'].append(df)

        # placeholder.empty()
        # st.experimental_rerun()

        if st.button("Descargar"):
            st.write("Descargando")

else:
    if st.button("Reiniciar"):
        st.session_state['file'] = list()
        st.experimental_rerun()
    # for path in st.session_state['images']:
    # image, y_pred = aux.predict(path)
    # st.image(image)
    # st.dataframe(y_pred)
    # st.bar_chart(y_pred.transpose())
