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

with tabs[2]:
  st.header("Productos 100% veganos ✅Ⓥ")
  st.write("Aquí encontrarás una lista de productos que son completamente veganos, sin ingredientes de origen animal ni derivados. Estos productos son seguros para un estilo de vida 100% vegetal 🌿.")

  # Leche vegetal
  st.image("https://static.independent.co.uk/2024/04/12/13/Vegan-milks-hero.png?fit=crop&height=630&width=1200", caption="Leche vegetal – Silk / Alpro / Califia Farms")
  st.write("**Leches vegetales:** bebidas de soya, almendra, avena, arroz, coco o nuez.")

  # Yogur vegetal
  st.image("https://makeitdairyfree.com/wp-content/uploads/2020/01/Vegan-Yogurt-Review-Dairy-free-yogurts-2-2.jpg", caption="Yogur vegetal – Silk / So Delicious / Alpro")
  st.write("**Yogur vegetal:** hecho a base de soya, coco, avena o almendra.")

  # Queso vegano
  st.image("https://www.tastingtable.com/img/gallery/14-best-vegan-cheese-brands-ranked-worst-to-best/intro-1670870549.jpg", caption="Queso vegano – Violife / Daiya / Follow Your Heart")
  st.write("**Queso vegano:** elaborado con frutos secos, tofu o aceites vegetales.")

  # Tofu
  st.image("https://bigmountainfoods.com/cdn/shop/files/smoked-tofu-mock-front-9.png?v=1754505176", caption="Tofu – Big Mountain / Mori-Nu / House Foods")
  st.write("**Tofu:** fuente vegetal de proteína hecha a base de soya coagulada.")

  # Tempeh
  st.image("C:\Users\aylin gabaldon\Pictures\MultiPacks1_1_4a75599c-ca9a-4f01-8fff-92814b702d8a.jpg", caption="Tempeh – ItzNot / Lightlife / Tofurky")
  st.write("**Tempeh:** alimento fermentado a base de soya con alto contenido proteico.")

  # Seitán
  st.image("https://www.thefullhelping.com/wp-content/uploads/2021/01/How-to-Make-Seitan-5.jpg", caption="Seitán – Upton’s Naturals / The Plant-Based Butchers")
  st.write("**Seitán:** también llamado carne vegetal, hecho de gluten de trigo.")

  # Hamburguesas vegetales
  st.image("https://beyond-meat-cms-production.s3.us-west-2.amazonaws.com/42e87ac4-e865-40d8-bce9-a3870489460e.png", caption="Hamburguesa vegetal – Beyond Meat / Impossible / Gardein")
  st.write("**Hamburguesas vegetales:** elaboradas con legumbres, granos y vegetales.")

  # Mayonesa vegana
  st.image("https://cdn.shopify.com/s/files/1/0322/3554/2434/products/Just_Mayo_3_1200x1200.jpg?v=1606335821", caption="Mayonesa vegana – Just Mayo / Hellmann’s Vegan")
  st.write("**Mayonesa vegana:** hecha sin huevo, con aceite vegetal y leche de soya o aquafaba.")

  # Mantequilla vegana
  st.image("https://target.scene7.com/is/image/Target/GUEST_c26f35f8-48a7-426d-80f3-780b6a2423cf?wid=488&hei=488&fmt=pjpeg", caption="Mantequilla vegana – Country Crock Plant / Earth Balance")
  st.write("**Mantequilla vegana:** elaborada con aceites vegetales o aguacate.")

  # Helado vegano
  st.image("https://vegnews.com/media/W1siZiIsIjI0NDQ0L1ZlZ05ld3MtSWNlLUNyZWFtLmpwZyJdLFsicCIsInRodW1iIiwiMTIwMHg2NzVcdTAwM2UiXV0/VegNews-Ice-Cream.jpg?sha=ccdb43b0b7b77cfb", caption="Helado vegano – Ben & Jerry’s Non-Dairy / Halo Top Vegan / Oatly")
  st.write("**Helado vegano:** hecho con base de leche vegetal y sin derivados animales.")

  # Chocolate negro
  st.image("https://images.immediate.co.uk/production/volatile/sites/30/2021/08/Dark-chocolate-2f1cc4a.jpg?quality=90&resize=556,505", caption="Chocolate negro – Lindt 70% / Hu Chocolate / Alter Eco")
  st.write("**Chocolate negro (≥70% cacao):** siempre que no contenga leche ni miel.")

  # Pastas y panes
  st.image("https://static01.nyt.com/images/2020/02/26/dining/as-pasta3/merlin_169213001_3d093afc-2234-4ce9-bd3d-0b7c1d95f0df-superJumbo.jpg", caption="Pastas y panes sin huevo ni leche – Barilla / Rustichella / Pan artesanal vegano")
  st.write("**Pastas y panes sin huevo ni leche:** revisando etiquetas, son opciones aptas.")

  # Snacks veganos
  st.image("https://www.tasteofhome.com/wp-content/uploads/2023/03/TOH-Vegan-Snacks-List-Final-TOHcom23-e1692716214927.jpg?fit=700,700", caption="Snacks veganos – Lays Original / Oreos / PopCorners")
  st.write("**Snacks veganos:** papas, palomitas, galletas y barras sin ingredientes animales.")

  # Suplementos veganos
  st.image("https://cdn.shopify.com/s/files/1/0580/5462/2782/files/vegan-protein-powder-header_1024x1024.jpg?v=1660000320", caption="Suplementos veganos – Vega / Orgain / MyProtein Vegan")
  st.write("**Suplementos veganos:** proteínas de chícharo, arroz o soya, sin gelatina ni miel.")

  # Cosméticos veganos
  st.image("https://vegnews.com/media/W1siZiIsIjI0Njc5L1ZlZ05ld3MtVmVnYW4tQ29zbWV0aWNzLmpwZyJdLFsicCIsInRodW1iIiwiMTIwMHg3MTRcdTAwM2UiXV0/VegNews-Vegan-Cosmetics.jpg?sha=71a8a19dd2e70d53", caption="Cosméticos veganos – e.l.f / Lush / The Body Shop")
  st.write("**Cosméticos cruelty-free:** no probados en animales y sin ingredientes derivados.")
  st.subheader("Lista completa de productos 🛒")
  for p in productos:
      st.write(f"➤ {p}")

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

