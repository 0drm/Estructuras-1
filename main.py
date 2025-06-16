import streamlit as st
import math
import numpy as np
from sympy import symbols, Eq, solve, simplify, sqrt

st.set_page_config(page_title="Examen Diagnóstico - Estructuras 1", layout="wide")

# Inicializar puntaje y respuestas
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'answers' not in st.session_state:
    st.session_state.answers = {}

# Header
st.title("📝 Examen Diagnóstico: Estructuras 1")
st.markdown("""
Evalúa tus conocimientos previos en *Trigonometría, **Álgebra* y *Estática*.
""")

# Función para verificar respuestas
def check_answer(question, user_answer, correct_answer, tolerance=0.01):
    if isinstance(correct_answer, (int, float)):
        is_correct = abs(user_answer - correct_answer) < tolerance
    else:
        is_correct = str(user_answer).strip().lower() == str(correct_answer).strip().lower()
    
    if is_correct and question not in st.session_state.answers:
        st.session_state.score += 1
        st.session_state.answers[question] = True
    elif not is_correct:
        st.session_state.answers[question] = False
    
    return is_correct

# --- SECCIÓN 1: TRIGONOMETRÍA (5 preguntas) ---
st.header("🔺 Trigonometría")
with st.expander("Preguntas 1-5", expanded=True):
    
    # Pregunta 1
    st.subheader("1. Resolución de triángulo rectángulo")
    st.write("Dado un triángulo rectángulo con cateto adyacente = 6 m e hipotenusa = 10 m:")
    col1, col2, col3 = st.columns(3)
    with col1:
        q1_opuesto = st.number_input("Cateto opuesto (m):", key="q1_opuesto", format="%.2f")
    with col2:
        q1_angulo1 = st.number_input("Ángulo 1 (°):", key="q1_angulo1", format="%.1f")
    with col3:
        q1_angulo2 = st.number_input("Ángulo 2 (°):", key="q1_angulo2", format="%.1f")
    
    if st.button("Verificar Pregunta 1"):
        correct_opuesto = math.sqrt(10*2 - 6*2)
        correct_angulo1 = round(math.degrees(math.acos(6/10)), 1)
        correct_angulo2 = round(90 - correct_angulo1, 1)
        
        correct = (check_answer("q1_opuesto", q1_opuesto, correct_opuesto) and
                  check_answer("q1_angulo1", q1_angulo1, correct_angulo1) and
                  check_answer("q1_angulo2", q1_angulo2, correct_angulo2))
        
        if correct:
            st.success("✅ Correcto!")
        else:
            st.error(f"❌ Incorrecto. Solución: Cateto opuesto = {correct_opuesto:.2f} m, Ángulos = {correct_angulo1}° y {correct_angulo2}°")

    # Pregunta 2
    st.subheader("2. Ecuación trigonométrica")
    st.latex(r"\sin(\theta) = \frac{\sqrt{3}}{2} \quad (0° \leq \theta \leq 90°)")
    q2_theta = st.number_input("Valor de θ (°):", key="q2_theta", format="%.1f")
    
    if st.button("Verificar Pregunta 2"):
        if check_answer("q2_theta", q2_theta, 60.0):
            st.success("✅ Correcto!")
        else:
            st.error("❌ Incorrecto. θ = 60°")

    # Pregunta 3
    st.subheader("3. Escalera contra la pared")
    st.write("Una escalera de 5 m forma 60° con el suelo. ¿Qué altura alcanza?")
    q3_altura = st.number_input("Altura (m):", key="q3_altura", format="%.2f")
    
    if st.button("Verificar Pregunta 3"):
        correct_altura = 5 * math.sin(math.radians(60))
        if check_answer("q3_altura", q3_altura, correct_altura):
            st.success("✅ Correcto!")
        else:
            st.error(f"❌ Incorrecto. Solución: {correct_altura:.2f} m")

    # Pregunta 4
    st.subheader("4. Conversión de ángulos")
    st.write("Convierte 135° a radianes (como fracción simplificada π):")
    q4_rad = st.selectbox("Respuesta:", 
                         ["", "π/2", "3π/4", "2π/3", "5π/6"], 
                         key="q4_rad")
    
    if st.button("Verificar Pregunta 4"):
        if check_answer("q4_rad", q4_rad, "3π/4"):
            st.success("✅ Correcto!")
        else:
            st.error("❌ Incorrecto. Solución: 3π/4")

    # Pregunta 5
    st.subheader("5. Ley de Cosenos")
    st.write("Para un triángulo con lados a=7, b=9 y ángulo C=45°. Encuentra el lado c:")
    q5_c = st.number_input("Longitud de c:", key="q5_c", format="%.2f")
    
    if st.button("Verificar Pregunta 5"):
        correct_c = sqrt(7*2 + 9*2 - 2*7*9*math.cos(math.radians(45)))
        if check_answer("q5_c", q5_c, float(correct_c.evalf())):
            st.success("✅ Correcto!")
        else:
            st.error(f"❌ Incorrecto. Solución: {correct_c.evalf():.2f}")

