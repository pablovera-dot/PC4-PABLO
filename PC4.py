
import streamlit as st


paginas = ['Inicio', 'Experiencia', 'Gráficos']

pagina_seleccionada = st.sidebar.selectbox('Selecciona la sección que deseas ver', paginas)

if pagina_seleccionada == 'Inicio':

    st.markdown("<h1 style='text-align: center;'>Pelea de gatos</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    col1.image("Pablo.jpg", caption='Pablo Vera Espinoza', width=300)

   

    texto = """
    ¡Hola! Mi nombre es Pablo Vera, estudio comunicación audiovisual en la PUCP, actualmente cursando el quinto ciclo de la carrera. Estoy convencido de que la cinematografía es un medio de expresión distinto, en el cual podemos mostrarnos como nosotros mismos o a nuestros ideales mediante historias o personajes. En un ámbito más personal, me interesa mucho la producción musical, es un arte que he explorado mucho como oyente, descubriendo géneros y artistas diversos. En un futuro me gustaría poder hacer algo propio, crear y fluir a través de la música. Tengo como principales referentes a Quentin Tarantino, Robert de Niro, The Beatles, Green Day y George Harrison.
    """

    col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)


elif  pagina_seleccionada == 'Experiencia':

    st.markdown("<h1 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h1>", unsafe_allow_html=True)

    texto_2 = """
Mi experiencia programando ha sido realmente enriquecedora. Al principio me sentía con mucha incertidumbre porque no tenía ningún conocimiento del tema y pensaba que quizá no lograría adaptarme a las clases o a las prácticas calificadas. Sin embargo, conforme avanzaron las semanas descubrí que podía entender las primeras funciones con bastante comodidad y que aprender este nuevo lenguaje me resultaba más natural de lo que esperaba. La programación me ha enseñado a ser más paciente, a analizar mejor los problemas y a valorar el proceso de aprendizaje paso a paso. Lo que más me gusta de programar es esa sensación de logro cuando algo funciona después de intentarlo varias veces, y cómo cada línea de código te permite crear algo desde cero . En el futuro, me gustaría seguir desarrollando mis habilidades, ya sea para crear proyectos más complejos, automatizar tareas o incluso involucrarme en áreas como el análisis de datos o el desarrollo web. Siento que aún me queda mucho por aprender, pero voy por buen camino.
    """

    st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto_2}</div>", unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center;'>Aprende a usar las variables: if - elif - else con Pablo 🤓</h2>", unsafe_allow_html=True)
    
    st.video("https://youtu.be/WbcvAGWdMDY?si=pm18qQDZBi0i2rm9")
    
    st.markdown(f"<div style='text-align: center;'><a href='https://drive.google.com/file/d/1REvRXSu3GuGD73w8j44135MkRiezd0gP/view?usp=drive_link' target='_blank'><button>Ver video</button></a></div>", unsafe_allow_html=True) 

