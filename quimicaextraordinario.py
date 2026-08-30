import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Dashboard de Examen", page_icon="📝", layout="centered")

# ==========================================
# 1. BASE DE DATOS DEL EXAMEN (45 PREGUNTAS)
# ==========================================
examen_quimica = [
    {
        "id": 1,
        "pregunta": "_______________: Ciencia que se encarga del estudio de la materia, sus propiedades, estructura, composición y las transformaciones que experimenta.",
        "opciones": ["a) Física", "b) Química", "c) Biología"],
        "correcta": "b) Química"
    },
    {
        "id": 2,
        "pregunta": "“La combustión de una tira de magnesio produce una luz blanca brillante y origina cenizas de óxido de magnesio.” La afirmación anterior hace referencia a un:",
        "opciones": ["a) Fenómeno físico", "b) Fenómeno químico", "c) Proceso biológico"],
        "correcta": "b) Fenómeno químico"
    },
    {
        "id": 3,
        "pregunta": "Relaciona correctamente cada término con su definición correspondiente:\n\n| Concepto | Definición |\n| :--- | :--- |\n| 1. Masa | a) Relación entre la masa de una sustancia y el volumen que ocupa. |\n| 2. Peso | b) Espacio tridimensional ocupado por un cuerpo. |\n| 3. Volumen | c) Cantidad de materia presente en un cuerpo. |\n| 4. Densidad | d) Fuerza de atracción gravitacional ejercida sobre una masa. |",
        "opciones": ["a) 1c, 2d, 3b, 4a", "b) 1a, 2b, 3c, 4d", "c) 1c, 2a, 3b, 4d"],
        "correcta": "a) 1c, 2d, 3b, 4a"
    },
    {
        "id": 4,
        "pregunta": "El cambio de estado de agregación de la materia de fase gaseosa a fase líquida se conoce como:",
        "opciones": ["a) Sublimación", "b) Evaporación", "c) Condensación"],
        "correcta": "c) Condensación"
    },
    {
        "id": 5,
        "pregunta": "¿Cuál de los siguientes grupos contiene únicamente elementos o compuestos?",
        "opciones": ["a) Aire, vinagre, agua de mar", "b) Cobre (Cu), Cloruro de Sodio (NaCl), Oxígeno (O2)", "c) Latón, petróleo, acero"],
        "correcta": "b) Cobre (Cu), Cloruro de Sodio (NaCl), Oxígeno (O2)"
    },
    {
        "id": 6,
        "pregunta": "¿Quién propuso la Ley de Conservación de la Materia, afirmando que la materia no se crea ni se destruye, solo se transforma?",
        "opciones": ["a) John Dalton", "b) Antoine Lavoisier", "c) Dmitri Mendeleiev"],
        "correcta": "b) Antoine Lavoisier"
    },
    {
        "id": 7,
        "pregunta": "Químico que propuso la \"Ley de las Octavas\" para clasificar los elementos químicos en orden creciente de sus masas atómicas:",
        "opciones": ["a) Johann Wolfgang Döbereiner", "b) John Newlands", "c) Dmitri Mendeleiev"],
        "correcta": "b) John Newlands"
    },
    {
        "id": 8,
        "pregunta": "Los elementos que pertenecen a la familia o grupo IIA de la tabla periódica son conocidos como:",
        "opciones": ["a) Metales alcalinos", "b) Metales alcalinotérreos", "c) Halógenos"],
        "correcta": "b) Metales alcalinotérreos"
    },
    {
        "id": 9,
        "pregunta": "El bloque \"d\" de la tabla periódica está constituido principalmente por los elementos conocidos como:",
        "opciones": ["a) Elementos representativos", "b) Metales de transición", "c) Tierras raras (Lantánidos y Actínidos)"],
        "correcta": "b) Metales de transición"
    },
    {
        "id": 10,
        "pregunta": "Es la distancia promedio que existe entre el núcleo atómico y el electrón más externo de la capa de valencia:",
        "opciones": ["a) Radio atómico", "b) Afinidad electrónica", "c) Electronegatividad"],
        "correcta": "a) Radio atómico"
    },
    {
        "id": 11,
        "pregunta": "La energía mínima necesaria para remover un electrón de un átomo neutro en estado gaseoso se denomina:",
        "opciones": ["a) Radio iónico", "b) Energía o potencial de ionización", "c) Afinidad electrónica"],
        "correcta": "b) Energía o potencial de ionización"
    },
    {
        "id": 12,
        "pregunta": "Es la capacidad relativa que tiene un átomo en una molécula para atraer hacia sí los electrones de un enlace químico:",
        "opciones": ["a) Electronegatividad", "b) Afinidad electrónica", "c) Valencia"],
        "correcta": "a) Electronegatividad"
    },
    {
        "id": 13,
        "pregunta": "Científico que propuso el modelo atómico conocido como \"pudín de pasas\", sugiriendo que el átomo era una esfera de carga positiva con electrones incrustados:",
        "opciones": ["a) Ernest Rutherford", "b) Joseph John Thomson", "c) Niels Bohr"],
        "correcta": "b) Joseph John Thomson"
    },
    {
        "id": 14,
        "pregunta": "Mediante el experimento de la lámina de oro, este científico demostró la existencia de un núcleo atómico pequeño, denso y con carga positiva:",
        "opciones": ["a) John Dalton", "b) Ernest Rutherford", "c) Niels Bohr"],
        "correcta": "b) Ernest Rutherford"
    },
    {
        "id": 15,
        "pregunta": "Un átomo neutro posee un número atómico Z = 19 y una masa atómica A = 39 UMA. Determina el número de protones, electrones y neutrones presentes:",
        "opciones": ["a) p+=19, e-=19, n=20", "b) p+=20, e-=19, n=19", "c) p+=19, e-=20, n=20"],
        "correcta": "a) p+=19, e-=19, n=20"
    },
    {
        "id": 16,
        "pregunta": "Si un elemento neutro tiene un Z = 26 y A = 56 UMA, ¿cuántos neutrones tiene en su núcleo?",
        "opciones": ["a) 26", "b) 30", "c) 56"],
        "correcta": "b) 30"
    },
    {
        "id": 17,
        "pregunta": "¿Cuál es la configuración electrónica completa del átomo de Fósforo (Z = 15)?",
        "opciones": ["a) 1s22s22p63s23p3", "b) 1s22s22p63s23p5", "c) 1s22s22p63s13p4"],
        "correcta": "a) 1s22s22p63s23p3"
    },
    {
        "id": 18,
        "pregunta": "Un elemento cuya configuración electrónica finaliza en 1s22s22p63s23p64s2 pertenece al:",
        "opciones": ["a) Periodo 4, Grupo IIA", "b) Periodo 3, Grupo IVA", "c) Periodo 4, Grupo IA"],
        "correcta": "a) Periodo 4, Grupo IIA"
    },
    {
        "id": 19,
        "pregunta": "¿Cuál es el número atómico (Z) y el grupo de un elemento con configuración electrónica 1s22s22p63s23p4?",
        "opciones": ["a) Z = 16, Grupo VIA", "b) Z = 14, Grupo IVA", "c) Z = 16, Grupo IVA"],
        "correcta": "a) Z = 16, Grupo VIA"
    },
    {
        "id": 20,
        "pregunta": "¿Qué valores corresponden a los números cuánticos (n,l,m,s) del electrón diferenciador para el subnivel 3p4?",
        "opciones": ["a) n=3, l=1, m=-1, s=-1/2", "b) n=3, l=2, m=0, s=+1/2", "c) n=3, l=1, m=+1, s=-1/2"],
        "correcta": "a) n=3, l=1, m=-1, s=-1/2"
    },
    {
        "id": 21,
        "pregunta": "¿Cuáles son los números cuánticos del electrón cuyo orbital termina en 4d2?",
        "opciones": ["a) n=4, l=2, m=-1, s=+1/2", "b) n=4, l=1, m=-1, s=-1/2", "c) n=4, l=2, m=0, s=+1/2"],
        "correcta": "a) n=4, l=2, m=-1, s=+1/2"
    },
    {
        "id": 22,
        "pregunta": "Representación que utiliza puntos o cruces alrededor del símbolo del elemento para indicar sus electrones de la capa de valencia:",
        "opciones": ["a) Diagrama de Hund", "b) Estructura de Lewis", "c) Modelo de Bohr"],
        "correcta": "b) Estructura de Lewis"
    },
    {
        "id": 23,
        "pregunta": "Selecciona la molécula que corresponde a una estructura con un átomo central de Carbono unido a dos átomos de Oxígeno mediante dobles enlaces (O=C=O):",
        "opciones": ["a) CO", "b) CO2", "c) CO32-"],
        "correcta": "b) CO2"
    },
    {
        "id": 24,
        "pregunta": "Relaciona el tipo de enlace químico con sus características o ejemplo representativo:\n\n| Tipo de Enlace | Característica / Ejemplo |\n| :--- | :--- |\n| 1. Iónico | a) Compartición desigual de electrones entre no metales diferentes (HCl). |\n| 2. Covalente polar | b) Unión entre átomos metálicos mediante un 'mar de electrones'. |\n| 3. Covalente no polar | c) Transferencia de electrones entre metal y no metal (NaCl). |\n| 4. Metálico | d) Compartición equitativa de electrones entre no metales iguales (O2). |",
        "opciones": ["a) 1c, 2a, 3d, 4b", "b) 1a, 2c, 3b, 4d", "c) 1c, 2d, 3a, 4b"],
        "correcta": "a) 1c, 2a, 3d, 4b"
    },
    {
        "id": 25,
        "pregunta": "El enlace presente en la molécula de N2 (Nitrógeno gaseoso), donde dos átomos de nitrógeno comparten tres pares de electrones, es un enlace:",
        "opciones": ["a) Covalente polar triple", "b) Covalente no polar triple", "c) Iónico"],
        "correcta": "b) Covalente no polar triple"
    },
    {
        "id": 26,
        "pregunta": "Observa la siguiente ecuación química:\n\n2Al(s) + 6HCl(aq) → 2AlCl3(aq) + 3H2(g)↑\n\nIdentifica correctamente las partes señaladas:",
        "opciones": [
            "a) Reactivos: 2Al+6HCl; Productos: 2AlCl3+3H2; aq: Acuoso; ↑: Desprendimiento de gas", 
            "b) Reactivos: 2AlCl3+3H2; Productos: 2Al+6HCl; aq: Sólido; ↑: Precipitado"
        ],
        "correcta": "a) Reactivos: 2Al+6HCl; Productos: 2AlCl3+3H2; aq: Acuoso; ↑: Desprendimiento de gas"
    },
    {
        "id": 27,
        "pregunta": "¿Cuál de las siguientes reacciones representa una reacción de síntesis o combinación?",
        "opciones": ["a) 2KClO3→2KCl+3O2", "b) N2+3H2→2NH3", "c) Zn+2HCl→ZnCl2+H2"],
        "correcta": "b) N2+3H2→2NH3"
    },
    {
        "id": 28,
        "pregunta": "La reacción 2H2O2→2H2O+O2 se clasifica como una reacción de:",
        "opciones": ["a) Síntesis", "b) Descomposición", "c) Sustitución simple"],
        "correcta": "b) Descomposición"
    },
    {
        "id": 29,
        "pregunta": "La reacción Cu+2AgNO3→Cu(NO3)2+2Ag es un ejemplo de:",
        "opciones": ["a) Descomposición", "b) Sustitución simple (desplazamiento)", "c) Doble sustitución"],
        "correcta": "b) Sustitución simple (desplazamiento)"
    },
    {
        "id": 30,
        "pregunta": "Relaciona la ecuación química general con el tipo de reacción:\n\n| Tipo de Reacción | Ecuación General |\n| :--- | :--- |\n| 1. Síntesis | a) AB+CD→AD+CB |\n| 2. Descomposición | b) A+B→AB |\n| 3. Sustitución Simple | c) AB→A+B |\n| 4. Doble Sustitución | d) A+BC→AC+B |",
        "opciones": ["a) 1b, 2c, 3d, 4a", "b) 1b, 2a, 3d, 4c", "c) 1c, 2b, 3a, 4d"],
        "correcta": "a) 1b, 2c, 3d, 4a"
    },
    {
        "id": 31,
        "pregunta": "La reacción de combustión completa de un hidrocarburo produce como productos principales:",
        "opciones": ["a) Monóxido de carbono y agua", "b) Dióxido de carbono, agua y energía", "c) Carbono elemental e hidrógeno"],
        "correcta": "b) Dióxido de carbono, agua y energía"
    },
    {
        "id": 32,
        "pregunta": "Una sustancia anfótera es aquella que:",
        "opciones": ["a) Solamente puede donar protones en solución.", "b) Puede actuar como ácido o como base según el medio.", "c) No se disocia en presencia de agua."],
        "correcta": "b) Puede actuar como ácido o como base según el medio."
    },
    {
        "id": 33,
        "pregunta": "Según la teoría de Arrhenius, un ácido es una sustancia que en solución acuosa disocia e incrementa la concentración de:",
        "opciones": ["a) Iones oxhidrilo (OH-)", "b) Iones hidrógeno / hidronio (H+)", "c) Electrones libres"],
        "correcta": "b) Iones hidrógeno / hidronio (H+)"
    },
    {
        "id": 34,
        "pregunta": "De acuerdo con la teoría de Brønsted-Lowry, una base es toda especie química capaz de:",
        "opciones": ["a) Aceptar un protón (H+)", "b) Donar un protón (H+)", "c) Aceptar un par de electrones"],
        "correcta": "a) Aceptar un protón (H+)"
    },
    {
        "id": 35,
        "pregunta": "Los productos formados en una reacción de neutralización entre un ácido fuerte y una base fuerte son:",
        "opciones": ["a) Gas y óxido", "b) Sal y agua", "c) Ácido débil y base débil"],
        "correcta": "b) Sal y agua"
    },
    {
        "id": 36,
        "pregunta": "Calcula el pH de una solución de ácido clorhídrico (HCl) con una concentración 0.001 M:",
        "opciones": ["a) pH=1", "b) pH=3", "c) pH=11"],
        "correcta": "b) pH=3"
    },
    {
        "id": 37,
        "pregunta": "Determina la concentración molar de iones OH- en una solución cuyo pOH es igual a 4:",
        "opciones": ["a) 1.0×10-4 M", "b) 1.0×10-10 M", "c) 4.0 M"],
        "correcta": "a) 1.0×10-4 M"
    },
    {
        "id": 38,
        "pregunta": "Si una solución acuosa de NaOH tiene un pH=12, ¿cuál es su concentración de OH- y su pOH?",
        "opciones": ["a) pOH=2, OH-=0.01 M", "b) pOH=12, OH-=1×10-12 M", "c) pOH=2, OH-=0.1 M"],
        "correcta": "a) pOH=2, OH-=0.01 M"
    },
    {
        "id": 39,
        "pregunta": "Relaciona la fórmula química con el nombre correcto del compuesto:\n\n| Compuesto | Nombre |\n| :--- | :--- |\n| 1. KMnO4 | a) Óxido de cobre (I) |\n| 2. Fe2O3 | b) Permanganato de potasio |\n| 3. Cu2O | c) Óxido de hierro (III) |",
        "opciones": ["a) 1b, 2c, 3a", "b) 1a, 2b, 3c", "c) 1b, 2a, 3c"],
        "correcta": "a) 1b, 2c, 3a"
    },
    {
        "id": 40,
        "pregunta": "Selecciona la fórmula química correspondiente al Sulfato de Calcio:",
        "opciones": ["a) CaSO3", "b) CaSO4", "c) CaS"],
        "correcta": "b) CaSO4"
    },
    {
        "id": 41,
        "pregunta": "¿Cuál es el nombre correcto del compuesto con fórmula HNO3?",
        "opciones": ["a) Ácido nitroso", "b) Ácido nítrico", "c) Nitrato de hidrógeno"],
        "correcta": "b) Ácido nítrico"
    },
    {
        "id": 42,
        "pregunta": "Balancea por el método de tanteo la siguiente ecuación química e indica los coeficientes correctos:\n___Fe + ___O2 → ___Fe2O3",
        "opciones": ["a) 2,3,1", "b) 4,3,2", "c) 2,1,2"],
        "correcta": "b) 4,3,2"
    },
    {
        "id": 43,
        "pregunta": "Balancea por el método de tanteo la siguiente ecuación:\n___C3H8 + ___O2 → ___CO2 + ___H2O",
        "opciones": ["a) 1,5,3,4", "b) 1,3,3,4", "c) 2,5,6,8"],
        "correcta": "a) 1,5,3,4"
    },
    {
        "id": 44,
        "pregunta": "En una reacción de óxido-reducción (redox), el agente reductor es la especie química que:",
        "opciones": ["a) Gana electrones y se reduce.", "b) Pierde electrones y se oxida.", "c) Mantiene su número de oxidación sin cambios."],
        "correcta": "b) Pierde electrones y se oxida."
    },
    {
        "id": 45,
        "pregunta": "Balancea por el método de redox la siguiente ecuación y selecciona los coeficientes de los reactivos:\n___Cu + ___HNO3 → Cu(NO3)2 + NO2 + H2O",
        "opciones": ["a) 1 Cu,4 HNO3", "b) 3 Cu,8 HNO3", "c) 2 Cu,2 HNO3"],
        "correcta": "a) 1 Cu,4 HNO3"
    }
]

