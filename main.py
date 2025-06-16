import streamlit as st
import math
import numpy as np
from sympy import symbols, Eq, solve, simplify

st.title("📝 Examen Diagnóstico: Estructuras 1")
st.markdown("""
Evalúa tus conocimientos previos en *Trigonometría, **Álgebra* y *Estática*.
""")

# Inicializar puntaje
if 'score' not in st.session_state:
    st.session_state.score = 0

# Sección 1: Trigonometría
st.header("🔺 Trigonometría")
with st.expander("Preguntas 1-5"):
    st.subheader("1. Resolución de triángulo rectángulo")
    st.write("""
    Dado un triángulo rectángulo con:
    - Cateto adyacente = 6 m
    - Hipotenusa = 10 m
    """)
    q1_opuesto = st.number_input("Cateto opuesto (m):", key="q1_opuesto")
    q1_angulo1 = st.number_input("Primer ángulo agudo (°):", key="q1_angulo1")
    q1_angulo2 = st.number_input("Segundo ángulo agudo (°):", key="q1_angulo2")

    # Verificación respuesta 1
    if st.button("Verificar Pregunta 1"):
        correct_opuesto = math.sqrt(10*2 - 6*2)
        correct_angulo1 = round(math.degrees(math.acos(6/10)))
        correct_angulo2 = 90 - correct_angulo1

        if abs(q1_opuesto - correct_opuesto) < 0.01 and \
           abs(q1_angulo1 - correct_angulo1) < 0.1 and \
           abs(q1_angulo2 - correct_angulo2) < 0.1:
            st.success("✅ Correcto!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Incorrecto. Solución: Cateto opuesto = {correct_opuesto:.2f} m, Ángulos = {correct_angulo1}° y {correct_angulo2}°")

    st.subheader("2. Ecuación trigonométrica")
    st.latex(r"\sin(\theta) = \frac{\sqrt{3}}{2} \quad (0° \leq \theta \leq 90°)")
    q2_theta = st.number_input("Valor de θ (°):", key="q2_theta")

    if st.button("Verificar Pregunta 2"):
        if abs(q2_theta - 60) < 0.1:
            st.success("✅ Correcto!")
            st.session_state.score += 1
        else:
            st.error("❌ Incorrecto. θ = 60°")

# Sección 2: Álgebra
st.header("➗ Álgebra")
with st.expander("Preguntas 6-10"):
    st.subheader("6. Sistema de ecuaciones")
    st.write("Resuelve:")
    st.latex(r"""
    \begin{cases} 
    3x + 2y = 8 \\ 
    x - y = 1 
    \end{cases}
    """)
    q6_x = st.number_input("x:", key="q6_x")
    q6_y = st.number_input("y:", key="q6_y")

    if st.button("Verificar Pregunta 6"):
        if abs(q6_x - 2) < 0.1 and abs(q6_y - 1) < 0.1:
            st.success("✅ Correcto!")
            st.session_state.score += 1
        else:
            st.error("❌ Incorrecto. Solución: x = 2, y = 1")

    st.subheader("7. Factorización")
    st.latex("2x^2 - 8x + 6")
    q7_factor = st.text_input("Factorización (usa formato (ax+b)(cx+d)):", key="q7_factor")

    if st.button("Verificar Pregunta 7"):
        if q7_factor.strip() in ["2(x-1)(x-3)", "(2x-2)(x-3)", "2(x-3)(x-1)"]:
            st.success("✅ Correcto!")
            st.session_state.score += 1
        else:
            st.error("❌ Incorrecto. Solución: 2(x-1)(x-3)")

# Sección 3: Estática
st.header("🏗️ Estática")
with st.expander("Preguntas 11-15"):
    st.subheader("11. Momento de una fuerza")
    q11_def = st.text_area("Define momento de una fuerza y escribe su fórmula:", key="q11_def")

    if st.button("Verificar Pregunta 11"):
        if "fuerza" in q11_def.lower() and "distancia" in q11_def.lower() and ("M = F*d" in q11_def or "M=F*d" in q11_def):
            st.success("✅ Correcto!")
            st.session_state.score += 1
        else:
            st.error("❌ Respuesta esperada: Momento = Fuerza × Distancia perpendicular (M = F·d)")

    st.subheader("15. Tipo de apoyo")
    q15_apoyo = st.radio(
        "Apoyo que restringe traslación vertical pero permite rotación:",
        ["Empotrado", "Articulado", "Rodillo"],
        key="q15_apoyo"
    )

    if st.button("Verificar Pregunta 15"):
        if q15_apoyo == "Rodillo":
            st.success("✅ Correcto!")
            st.session_state.score += 1
        else:
            st.error("❌ Incorrecto. La respuesta correcta es: Rodillo")

# Mostrar puntaje
st.markdown(f"""
## 📊 Puntaje Total: {st.session_state.score}/15
""")

if st.button("Reiniciar Examen"):
    st.session_state.score = 0
    st.experimental_rerun()
