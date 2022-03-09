import streamlit as st

def cheatsheet():

    text = "# Algunos datos adicionales de la obra"
    st.write(text)


    title = "Quién fue Lina bo Bardi"
    expander = st.expander(title)
    text = "Lina Bo Bardi no solo ha sido la arquitecta contemporánea brasileña más reconocida e influyente sino que, al lado de Alison Smithson, Denise Scott-Brown y otras arquitectas, representa el contrapunto latino a la consolidación predominantemente angloamericana de las mujeres arquitectas."
    expander.write(text)

    title = "Qué otras obras tiene?"
    expander = st.expander(title)
    text = "*Instituto Lina Bo y Pietro Maria Bardi (Casa de Vidro), São Paulo, 1951 - originalmente residencia de la pareja. Museu de Arte de São Paulo, São Paulo, 1958 - considerado su obra prima Proyecto de la *Casa da Cultura*, Recife 1963 Iglesia del Espíritu Santo do Cerrado, Minas Gerais, 1976 Museo de Arte Moderno de Bahía Teatro Oficina, São Paulo, 1990 SESC Pompéia - Fábrica, São Paulo, 1990"
    expander.write(text)

    title = "Dónde estudió?"
    expander = st.expander(title)
    text = """
            Lina Bo Bardi estudió en la Facultad de Arquitectura de la Universidad de Roma durante la década de 1930. Tras graduarse se trasladó a Milán, donde trabajó para Giò Ponti, editor de la revista Quaderni di Domus, de la cual llegó a ser editora."""
    expander.write(text)

    title = "Qué otras producciones tuvo"
    expander = st.expander(title)
    text = "En 1950 creó la revista *Hábitat*"
    expander.write(text)

    title = "Qué otras prácticas artísticas hizo?"
    expander = st.expander(title)
    text = "tuvo siempre una fuerte conexión con el dibujo. A lo largo de su vida y en todas las facetas artísticas a las que se volcó, el dibujo siempre estuvo presente. Más que una herramienta de diseño, dibujar era para ella un medio de expresión primordial, alimentado por un gran sentido de la curiosidad y la duda. El dibujo fue su lenguaje, la prolongación de su pensamiento y el vehículo para su mente. En definitiva, su forma más genuina de explorar, sentir y relacionarse con el mundo."
    expander.write(text)

    title = "Que nos dijo acerca de la Arquitectura?"
    expander = st.expander(title)
    text = """
            *La arquitectura es creada, "inventada de nuevo", por cada hombre que anda en ella, que recorre su espacio, subiendo las escaleras, o descansando sobre una barandilla, levantando la cabeza para oler, abrir o cerrar una puerta, sentarse o levantarse a tener un contacto íntimo y al mismo tiempo crear "formas" en el espacio; el ritual primitivo desde el cual surge la danza, la primera expresión de lo que sería el drama. Este contacto íntimo, ardiente, que una vez fue percibido por el hombre, está ahora en el olvido. Los lugares habituales y comunes hicieron al hombre olvidar la belleza de su "movimiento en el espacio", su movimiento consciente, de mínimos gestos, de menos actitud...* 
            """
    expander.write(text)

    title = "Cuáles son las fuentes de esta información?"
    expander = st.expander(title)
    text = "Puedes consultarlas en: Plataforma Arquitectura, Wikipedia, Artishock, undiaunaarquitecta"
    expander.write(text)


    text =  "Gracias por ser parte de este experimento"
    st.write(text)
