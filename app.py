import streamlit as st
import pandas as pd

st.title("Завантаження CSV-файлу")

uploaded_file = st.file_uploader(label="Завантажте CSV-файл", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    sort_column = st.selectbox("Виберіть колонку для сортування", df.columns)

    if df[sort_column].dtype == 'O':
        sort_options = ["За алфавітом (А-Я; A-Z)", "За алфавітом (Я-А; Z-A)"]
    else:
        sort_options = ["За зростанням", "За спаданням"]

    sort_order = st.radio("Виберіть порядок сортування", sort_options)

    if sort_order in ["За алфавітом (А-Я; A-Z)", "За зростанням"]:
        ascending = True
    else:
        ascending = False

    df_sorted = df.sort_values(by=sort_column, ascending=ascending)
    st.dataframe(df_sorted)