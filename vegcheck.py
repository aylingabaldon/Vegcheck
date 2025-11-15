import streamlit as st

st.title("VegCheck 🌱💚")
st.header("¿Eres vegano y batallas para encontrar productos 100% aptos para ti?")
st.write("Entonces esta app es ideal para ti, aquí encontrarás información importante que te ayudará a elegir los productos que cumplan con tu estilo de vida") 
st.sidebar.write("**VEGCHECK:** Una app para tu nuevo estilo de vida")
st.sidebar.write("**Equipo:** ")
Nombres = ["Paola Conde", "Aylín Gabaldón", "José Luis Guevara", "Alan López", "Luis Yepiz"]
for Nombres in Nombres:
  st.sidebar.write(f"• {Nombres}")
st.sidebar.write("**Materia:** Programación")
st.sidebar.write("**Grupo:** 3L")
tabs = st.tabs(["Iniciación al veganismo", "Ingredientes no aptos ❌", "Ingredientes a revisar 🔎", "Productos 100% veganos ✅Ⓥ", "Recetas Veganas 🍽️"])

with tabs[0]:
  st.header("Iniciación al veganismo")
  st. write("A continuación se presenta información relevante que es fundamental que conozcas si deseas adentrarte en el mundo del veganismo y mejorar o cambiar tu estilo de vida")
  st.subheader("¿Qué es el veganismo?")
  st.write("El veganismo es una filosofía y un estilo de vida que busca excluir, en la medida de lo posible y practicable, toda forma de explotación y crueldad hacia los animales para la alimentación, la vestimenta o cualquier otro propósito; y, por extensión, promueve el desarrollo y el uso de alternativas libres de productos animales en beneficio de los animales, los seres humanos y el medio ambiente. En términos dietéticos, denota la práctica de prescindir de todos los productos derivados total o parcialmente de animales.")
  st.subheader("¿Qué tipo de alimentación se tiene al ser vegano?")
  st.write("Hay muchas maneras de adoptar un estilo de vida vegano. Sin embargo, algo que todos los veganos tienen en común es una dieta basada en plantas que evita todos los alimentos de origen animal, como la carne (incluidos el pescado, los mariscos y los insectos), los lácteos, los huevos y la miel ; además de evitar materiales derivados de animales, productos probados en animales y lugares que utilizan animales para el entretenimiento.")
  st.write("La dieta vegana es muy variada e incluye todo tipo de frutas, verduras, frutos secos, cereales, semillas, legumbres y frijoles, que se pueden preparar en infinitas combinaciones.")
  st.write("Una dieta vegana equilibrada se componede cuatro grupos de alimentos:")

  grupos = st.selectbox(
    "Grupos", 
    ["Legumbres", "Cereales", "Verduras", "Frutas", "Otros alimentos", "Vitamina B12"]
  if grupos == "Legumbres":
    st.write("**Legumbres, Frutos secos y Semillas (Más de 4 raciones al día):** Este grupo incluye frijoles, lentejas, guisantes, nueces, cacahuates, semillas de girasol, semillas de calabaza, productos de soya, entre otros. Todos estos alimentos son ricos en nutrientes coo proteínas, fibra, minerales, vitaminas del grupo B, antioidantes y ácidos grasos escenciales. Algunas de las porciones recomendadas son: 1/2tz Frijoles cocidos, 115gr Tofu, 1tz Leche de soya, 28gr de frutos secos o semillas, etc.")
  elif grupos == "Cereales":
    st.write("**Cereales o granos (De 4-6 porciones al día):** Dentro de este grupo encontramos el arroz, la avena, el trigo, la quinoa, cebada, sorgo, etc. Los cereales integrales aportan vitaminas del gruo B, fibra, inerales y antioxidantes, se recomienda evitar los refinados ya quedentro de et procedo se eliminan gran parte de los nutrientes benéficos para la salud. Una ración equivale a 1 rebanada de pan, 1/2tz de cualquier cereal cocido, 1pz Tortilla de maíz, 1/2tz Avena, 4pz Galletas saladas")
  elif grupos == "Verduras":
    st.write("**Verduras (4 o más raciones al día):** Consumir una variedad de vegetales con amplia diversidad de colores garantiza la ingesta de múltiples nutrientes protectores en la dieta (vitaminas y minerales), asi como fibra. Una porción equivale a 1/2tz de vegetales cocidos, 1tz vegetales crudos o 1(2tz de vegetales en jugo.")
  elif grupos == "Frutas":
    st.write("**Frutas (2 o más raciones):** La mayoría de las frutas, especialmente los cítricos, son una excelente fuente de vitamina C, las frutas además son fuente de antioxidantes. Para obtener el mayor beneficio de estas es preferible elegri la fruta entera en lugar de jugos. Una porción equivale a 1pz mediana, 1tz Fruta en rodajas, 1/4tz Fruta dehidratada, 1/2tz Fruta en jugo.")
  elif grupos == "Otros alimentos":
    st.write("**Otros alimentos:** Las grasas, como aceites y margarinas, deben de ser limitado su consumo y ser lo menos procesadas posibles. Las grasas esenciales para la alimentación provienen de alimentos como el aguacate, las aceitunas, los frutos secos y las semillas. Una porción recomendada en cuanto a los aceites es 1cdita al día.")
  elif grupos == "Vitamina B12":
    st.write("Vitamina B12: Esta vitamina es necesaria para la formación de globulos rojos, funciones neurológicas y la síntesis del ADN. Su prncipal fuente son los alimentos de origen animal como las carnes rojas, sin embargo se puede encontrar en ciertos tipos de vegetales pero los niveles de esta vitamina varían mucho por lo que no podemosdepender de los vegetales para cubrir las necesidades diarias, por lo que se recomienda recurrir al consumo de suplementos o alimentos fortificados con esta vitamina. Hay que tomar en cuenta que no todas las vitaminas B12 etiquetadas en el mercado son aptas para veganos por lo que hay que verificar el origen de estas.")
  
  st.write("**IMPORTANTE:** Dado que las necesidades nutricionales y energéticas individuales varían según la edad, el nivel de actividad y el estado de salud, esta guía debe considerarse únicamente como una introducción general a una dieta vegana equilibrada. Para obtener recomendaciones personalizadas, consulte con un dietista o nutriólogo especializado en nutrición vegana.")
  st.subheader("¿Cómo sustituyo los productos de origen animal?")
# st.write(AQUI ESCRIBIR LAS ALTERNATIVAS QUE SE TIENE DE LOS ALIMENTOS BÁSICOS DE ORIGEN ANIMAL A LOS DE ORIGEN VEGETAL)
  st.subheader("Beneficios del veganismo")
# "ESCRIBIR LAS PRINCIPALES VENTAJAS Y BENEFICIOS DEL VEGANISMO)
# beneficios = []
# for beneficios in beneficios:
# st.write(f"•{beneficios}")
  st.subheader("Mitos del veganismo")
# AQUÍ ESCRIBIR ALGUNOS DE LOS MITOS MÁS SONADOS Y LA RAZON POR LA QUE NO ES VERDAD)
#  mitos = []
#  for mitos in mitos:
#    st.write(f"•{mitos}") 
    
  st.subheader("Guías para iniciar en el veganismo")
  PDF_FILE_PATH = r"PETAspanishVSK.pdf"
  with open(PDF_FILE_PATH, "rb") as pdf_file:
    PDF_bytes = pdf_file.read()
    st.write("Kit vegano para principiantes")
    st.download_button(
      label="Descargar PDF",
      data=PDF_bytes,
      file_name="Kit_Vegano_Para_Principiantes.pdf",
      mime="application/pdf")

  PDF_FILE_PATH = r"GuíaDeIniciaciónAlVeganismo-Español-2.1.pdf"
  with open(PDF_FILE_PATH, "rb") as pdf_file:
    PDF_bytes = pdf_file.read()
    st.write("Guía de iniciación al veganismo")
    st.download_button(
      label="Descargar PDF",
      data=PDF_bytes,
      file_name="Guía_de_iniciación_al_veganismo.pdf",
      mime="application/pdf")

  PDF_FILE_PATH = r"Guia Vegetariana Para Principiantes_LA [EligeVeg].pdf"
  with open(PDF_FILE_PATH, "rb") as pdf_file:
    PDF_bytes = pdf_file.read()
    st.write("Guía vegetariana para principiantes")
    st.download_button(
      label="Descargar PDF",
      data=PDF_bytes,
      file_name="Guía_vegetariana_para_principiantes.pdf",
      mime="application/pdf")

  PDF_FILE_PATH = r"Good Nutrition - Vegan Starter Kit.pdf"
  with open(PDF_FILE_PATH, "rb") as pdf_file:
    PDF_bytes = pdf_file.read()
    st.write("Vegan Starter (Inglés)")
    st.download_button(
      label="Descargar PDF",
      data=PDF_bytes,
      file_name="Vegan_Starter.pdf",
      mime="application/pdf")

with tabs[1]:
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

with tabs[2]:
   st.header("Ingredientes a revisar 🔎")
   st.write("En esta sección encontrarás ingredientes que pueden ocasionar confusión entre si son de origen vegetal o de origen animal, con los cuáles se tendrá que investigar un poco más a fondo de que origen tienen antes de clasificar el producto como apto o no.")
   ingredientes =  ['**Glicerina o E422:** Puede ser vegetal extraída de aceites de coco, soya, maíz o palma, sin embargo también puede provenir de grasas animales por lo que se debe de buscar en la etiqueta que diga "glicerina vegetal."',
                    "**Mono y digliceridos o E471:** Son de origen mixto: Los de origen vegetal provienen de aceites de soya, girasol o palma y los de origen animal provienende las grasas o aceites animales. Normalmente en la etiqueta especifica si son de origen vegetal o animal.",
                    "**Estearato de magnesio o E572:** Esta sal del ácido esteárico, es un ácido graso saturado que puede ser derivado de fuentes animales como el cebo de res, o de fuentes vegetales como el aceite de coco o palma. Se debe buscar en la etiqueta si especifica que es de origen vegetal.", 
                    '**Lecitina o E5322:** Esta grasa natural se obtiene de la soya o girasol, sin embargo también puede provenir de fuentes animales como el huevo. Por lo tanto se debe buscar que en la etiqueta diga "Lecitina de soya" o "Lecitina de girasol".', 
                    "**Acido esteárico:** Es un ácido graso natural puede provenir de grasa animal o vegetal. Se debe verificar el origen de este o que el producto esté certificado como vegano.",
                    "**L cisteína o E910-E913:** Este es un aminoácido no esencial que frecuentemente se obtiene de fuentes animales, sin embargo se puede producir de forma sintética mediante la fermentación del almidón. Comprobar si el producto está certificado como vegano.",
                    "**Saborizante natural:** No necesariamnte es apto para veganos ya que puede contener compuestos de origen animal o derivar de estos y la etiqueta no siempre lo especifica, por lo que se debe de buscar si el producto cuenta con una certificación o sello vegano.", 
                    '**Vitamina D:** D3 puede derivar de lanolina (sustancia aceitosa que se obtiene de la lana de la oveja), sin embargo existen opciones veganas como la Vitamina D2 que se obtiene de hongos y levaduras, la Vitamina D3 si se obtiene del liquen (alga). Buscar en la etiqueta los términos "Vegano" o "De origen vegetal".', 
                    '**Carbon activado:** Usado en suplementos, colorantes o cosméticos, puede provenir de los huesos de la vaca o si es de origen vegetal se obtiene de materiales como la cáscara de coco, bambú o madera. Buscar la palabra "De origen animal" o "Vegano".', 
                   '**Inosinato disódico o E631:** Puede ser de carne o pescado o también se puede obtener por medio de fermentacion, sin embargo es muy importante confirmar con la certificación o un sello que diga "vegano" ya que la industria alimentaria puede obtener este aditivo de diferentes maneras.']
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
  st.header("Productos 100% veganos ✅Ⓥ")
  st.write("Aquí encontrarás una lista de productos que son completamente veganos, sin ingredientes de origen animal ni derivados. Estos productos son seguros para un estilo de vida 100% vegetal 🌿.")

  # Leche vegetal
  st.write("**Leches vegetales:** Bebidas de soya, almendra, avena, arroz, coco o nuez.")
  st.image("https://static.independent.co.uk/2024/04/12/13/Vegan-milks-hero.png?fit=crop&height=630&width=1200", caption="Leche vegetal – Silk / Alpro / Califia Farms")
  
  # Yogur vegetal
  st.write("**Yogur vegetal:** Hecho a base de soya, coco, avena o almendra.")
  st.image("https://makeitdairyfree.com/wp-content/uploads/2020/01/Vegan-Yogurt-Review-Dairy-free-yogurts-2-2.jpg", caption="Yogur vegetal – Silk / So Delicious / Alpro")
  
  # Queso vegano
  st.write("**Queso vegano:** Elaborado con frutos secos, tofu o aceites vegetales.")
  st.image("https://www.tastingtable.com/img/gallery/14-best-vegan-cheese-brands-ranked-worst-to-best/intro-1670870549.jpg", caption="Queso vegano – Violife / Daiya / Follow Your Heart")
 
  # Tofu
  st.write("**Tofu:** Fuente vegetal de proteína hecha a base de soya coagulada.")  
  st.image("https://bigmountainfoods.com/cdn/shop/files/smoked-tofu-mock-front-9.png?v=1754505176", caption="Tofu – Big Mountain / Mori-Nu / House Foods")
    
  # Tempeh
  st.write("**Tempeh:** Alimento fermentado a base de soya con alto contenido proteico.")
  st.image("https://itznot.com/cdn/shop/files/Tofu_combo.png?v=1749569629", caption="Tempeh – ItzNot / Lightlife / Tofurky")
  
  # Seitán
  st.write("**Seitán:** También llamado carne vegetal, está hecho de gluten de trigo.")
  st.image("https://uptonsnaturals.com/wp-content/uploads/2024/02/TraditionalSeitanCanada.png", caption="Seitán – Upton’s Naturals / The Plant-Based Butchers")

  # Hamburguesas vegetales
  st.write("**Hamburguesas vegetales:** Elaboradas con legumbres, granos y vegetales.")
  st.image("https://beyond-meat-cms-production.s3.us-west-2.amazonaws.com/42e87ac4-e865-40d8-bce9-a3870489460e.png", caption="Hamburguesa vegetal – Beyond Meat / Impossible / Gardein")
  
  # Mayonesa vegana
  st.write("**Mayonesa vegana:** Hecha sin huevo, con aceite vegetal y leche de soya o aquafaba.")
  st.image("https://hebmx.vtexassets.com/arquivos/ids/703414-800-800?v=638521750175800000&width=800&height=800&aspect=true", caption="Mayonesa vegana – Just Mayo / Hellmann’s Vegan")
  
  # Mantequilla vegana
  st.write("**Mantequilla vegana:** Elaborada con aceites vegetales o aguacate.")
  st.image("https://i5-mx.walmartimages.com/gr/images/product-images/img_large/00002740000024L.jpg?odnHeight=612&odnWidth=612&odnBg=FFFFFF&format=avif", caption="Mantequilla vegana – Country Crock Plant / Earth Balance")
  
  # Helado vegano
  st.write("**Helado vegano:** Hecho con base de leche vegetal y sin derivados animales.")
  st.image("https://sgfm.elcorteingles.es/SGFM/dctm/MEDIA03/202304/26/00118952006924____7__600x600.jpg", caption="Helado vegano – Ben & Jerry’s Non-Dairy / Halo Top Vegan / Oatly")
  
  # Chocolate negro
  st.write("**Chocolate negro (≥70% cacao):** Siempre que no contenga leche ni miel.")
  st.image("https://i5-mx.walmartimages.com/gr/images/product-images/img_large/00003746601763L.jpg?odnHeight=612&odnWidth=612&odnBg=FFFFFF", caption="Chocolate negro – Lindt 70% / Hu Chocolate / Alter Eco")
  
  # Pastas y panes 
  st.write("**Pastas y panes sin huevo ni leche:** Revisando las etiquetas, son opciones aptas.")
  st.image("https://2fa9243327.clvaw-cdnwnd.com/5cae5153195db7e844209308a86bfd40/200002966-a9601a9603/Barilla.jpg?ph=2fa9243327", caption="Pastas y panes sin huevo ni leche – Barilla / Rustichella / Pan artesanal vegano")
  
  # Snacks veganos
  st.write("**Snacks veganos:** Papas, palomitas, galletas y barras sin ingredientes animales.")
  st.image("https://www.costco.com.mx/medias/sys_master/products/hff/hc8/362138339442718.jpg", caption="Snacks veganos – Lays Original / Oreos / PopCorners")
  
  # Suplementos veganos
  st.write("**Suplementos veganos:** Proteínas de chícharo, arroz o soya, sin gelatina ni miel.")
  st.image("https://m.media-amazon.com/images/I/71Q-0sa8IML._AC_UF1000,1000_QL80_.jpg", caption="Suplementos veganos – Vega / Orgain / MyProtein Vegan")
  
  # Cosméticos veganos
  st.write("**Cosméticos cruelty-free:** Estos no fueron probados en animales y o contienen ingredientes derivados.")
  st.image("https://media.fashionnetwork.com/cdn-cgi/image/format=auto/m/1351/5c79/3361/d60c/9c91/b9c3/75a7/02aa/15f4/c7bc/c7bc.jpg", caption="Cosméticos veganos – e.l.f / Lush / The Body Shop")
  st.subheader("Lista completa de productos 🛒")
 # AGREGAR UNA LISTA DE PRODUCTOS JUNTO CON EL TIPO, MARCAS, SUPERMERCADOS Y LINKS
# for p in productos:
    #  st.write(f"➤ {p}") #Falta agregar la lista

with tabs[4]:
  st. header("Recetas Veganas 🍽️")
  st.write("Sabemos que a veces es dificil pensar en nuevas recetas o en otras opciones que se adapten a tu alimentación vegana, para ayudarte con eso te dejamos una variedad de link y documentos que te van a servir a variar tus comidas y tener más ideas desde desayunos, comidas, guarniciones y hasta postres.")
  st.subheader("Links útiles")
  st.write("Haz clic en los siguientes enlaces para visitar páginas de recetas.")
  st.markdown("[LoveVeg](https://loveveg.mx/recetas/)")
  st.markdown("[Nutritionfacts](https://nutritionfacts.org/es/recipes/)")
  st.markdown("[Veganoutreach](https://veganoutreach.org/recetas/)")
  st.markdown("[Veganuary](https://veganoutreach.org/recetas/)")
  st.markdown("[PCRM](https://www.pcrm.org/good-nutrition/plant-based-diets/recipes)")
  st.info("Los enlaces se abrirán en una nueva pestaña del navegador.")
# CLASIFICAR LOS LINKS Y AGREGAR LOS PDFs DE LAS RECETAS
  st.subheader("Recetarios descargables")
  st.write("A continuación hay una serie de documentos que puedes descargar con más deliciosas recetas para preparar.")
  PDF_FILE_PATH = r"30Recetas_-comprimido.pdf"
  with open(PDF_FILE_PATH, "rb") as pdf_file:
    PDF_bytes = pdf_file.read()
    st.write("**Vegaffinity** 🥘")
    st.write("En este recetario encontrarás gran variedad de recetas conocidas o comunes pero con su alternativa vegana.")
    st.download_button(
      label="Descargar PDF",
      data=PDF_bytes,
      file_name="Vegaffinity.pdf",
      mime="application/pdf")

  PDF_FILE_PATH = r"MisPrimerosTacosVeganos_LoveVegMéxico_2021.pdf"
  with open(PDF_FILE_PATH, "rb") as pdf_file:
    PDF_bytes = pdf_file.read()
    st.write("**Love Veg: Tacos Veganos**🌮")
    st.write("Como buen Mexicano los tacos no pueden faltar en la alimentación, este recetario está dedicado a como preparar diferentes tipos de tacos sin productos de origen animal.")
    st.download_button(
      label="Descargar PDF",
      data=PDF_bytes,
      file_name="TacosVeganos.pdf",
      mime="application/pdf")

  PDF_FILE_PATH = r"EnCasa_-ConLoveVeg_-Recetario.pdf"
  with open(PDF_FILE_PATH, "rb") as pdf_file:
    PDF_bytes = pdf_file.read()
    st.write("**Love Veg: Más recetas**🌯")
    st.write("Este recetario te da ideas desde desayunos, platos fuertes, postres y hasta bebidas.")
    st.download_button(
      label="Descargar PDF",
      data=PDF_bytes,
      file_name="RecetarioLoveveg.pdf",
      mime="application/pdf")

  PDF_FILE_PATH = r"Recetario_Patrio.pdf"
  with open(PDF_FILE_PATH, "rb") as pdf_file:
    PDF_bytes = pdf_file.read()
    st.write("**Love Veg: Recetas patrias**🌶️")
    st.write("En fechas patrias personaliza tu menú con recetas veganas con los sabores de estas festividades.")
    st.download_button(
      label="Descargar PDF",
      data=PDF_bytes,
      file_name="RecetasPatrias.pdf",
      mime="application/pdf")

  PDF_FILE_PATH = r"recetario_huevo.pdf"
  with open(PDF_FILE_PATH, "rb") as pdf_file:
    PDF_bytes = pdf_file.read()
    st.write("**Alternativas del huevo**🥚")
    st.write("Aquí te mostrarán diferentes recetas que utilizan huevo y de que manera se puede sustituir este producto para hacer una receta 100% vegana.")
    st.download_button(
      label="Descargar PDF",
      data=PDF_bytes,
      file_name="Recetasparasustituirelhuevo.pdf",
      mime="application/pdf")

  PDF_FILE_PATH = r"recetario_pollo.pdf"
  with open(PDF_FILE_PATH, "rb") as pdf_file:
    PDF_bytes = pdf_file.read()
    st.write("**Alternativas del pollo**🐤")
    st.write("¿Quieres hacer una receta pero lleva pollo en los ingredientes?, aquí te muestran diferentes alternativas para sustituirlo.")
    st.download_button(
      label="Descargar PDF",
      data=PDF_bytes,
      file_name="Recetasparasustituirelpollo.pdf",
      mime="application/pdf")


