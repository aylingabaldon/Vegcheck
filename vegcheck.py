import streamlit as st

st.title("VegCheck 🌱💚")
st.header("¿Eres vegano y batallas para encontrar alimentos 100% aptos para ti?")
st.write("Entonces esta app es ideal para ti, aquí encontrarás información importante que te ayudará a elegir los productos que cumplan con tu estilo de vida") 
st.sidebar.write("**Equipo:** ")
Nombres = ["Paola Conde", "Aylín Gabaldón", "José Luis Guevara", "Alan López", "Luis Yepiz"]
for Nombres in Nombres:
  st.sidebar.write(f"• {Nombres}")
st.sidebar.write("**Materia:** Programación")
st.sidebar.write("**Grupo:** 3L")
tabs = st.tabs(["Ingredientes no aptos ❌", "Ingredientes aptos ✅", "Ingredientes a revisar 🔎", "Productos 100% veganos Ⓥ", "Recetas veganas 🍽️"])

with tabs[0]:
  st.header("Ingredientes no aptos ❌")
  st.write("Aquí encontrarás una lista de ingredientes presentes en los productos que son de origen animal")
  categoria = st.tabs(["Origen animal directo", "Colorantes o aditivos"])
with categoria[0]:
  st.header("Origen animal directo")
  Ingredientes = ["**Animales:** Vaca, cerdo, pescado, mariscos, cordero, caballo, pollo, gallina, cabra, conejo, pavo, pato, borrego, aves, insectos, entre otros.", "**Gelatina:** Proveniente principalmente de proteína animal como piel o huesos.", "**Caseína:** Es la principal proteína de la leche.",
                  "**Caseínato:** Es derivado de la caseína y por lo tanto de la leche, usado como espesante.", "**Caseínato de sodio:** Es una sal sódica que se obtiene de la leche al precipitar las proteínas y neutralizarlas con hidróxico de sodio. Usado como espesante, aglutinante o fuente de proteínas.",
                 "**Suero de leche:** Es el líquido amarillento que queda después de que se coagula la leche. Usado principalmente en quesos y yogurt.", "**Lactosa:** Es el azúcar natural que se encuentra presente en la leche.", 
                 "**Miel:** Sustancia natural proveniente y producida por las abejas.", "**Propóleo:** Es una sustancia resinosa que fabrican las abejas a partir de los árboles, usado como conservante en los alimentos.", 
                 "**Jalea real:** Sustancia secretada por las abejas de color oscuro. Usado como complemento al aportar energía y nutrientes.", "**Carmín:** Es un colorante rojo intenso extraído principalmente de la cochinilla", 
                 "**Isinglass:** Es una gelatina traslúcida hecha con las colas de pescado secas. Utilizado para la clarificación de cervezas y vinos.", "**Albúmina de huevo:** Es las proteína principal de la clara de huevo, utilizada como espumante o estabilizador.",
                 "**Albumen:** Es otro nombre con el cual se nombra a la clara del huevo.", "**Lactoalbúmina:** Es una proteína del suero de la leche. Utilizada en fórmulas infantiles para imitar la leche materna o en suplementos.", 
                 "**Shellac o E904:** Es un barniz de origen natural producido por el insecto de la laca. Utilizado para otorgar un glaseado, recubrimiento o brillo en los alimentos.", 
                 "**Cera de abejas o E901:** Sustancia natural producida por las abejas para construir sus colmenas, se utilizan como agente de recubrimiento en algunos alimentos.", "**Manteca de cerdo:** Es la grasa de cerdo derretida, utilizado como aceite para freír, guisar o preparar masas.",
                 "**Sebo:** Grasa sólida de los animales que se utiliza como grasa para cocinar, alimentos para mascotas e incluso en velas, jabones o lubricantes.", "**Lactitol o E966:** Es un polialcohol derivado de la lactosa, que se utiliza principalmente como edulcorante bajo en calorías.",
                 "**Lanolina:** Es una sustancia cerosa y oleosa que se extrae de la lana de la obeja, utilizada en productos cosméticos y cuidados de la piel."]
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
                          
  