# --- SECCIÓN 2: ÁLGEBRA (5 preguntas) ---
st.header("➗ Álgebra")
with st.expander("Preguntas 6-10", expanded=True):
    
    # Pregunta 6
    st.subheader("6. Sistema de ecuaciones")
    st.latex(r"""
    \begin{cases} 
    3x + 2y = 8 \\ 
    x - y = 1 
    \end{cases}
    """)
    col1, col2 = st.columns(2)
    with col1:
        q6_x = st.number_input("x:", key="q6_x", format="%.1f")
    with col2:
        q6_y = st.number_input("y:", key="q6_y", format="%.1f")
    
    if st.button("Verificar Pregunta 6"):
        if (check_answer("q6_x", q6_x, 2.0) and 
            check_answer("q6_y", q6_y, 1.0)):
            st.success("✅ Correcto!")
        else:
            st.error("❌ Incorrecto. Solución: x = 2.0, y = 1.0")

    # Pregunta 7
    st.subheader("7. Factorización")
    st.latex("2x^2 - 8x + 6")
    q7_factor = st.text_input("Factorización:", key="q7_factor", value="")
    
    if st.button("Verificar Pregunta 7"):
        accepted_answers = ["2(x-1)(x-3)", "(2x-6)(x-1)", "2(x-3)(x-1)"]
        user_answer = q7_factor.replace(" ", "").lower()
        is_correct = any(user_answer == ans.lower() for ans in accepted_answers)
        
        if is_correct and "q7_factor" not in st.session_state.answers:
            st.session_state.score += 1
            st.session_state.answers["q7_factor"] = True
            st.success("✅ Correcto!")
        elif not is_correct:
            st.session_state.answers["q7_factor"] = False
            st.error("❌ Incorrecto. Soluciones aceptadas: 2(x-1)(x-3) o equivalentes")

    # Pregunta 8
    st.subheader("8. Ecuación matricial")
    st.latex(r"\mathbf{K} \mathbf{D} = \mathbf{F}")
    st.write("Despeja F en términos de K y D:")
    q8_answer = st.text_input("Respuesta:", key="q8_answer", value="")
    
    if st.button("Verificar Pregunta 8"):
        accepted_answers = ["f=k*d", "f = k * d", "f=k×d"]
        if q8_answer.replace(" ", "").lower() in accepted_answers:
            st.success("✅ Correcto!")
            if "q8_answer" not in st.session_state.answers:
                st.session_state.score += 1
                st.session_state.answers["q8_answer"] = True
        else:
            st.error("❌ Incorrecto. Respuesta: F = KD")

    # Pregunta 9
    st.subheader("9. Ecuación cuadrática")
    st.latex("x^2 - 5x + 6 = 0")
    col1, col2 = st.columns(2)
    with col1:
        q9_x1 = st.number_input("Solución x₁:", key="q9_x1", format="%.1f")
    with col2:
        q9_x2 = st.number_input("Solución x₂:", key="q9_x2", format="%.1f")
    
    if st.button("Verificar Pregunta 9"):
        solutions = [2.0, 3.0]
        user_solutions = sorted([q9_x1, q9_x2])
        
        if (abs(user_solutions[0] - solutions[0]) < 0.1 and 
            abs(user_solutions[1] - solutions[1]) < 0.1):
            st.success("✅ Correcto!")
            if "q9_solutions" not in st.session_state.answers:
                st.session_state.score += 1
                st.session_state.answers["q9_solutions"] = True
        else:
            st.error("❌ Incorrecto. Soluciones: x=2.0 y x=3.0")

    # Pregunta 10
    st.subheader("10. Simplificación")
    st.latex(r"\frac{x^2 - 9}{x^2 - 4x + 3}")
    q10_simp = st.text_input("Expresión simplificada:", key="q10_simp", value="")
    
    if st.button("Verificar Pregunta 10"):
        accepted_answers = ["(x+3)/(x-1)", "(x + 3)/(x - 1)"]
        user_answer = q10_simp.replace(" ", "")
        if user_answer.lower() in [ans.lower() for ans in accepted_answers]:
            st.success("✅ Correcto!")
            if "q10_simp" not in st.session_state.answers:
                st.session_state.score += 1
                st.session_state.answers["q10_simp"] = True
        else:
            st.error("❌ Incorrecto. Solución: (x+3)/(x-1)")

