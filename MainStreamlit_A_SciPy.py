import streamlit as st
import pandas as pd
import pickle
from streamlit_option_menu import option_menu

# Load prediction models
with open("BestModel_CLF_RF_SciPy.pkl", "rb") as file:
    lr_model = pickle.load(file)

with open("BestModel_REG_Lasso_SciPy.pkl", "rb") as file:
    rf_model = pickle.load(file)

# Load dataset if needed
data = pd.read_csv("/mnt/data/Dataset UTS_Gasal 2425.csv")

# Sidebar menu
with st.sidebar:
    selected = option_menu('Streamlit UTS ML 24/25',
                           ['Klasifikasi',
                            'Regresi', 'Catatan'],
                            default_index=0)

# Klasifikasi Properti
if selected == 'Klasifikasi':
    st.title('Klasifikasi Properti')

    # Input features
    squaremeters = st.slider("Squaremeters", 0, 100000)
    numberofrooms = st.slider("Number of Rooms", 0, 100)
    hasyard = st.radio("Has Yard?", ["Yes", "No"])
    haspool = st.radio("Has Pool?", ["Yes", "No"])
    floors = st.number_input("Floors", 0)
    citycode = st.number_input("City Code", 0)
    citypartrange = st.number_input("City Part Range", 0)
    numprevowners = st.number_input("Number of Previous Owners", 0)
    made = st.number_input("Year Built", 0)
    isnewbuilt = st.radio("Is New Built?", ["New", "Old"])
    hasstormprotector = st.radio("Has Storm Protector?", ["Yes", "No"])
    basement = st.number_input("Basement Area", 0)
    attic = st.number_input("Attic Area", 0)
    garage = st.number_input("Garage Area", 0)
    hasstorageroom = st.radio("Has Storage Room?", ["Yes", "No"])
    hasguestroom = st.number_input("Number of Guest Rooms", 0)

    # Convert categorical features to binary
    data_input = pd.DataFrame([[squaremeters, numberofrooms, hasyard == "Yes", haspool == "Yes", floors,
                                citycode, citypartrange, numprevowners, made, isnewbuilt == "New",
                                hasstormprotector == "Yes", basement, attic, garage, 
                                hasstorageroom == "Yes", hasguestroom]],
                              columns=['squaremeters', 'numberofrooms', 'hasyard', 'haspool', 'floors',
                                       'citycode', 'citypartrange', 'numprevowners', 'made', 
                                       'isnewbuilt', 'hasstormprotector', 'basement', 'attic', 
                                       'garage', 'hasstorageroom', 'hasguestroom'])

    # Predict button
    if st.button("Prediksi Kategori"):
        kategori = rf_model.predict(data_input)[0]
        st.success(f"Kategori Properti: {kategori}")

# Regresi Harga Properti
if selected == 'Regresi':
    st.title('Regresi Harga Properti')

    # Reuse inputs for regression model
    squaremeters = st.slider("Squaremeters", 0, 100000)
    numberofrooms = st.slider("Number of Rooms", 0, 100)
    hasyard = st.radio("Has Yard?", ["Yes", "No"])
    haspool = st.radio("Has Pool?", ["Yes", "No"])
    floors = st.number_input("Floors", 0)
    citycode = st.number_input("City Code", 0)
    citypartrange = st.number_input("City Part Range", 0)
    numprevowners = st.number_input("Number of Previous Owners", 0)
    made = st.number_input("Year Built", 0)
    isnewbuilt = st.radio("Is New Built?", ["New", "Old"])
    hasstormprotector = st.radio("Has Storm Protector?", ["Yes", "No"])
    basement = st.number_input("Basement Area", 0)
    attic = st.number_input("Attic Area", 0)
    garage = st.number_input("Garage Area", 0)
    hasstorageroom = st.radio("Has Storage Room?", ["Yes", "No"])
    hasguestroom = st.number_input("Number of Guest Rooms", 0)

    # Convert categorical features to binary
    data_input = pd.DataFrame([[squaremeters, numberofrooms, hasyard == "Yes", haspool == "Yes", floors,
                                citycode, citypartrange, numprevowners, made, isnewbuilt == "New",
                                hasstormprotector == "Yes", basement, attic, garage, 
                                hasstorageroom == "Yes", hasguestroom]],
                              columns=['squaremeters', 'numberofrooms', 'hasyard', 'haspool', 'floors',
                                       'citycode', 'citypartrange', 'numprevowners', 'made', 
                                       'isnewbuilt', 'hasstormprotector', 'basement', 'attic', 
                                       'garage', 'hasstorageroom', 'hasguestroom'])

    # Predict button
    if st.button("Prediksi Harga"):
        harga = lr_model.predict(data_input)[0]
        st.success(f"Harga Properti: Rp {harga:,.0f}")

# Halaman Catatan
if selected == 'Catatan':
    st.title('Catatan')
    st.write('''
    1. Untuk memunculkan sidebar agar tidak error ketika di run, silahkan install library streamlit option menu di terminal dengan perintah "pip install streamlit-option-menu".
    2. Menu yang dibuat ada 2 yaitu Klasifikasi dan Regresi.
    3. Inputnya apa saja, sesuaikan dengan arsitektur code anda pada notebook.
    4. Referensi desain streamlit dapat di akses pada https://streamlit.io/
    5. Link streamlit design ini dapat di akses pada https://apputs-6qzfrvr4ufiyzhj84mrfkt7.streamlit.app/
    6. Library dan file requirements yang dibutuhkan untuk deploy online di github ada 5 yaitu streamlit, scikit-learn, pandas, numpy, streamlit-option-menu.
    ''')