# ==========================================
# 2. VARIABLES DE ESTADO (SESSION STATE)
# ==========================================
# Esto evita que se borre la información al interactuar con la página
if 'examen_enviado' not in st.session_state:
    st.session_state.examen_enviado = False
if 'respuestas_usuario' not in st.session_state:
    st.session_state.respuestas_usuario = {}

# ==========================================
# 3. PANTALLA 1: TOMAR EL EXAMEN
# ==========================================
if not st.session_state.examen_enviado:
    st.title("📝 Examen Extraordinario de Química")
    st.info("Lee cuidadosamente cada pregunta. Al finalizar, presiona el botón 'Calificar Examen' al fondo de la página.")
    
    # Creamos un formulario para que no se recargue la página en cada clic
    with st.form("formulario_examen"):
        respuestas_temporales = {}
        
        for item in examen_quimica:
            st.markdown(f"**{item['id']}. {item['pregunta']}**")
            # El radio button guarda la respuesta del usuario
            respuestas_temporales[item['id']] = st.radio(
                "Selecciona una opción:",
                item['opciones'],
                key=f"q_{item['id']}",
                index=None # Ninguna seleccionada por defecto
            )
            st.write("---")
            
        boton_enviar = st.form_submit_button("✅ Calificar Examen")
        
        if boton_enviar:
            # Guardamos las respuestas en el estado de la sesión
            st.session_state.respuestas_usuario = respuestas_temporales
            st.session_state.examen_enviado = True
            st.rerun() # Forzamos recarga para ir a la Pantalla de Resultados

