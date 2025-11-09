import streamlit as st

base="light"
backgroundColor="#D4E5F4"
secondaryBackgroundColor="lavender"
codeBackgroundColor="powderBlue"
textColor="#00CC99"
font="Cooper Black"
[theme.sidebar]
backgroundColor="ghostWhite"
secondaryBackgroundColor="lavender"




st.title("VegCheck 🌱💚")
st.header("¿Eres vegano y batallas para encontrar alimentos 100% aptos para ti?")
st.write("Entonces esta app es ideal para ti, aquí encontrarás información importante que te ayudará a elegir los productos que cumplan con tu estilo de vida") 
st.sidebar.write("Equipo: ")
st.sidebar.write("Paola Conde")
st.sidebar.write("Aylín Gabaldón")
st.sidebar.write("José Luis Guevara")
st.sidebar.write("Alan López")
st.sidebar.write("Luis Yepiz")
st.sidebar.write("Materia: Programación")
st.sidebar.write("Grupo: 3L")
tabs = st.tabs(["Ingredientes no aptos ❌", "Ingredientes aptos ✅", "Ingredientes a revisar 🔎", "Productos 100% veganos Ⓥ", "Recetas veganas 🍽️"])
