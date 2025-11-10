import streamlit as st

st.title("VegCheck 🌱💚")
st.header("¿Eres vegano y batallas para encontrar productos 100% aptos para ti?")
st.write("Entonces esta app es ideal para ti, aquí encontrarás información importante que te ayudará a elegir los productos que cumplan con tu estilo de vida") 
st.sidebar.write("**Equipo:** ")
Nombres = ["Paola Conde", "Aylín Gabaldón", "José Luis Guevara", "Alan López", "Luis Yepiz"]
for Nombres in Nombres:
  st.sidebar.write(f"• {Nombres}")
st.sidebar.write("**Materia:** Programación")
st.sidebar.write("**Grupo:** 3L")
tabs = st.tabs(["Ingredientes no aptos ❌", "Ingredientes a revisar 🔎", "Productos 100% veganos ✅Ⓥ", "Recetas veganas 🍽️"])

with tabs[0]:
  st.header("Ingredientes no aptos ❌")
  st.write("Aquí encontrarás una lista de ingredientes presentes en los productos que son directamente de origen animal")

  Ingredientes = ["**Animales:** Vaca, cerdo, pescado, mariscos, cordero, caballo, pollo, gallina, cabra, conejo, pavo, pato, borrego, aves, insectos, entre otros.", "**Gelatina o E441:** Proveniente principalmente de proteína animal como piel o huesos.", "**Caseína:** Es la principal proteína de la leche.",
                  "**Caseínato:** Es derivado de la caseína y por lo tanto de la leche, usado como espesante.", "**Caseínato de sodio:** Es una sal sódica que se obtiene de la leche al precipitar las proteínas y neutralizarlas con hidróxico de sodio. Usado como espesante, aglutinante o fuente de proteínas.",
                 "**Suero de leche:** Es el líquido amarillento que queda después de que se coagula la leche. Usado principalmente en quesos y yogurt.", "**Lactosa:** Es el azúcar natural que se encuentra presente en la leche.", 
                 "**Miel:** Sustancia natural proveniente y producida por las abejas.", "**Propóleo:** Es una sustancia resinosa que fabrican las abejas a partir de los árboles, usado como conservante en los alimentos.", 
                 "**Jalea real:** Sustancia secretada por las abejas de color oscuro. Usado como complemento al aportar energía y nutrientes.", "**Carmín o E120:** Es un colorante rojo intenso extraído principalmente de la cochinilla", 
                 "**Isinglass:** Es una gelatina traslúcida hecha con las colas de pescado secas. Utilizado para la clarificación de cervezas y vinos.", "**Albúmina de huevo:** Es las proteína principal de la clara de huevo, utilizada como espumante o estabilizador.",
                 "**Albumen:** Es otro nombre con el cual se nombra a la clara del huevo.", "**Lactoalbúmina:** Es una proteína del suero de la leche. Utilizada en fórmulas infantiles para imitar la leche materna o en suplementos.", 
                 "**Shellac o E904:** Es un barniz de origen natural producido por el insecto de la laca. Utilizado para otorgar un glaseado, recubrimiento o brillo en los alimentos.", 
                 "**Cera de abejas o E901:** Sustancia natural producida por las abejas para construir sus colmenas, se utilizan como agente de recubrimiento en algunos alimentos.", "**Manteca de cerdo:** Es la grasa de cerdo derretida, utilizado como aceite para freír, guisar o preparar masas.",
                 "**Sebo:** Grasa sólida de los animales que se utiliza como grasa para cocinar, alimentos para mascotas e incluso en velas, jabones o lubricantes.", "**Lactitol o E966:** Es un polialcohol derivado de la lactosa, que se utiliza principalmente como edulcorante bajo en calorías.",
                 "**Lanolina o E913:** Es una sustancia cerosa y oleosa que se extrae de la lana de la obeja, utilizada en productos cosméticos y cuidados de la piel.", "**Fosfato de hueso comestible o E542:** Es un aditivo alimentario utilizado como antiaglomerante que proviene de huesos de animalescomo el vacuno o porcino. Tambien se puede encontrar en pastas de dientes o suplementos."]
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

with tabs[1]:
   st.header("Ingredientes a revisar 🔎")
   st.write("En esta sección encontrarás ingredientes que pueden ocasionar confusión entre si son de origen vegetal o de origen animal, con los cuáles se tendrá que investigar un poco más a fondo de que origen tienen antes de clasificar el producto como apto o no.")
   ingredientes =  ["**Glicerina o E422:** Puede ser vegetal o animal","**Glicerol o E422:** puede ser vegetal o animal", "**mono y digliceridos o E471:** de origen mixto", "**estereato de magnesio o E572:** puede ser vegetal o animal", "**Lecitina o E5322:** se obtiene de la soya/girasol o del huevo", 
                    "**Acido estearico:** puede provenir de grasa animal o vegetal", "**L cisteina o E910-E913:** Frecuentemente animal pero existe sintetica(vegana)", "**Saborizante natural:** Puede contener compuestos de origen animal. consultar con el fabricante", "**Vitamina d:** D3 puede derivar de lanolina o ser vegana(liquen); D2 es vegana", "**Carbon activado:** En algunos procesos(azùcar) puede usarse hueso; confirmar con el provedor", 
                   "**inosinato disodico o E631:** Puede ser de carne/pescado o fermentacion"]
   busqueda = st.text_input("Buscar el ingrediente ⌕")
   if busqueda:
     resultados = [p for p in ingredientes if busqueda.lower() in p.lower()]
     if resultados:
       st.write("Resultados: ")
       for r in resultados:
         st.write(f"- {r}")
     else: 
       st.write("No se encontro el ingrediente")
   st.subheader("Lista completa de los ingredientes 📝")
   for ingredientes in ingredientes:
     st.write(f"➤ {ingredientes}")

with tabs[3]:
  st. header("Recetas veganas 🍽️")
  st.subheader("Link utiles")
  st.write("Haz clic en los siguientes enlaces para visitar paginas de recetas")
  st.markdown("[LoveVeg](https://loveveg.mx/recetas/)")
  st.markdown("[Nutritionfacts](https://nutritionfacts.org/es/recipes/)")
  st.markdown("[Veganoutreach](https://veganoutreach.org/recetas/)")
  st.markdown("[Veganuary](https://veganoutreach.org/recetas/)")
  st.markdown("[PCRM](https://www.pcrm.org/good-nutrition/plant-based-diets/recipes)")
  st.info("Los enlaces se abriran en una nueva pestaña del navegador.")