else:

    st.markdown("<h1 style='text-align: center;'>Mis primeros gráficos</h1>", unsafe_allow_html=True)

    graficos = ['Nube de Palabras a partir del texto sobre Dina Boluarte',
                'Histograma de goles del Real Madrid',
                'Gráfico de barras de tarjetas rojas recibidas de local',
                'Mapa películas Pablo']

    grafico_seleccionado = st.selectbox('Selecciona un gráfico', graficos)

    if grafico_seleccionado == 'Nube de Palabras a partir del texto sobre Dina Boluarte':
        st.markdown(
            "<div style='text-align: justify; font-size: 20px;'>"
            "El código genera y visualiza una nube de palabras a partir de un texto relacionado con Dina Boluarte, "
            "quien es una política peruana que asumió la presidencia del Perú en diciembre de 2022 luego de la vacancia de Pedro Castillo. "
            "Su gobierno ha estado marcado por fuertes controversias, especialmente por las protestas sociales y las investigaciones "
            "que han surgido durante su mandato. La nube de palabras se construye utilizando las frecuencias de los términos presentes "
            "en ese texto sobre Boluarte, haciendo que las palabras más mencionadas aparezcan con mayor tamaño dentro de la imagen. "
            "Luego, la nube se visualiza con Matplotlib y finalmente se guarda como archivo bajo el nombre nube.png, "
            "permitiendo conservar una representación gráfica de los conceptos más relevantes asociados a ese contenido."
            "</div>", 
            unsafe_allow_html=True
        )
        st.image("nube.png", caption='Nube de Palabras a partir del texto sobre Dina Boluarte', width=500)

    elif grafico_seleccionado == 'Histograma de goles del Real Madrid':
        st.markdown(
            "<div style='text-align: justify; font-size: 20px;'>"
            "Los histogramas presentados muestran la distribución de goles del Real Madrid durante la temporada 2024-2025, "
            "permitiendo analizar su rendimiento tanto en condición de local como de visitante. El primer gráfico refleja la frecuencia "
            "con la que el equipo anotó distintas cantidades de goles cuando jugó en casa, mostrando su desempeño ofensivo en el Santiago Bernabéu. "
            "El segundo histograma representa los goles recibidos como local, lo que permite evaluar la solidez defensiva del equipo en su estadio. "
            "El tercer gráfico muestra cuántos goles anotó el Real Madrid actuando como visitante, proporcionando una comparación de su capacidad ofensiva fuera de casa. "
            "Finalmente, el cuarto histograma evidencia la distribución de goles recibidos como visitante, ofreciendo una visión clara sobre el nivel de vulnerabilidad defensiva del equipo cuando juega lejos de su afición. "
            "En conjunto, estos cuatro histogramas permiten tener una interpretación visual completa sobre el comportamiento ofensivo y defensivo del Real Madrid a lo largo de la temporada. "
            "Este histograma fue desarrollado durante la primera parte de la práctica calificada 3 del curso Pensamiento computacional para las comunicaciones."
            "</div>",
            unsafe_allow_html=True
        )
        st.image("histograma.png", caption='Histograma a partir de la distribución de goles del Real Madrid (2024-2025)', width=500)

    elif grafico_seleccionado == 'Gráfico de barras de tarjetas rojas recibidas de local':
        st.markdown(
            "<div style='text-align: justify; font-size: 20px;'>"
            "El gráfico de barras muestra el promedio de tarjetas rojas que cada equipo de la Liga Española recibió cuando jugó como local durante la temporada 2024-2025. "
            "Para construirlo, se calculó el promedio de expulsiones por equipo agrupando los datos según el club que actuó como local. "
            "De esta manera, el gráfico permite comparar cuáles equipos de la liga fueron expulsados con mayor frecuencia en su propio estadio y cuáles mantuvieron una conducta más disciplinada jugando en casa. "
            "Las barras están ordenadas de mayor a menor promedio, facilitando identificar rápidamente a los clubes con más expulsiones como local. "
            "Además, el color rojo resalta visualmente la temática de tarjetas rojas, mientras que la cuadrícula horizontal ayuda a interpretar mejor los valores. "
            "En conjunto, este gráfico ofrece una visión clara y comparativa del comportamiento disciplinario de los equipos de la Liga Española cuando actuaron como locales durante la temporada. "
            "Este histograma fue desarrollado durante la primera parte de la práctica calificada 3 del curso Pensamiento computacional para las comunicaciones."
            "</div>", 
            unsafe_allow_html=True
        )
        st.image("histograma2.png", caption='Gráfico de barras de tarjetas rojas recibidas de local', width=500)

    elif grafico_seleccionado == 'Mapa películas Pablo':
        st.markdown(
            "<div style='text-align: justify; font-size: 20px;'>"
            "El código tiene como objetivo crear un mapa interactivo utilizando la librería Folium, con el fin de mostrar la ubicación geográfica de mis películas favoritas. "
            "Para ello, se genera primero un mapa base centrado en coordenadas cercanas al ecuador y al meridiano cero, con un nivel de zoom que permite observar amplias regiones del mundo. "
            "A continuación, se recorre un diccionario que contiene información detallada de cada película, incluyendo título, país de origen, director, año de producción y sus coordenadas geográficas (latitud y longitud). "
            "Para cada película, se añade un marcador al mapa, representado con un icono de película de color rojo. "
            "Al hacer clic sobre este marcador, se despliega un popup que muestra de manera organizada la información de la película, permitiendo al usuario consultar el título, el país, el director y el año de producción. "
            "De esta manera, el mapa permite visualizar de forma interactiva la distribución geográfica de las películas favoritas, combinando información detallada con una representación espacial clara y accesible, lo que facilita tanto el análisis como la exploración de los datos."
            "</div>", 
            unsafe_allow_html=True
        )
    
        import streamlit.components.v1 as components
        with open("mapa_peliculas.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=500)
