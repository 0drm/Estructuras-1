import streamlit as st
import pandas as pd
from datetime import datetime

st.title("Examen Diagnóstico – Estructuras 1")
st.write("**Nombre del alumno:**")
nombre = st.text_input("Escribe tu nombre completo")

preguntas = [
    {
        "pregunta": "¿Cuál es el valor de 2(3 + 4)^2 - 5?",
        "opciones": ["89", "93", "77", "91"],
        "respuesta": "89"
    },
    {
        "pregunta": "Resuelve la ecuación: 3x - 7 = 2x + 5",
        "opciones": ["x = 2", "x = 12", "x = -12", "x = -2"],
        "respuesta": "x = 2"
    },
    {
        "pregunta": "Si un triángulo rectángulo tiene un cateto de 3 cm y el otro de 4 cm, ¿cuánto mide la hipotenusa?",
        "opciones": ["6 cm", "5 cm", "7 cm", "4.5 cm"],
        "respuesta": "5 cm"
    },
    {
        "pregunta": "¿Qué representa el seno de un ángulo en un triángulo rectángulo?",
        "opciones": [
            "Cateto opuesto / hipotenusa",
            "Cateto adyacente / hipotenusa",
            "Cateto opuesto / cateto adyacente",
            "Hipotenusa / cateto adyacente"
        ],
        "respuesta": "Cateto opuesto / hipotenusa"
    },
    {
        "pregunta": "¿Cuál es el valor de cos(60°)?",
        "opciones": ["0", "0.5", "√3/2", "1"],
        "respuesta": "0.5"
    },
    {
        "pregunta": "¿Qué unidades se utilizan comúnmente para medir fuerza en el sistema internacional?",
        "opciones": ["Joules", "Kilogramos", "Newtons", "Pascales"],
        "respuesta": "Newtons"
    },
    {
        "pregunta": "¿Cuál es el momento de una fuerza de 10 N aplicada perpendicularmente a una palanca de 2 m?",
        "opciones": ["20 Nm", "5 Nm", "12 Nm", "8 Nm"],
        "respuesta": "20 Nm"
    },
    {
        "pregunta": "¿Cuál de las siguientes ecuaciones representa el equilibrio de fuerzas horizontales?",
        "opciones": ["ΣM = 0", "ΣFx = 0", "ΣFy = 0", "Σa = 0"],
        "respuesta": "ΣFx = 0"
    },
    {
        "pregunta": "¿Cuál es el área de un rectángulo de 4 m de largo por 3 m de ancho?",
        "opciones": ["12 m²", "7 m²", "14 m²", "24 m²"],
        "respuesta": "12 m²"
    },
    {
        "pregunta": "Si un vector tiene magnitud 5 y forma un ángulo de 60° con el eje X, ¿cuál es su componente horizontal?",
        "opciones": ["2.5", "5", "3.5", "5 × cos(60°)"],
        "respuesta": "5 × cos(60°)"
    },
    {
        "pregunta": """Lee el siguiente fragmento:
        "Un sistema estructural es un conjunto de elementos interrelacionados que trabajan juntos para resistir cargas y transferirlas al terreno de forma segura."
        ¿Cuál es el propósito principal de un sistema estructural?""",
        "opciones": [
            "Servir como decoración arquitectónica",
            "Unir los materiales del edificio",
            "Resistir y transferir cargas al terreno",
            "Proteger de la lluvia y el viento"
        ],
        "respuesta": "Resistir y transferir cargas al terreno"
    },
    {
        "pregunta": """Lee el siguiente enunciado:
        "En una viga simplemente apoyada con carga puntual al centro, se produce un momento máximo justo en el punto medio."
        ¿Dónde se encuentra el momento flector máximo?""",
        "opciones": [
            "En los extremos",
            "En el punto medio",
            "En los apoyos",
            "A un cuarto del largo"
        ],
        "respuesta": "En el punto medio"
    }
]

respuestas_usuario = []
correctas = 0

for i, item in enumerate(preguntas):
    st.markdown(f"**{i+1}. {item['pregunta']}**")
    seleccion = st.radio(f"Selecciona una respuesta:", item["opciones"], key=f"q{i}")
    respuestas_usuario.append({
        "pregunta": item["pregunta"],
        "respuesta_usuario": seleccion,
        "respuesta_correcta": item["respuesta"],
        "correcta": seleccion == item["respuesta"]
    })
    if seleccion == item["respuesta"]:
        correctas += 1

if st.button("Enviar y guardar resultados"):
    fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    resultados_df = pd.DataFrame(respuestas_usuario)
    resultados_df.insert(0, "Alumno", nombre)
    resultados_df.insert(1, "Fecha", fecha)
    resultados_df.insert(2, "Calificación", f"{correctas}/12")
    resultados_df.to_csv(f"resultados_{nombre.replace(' ', '_')}_{fecha}.csv", index=False)
    st.success("¡Respuestas guardadas correctamente!")
    st.write(f"Tu calificación es: **{correctas} de 12**")