# --- SECCIÓN 3: ESTÁTICA (5 preguntas) ---
st.header("🏗️ Estática")
with st.expander("Preguntas 11-15", expanded=True):
    
    # Pregunta 11
    st.subheader("11. Momento de una fuerza")
    q11_def = st.text_area("Definición y fórmula:", key="q11_def", height=100)
    
    if st.button("Verificar Pregunta 11"):
        keywords = ["fuerza", "distancia", "momento", "m = f*d", "m=f×d"]
        user_text = q11_def.lower()
        if any(keyword in user_text for keyword in keywords):
            st.success("✅ Correcto!")
            if "q11_def" not in st.session_state.answers:
                st.session_state.score += 1
                st.session_state.answers["q11_def"] = True
        else:
            st.error("❌ Respuesta debe incluir: Momento = Fuerza × Distancia (M = F·d)")

    # Pregunta 12
    st.subheader("12. Diagrama de cuerpo libre")
    st.write("Dibuja (describe) el DCL de una viga simplemente apoyada con carga puntual en el centro:")
    q12_dcl = st.text_area("Descripción:", key="q12_dcl", height=100)
    
    if st.button("Verificar Pregunta 12"):
        required_terms = ["reacciones", "apoyos", "carga", "vertical"]
        user_text = q12_dcl.lower()
        if sum(term in user_text for term in required_terms) >= 2:
            st.success("✅ Correcto!")
            if "q12_dcl" not in st.session_state.answers:
                st.session_state.score += 1
                st.session_state.answers["q12_dcl"] = True
        else:
            st.error("❌ Debe incluir: reacciones en apoyos y carga vertical central")

    # Pregunta 13
    st.subheader("13. Reacciones en vigas")
    st.write("Viga con carga uniforme q=10 kN/m y L=4 m. Calcule las reacciones:")
    col1, col2 = st.columns(2)
    with col1:
        q13_ra = st.number_input("Reacción A (kN):", key="q13_ra", format="%.1f")
    with col2:
        q13_rb = st.number_input("Reacción B (kN):", key="q13_rb", format="%.1f")
    
    if st.button("Verificar Pregunta 13"):
        correct = 10 * 4 / 2
        if (check_answer("q13_ra", q13_ra, correct) and 
            check_answer("q13_rb", q13_rb, correct)):
            st.success("✅ Correcto!")
        else:
            st.error(f"❌ Incorrecto. Solución: R_A = R_B = {correct:.1f} kN")

    # Pregunta 14
    st.subheader("14. Equilibrio estático")
    q14_cond = st.multiselect(
        "Condiciones para equilibrio:",
        ["ΣF_x = 0", "ΣF_y = 0", "ΣM = 0", "ΣT = 0", "ΣE = 0"],
        key="q14_cond"
    )
    
    if st.button("Verificar Pregunta 14"):
        correct_answers = {"ΣF_x = 0", "ΣF_y = 0", "ΣM = 0"}
        user_answers = set(q14_cond)
        
        if user_answers == correct_answers:
            st.success("✅ Correcto!")
            if "q14_cond" not in st.session_state.answers:
                st.session_state.score += 1
                st.session_state.answers["q14_cond"] = True
        else:
            st.error("❌ Incorrecto. Debe seleccionar: ΣF_x = 0, ΣF_y = 0 y ΣM = 0")

    # Pregunta 15
    st.subheader("15. Tipos de apoyos")
    q15_apoyo = st.radio(
        "Apoyo que restringe traslación vertical pero permite rotación:",
        ["Empotrado", "Articulado", "Rodillo"],
        key="q15_apoyo"
    )
    
    if st.button("Verificar Pregunta 15"):
        if check_answer("q15_apoyo", q15_apoyo, "Rodillo"):
            st.success("✅ Correcto!")
        else:
            st.error("❌ Incorrecto. Respuesta correcta: Rodillo")

# Mostrar resultados
st.markdown("---")
st.header("📊 Resultados")
col1, col2 = st.columns(2)
with col1:
    st.metric("Puntaje Total", f"{st.session_state.score}/15")
with col2:
    st.metric("Porcentaje", f"{(st.session_state.score/15)*100:.1f}%")

if st.button("Reiniciar Examen"):
    st.session_state.score = 0
    st.session_state.answers = {}
    st.experimental_rerun()

# Feedback final
if st.session_state.score >= 12:
    st.balloons()
    st.success("¡Excelente! Estás listo para Estructuras 1.")
elif st.session_state.score >= 8:
    st.warning("Buen trabajo, pero revisa algunos conceptos.")
else:
    st.error("Recomendamos repasar los temas antes de comenzar el curso.")