# ==========================================
# 4. PANTALLA 2: RESULTADOS Y RETROALIMENTACIÓN
# ==========================================
else:
    st.title("📊 Resultados del Examen")
    
    # Calcular el puntaje
    puntaje = 0
    total_preguntas = len(examen_quimica)
    
    for item in examen_quimica:
        resp_usuario = st.session_state.respuestas_usuario.get(item['id'])
        if resp_usuario == item['correcta']:
            puntaje += 1
            
    porcentaje = (puntaje / total_preguntas) * 100

    # Mostrar métricas visuales
    col1, col2, col3 = st.columns(3)
    col1.metric("Aciertos", f"{puntaje} / {total_preguntas}")
    col2.metric("Calificación", f"{round(porcentaje, 1)} / 100")
    
    if porcentaje >= 60:
        st.success("🎉 ¡Felicidades! Has aprobado el examen.")
        st.balloons()
    else:
        st.error("⚠️ Necesitas repasar un poco más. ¡No te rindas!")

    st.progress(int(porcentaje))
    st.write("---")
    
    # Mostrar desglose de respuestas
    st.subheader("🔎 Revisión de Respuestas")
    
    for item in examen_quimica:
        resp_usuario = st.session_state.respuestas_usuario.get(item['id'])
        correcta = item['correcta']
        
        st.markdown(f"**{item['id']}. {item['pregunta']}**")
        
        # Validar y mostrar colores según la respuesta
        if resp_usuario == correcta:
            st.success(f"✅ Tu respuesta: {resp_usuario}")
        else:
            if resp_usuario is None:
                st.warning("⚠️ No respondiste esta pregunta.")
            else:
                st.error(f"❌ Tu respuesta: {resp_usuario}")
            
            # Si se equivocó o no respondió, le mostramos la correcta
            st.info(f"💡 Respuesta correcta: {correcta}")
            
        st.write("---")
        
    # Botón para volver a intentar
    if st.button("🔄 Volver a intentar"):
        st.session_state.examen_enviado = False
        st.session_state.respuestas_usuario = {}
        st.rerun()