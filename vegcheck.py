import streamlit as st

st.title("VegCheck 🌱💚")
st.header("¿Eres vegano y batallas para encontrar alimentos 100% aptos para ti?")
st.write("Entonces esta app es ideal para ti, aquí encontrarás información importante que te ayudará a elegir los productos que cumplan con tu estilo de vida") 
st.sidebar.write("Equipo: ")
Nombres = ["Paola Conde", "Aylín Gabaldón", "José Luis Guevara", "Alan López", "Luis Yepiz"]
for Nombres in Nombres:
  st.sidebar.write(f"• {Nombres}")
st.sidebar.write("Materia: Programación")
st.sidebar.write("Grupo: 3L")
tabs = st.tabs(["Ingredientes no aptos ❌", "Ingredientes aptos ✅", "Ingredientes a revisar 🔎", "Productos 100% veganos Ⓥ", "Recetas veganas 🍽️"])

with tabs[0]:
  st.header("Ingredientes no aptos ❌")
  st.write("Aquí encontrarás una lista de ingredientes presentes en los productos que son de origen animal")
  categoria = st.tabs(["Origen animal directo", "Colorantes o aditivos"])
with categoria[0]:
  st.header("Origen animal directo")
  Ingredientes = ["**Gelatina:** Proveniente principalmente de proteína animal como piel o huesos.", "**Caseína:** Es la principal proteína de la leche.",
                  "Caseínato: Es derivado de la caseína y por lo tanto de la leche, usado como espesante.", "Caseínato de sodio: Es una sal sódica que se obtiene de la leche al precipitar las proteínas y neutralizarlas con hidróxico de sodio. Usado como espesante, aglutinante o fuente de proteínas.",
                 "Suero de leche: Es el líquido amarillento que queda después de que se coagula la leche. Usado principalmente en quesos y yogurt.", "Lactosa: Es el azúcar natural que se encuentra presente en la leche.", 
                 "Miel: Sustancia natural proveniente y producida por las abejas.", "Propóleo: Es una sustancia resinosa que fabrican las abejas a partir de los árboles, usado como conservante en los alimentos.", 
                 "Jalea real: Sustancia secretada por las abejas de color oscuro. Usado como complemento al aportar energía y nutrientes."]
  buscar = st.text_input("Busca el ingrediente ⌕")
  if buscar:
    resultado = [p for p in Ingredientes if buscar.lower() in p.lower()]
    if resultado:
      st.write("Resultados: ")
      for r in resultado:
        st.write(f"- {r}")
    else:
      st.write("No se encontró el ingrediente")
  st.subheader("Lista completa de los ingredientes 📝")
  for Ingredientes in Ingredientes:
    st.write(f"➤ {Ingredientes}")
                          
  
