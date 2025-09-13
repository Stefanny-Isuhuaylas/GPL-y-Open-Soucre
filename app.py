# app.py
import streamlit as st

st.set_page_config(page_title="GPL y Open Source", page_icon="📘", layout="centered")

# --- Cabecera ---
st.title("📘 GPL y Open Source")
st.caption("Explicación clara, comparaciones, ejemplos y un pequeño quiz para evaluar lo aprendido.")

# --- Introducción ---
st.markdown("""
## 🔎 Introducción
El software de código abierto (Open Source) y las licencias como la **GNU General Public License (GPL)** son pilares del desarrollo colaborativo.
En esta página verás definiciones, características, diferencias clave, ejemplos y recursos para profundizar. Finalmente encontrarás un **quiz** para comprobar tu comprensión.
""")

# --- Sección: ¿Qué es Open Source? ---
st.header("¿Qué es *Open Source*?")
st.markdown("""
**Open Source** (código abierto) se refiere a software cuyo **código fuente** está disponible públicamente para ser leído, estudiado, modificado y redistribuido.  
La *Open Source Initiative (OSI)* establece criterios que una licencia debe cumplir para ser considerada *open source*.
""")
st.markdown("**Ventajas**:")
st.write("- Transparencia: cualquiera puede revisar el código.")
st.write("- Seguridad: más revisiones ayudan a detectar errores.")
st.write("- Innovación: colaboración entre comunidades.")
st.write("- Independencia: menor dependencia de un único proveedor.")

with st.expander("Ver ejemplo de licencias Open Source comunes"):
    st.write("""
    - **MIT**: Muy permisiva; permite reutilizar y sublicenciar con pocas restricciones.  
    - **Apache 2.0**: Permisiva y añade cláusulas sobre patentes.  
    - **BSD**: Similar a MIT (varias variantes).  
    - **GPL**: Es Open Source pero con *copyleft* (ver más abajo).
    """)

# --- Sección: ¿Qué es la GPL? ---
st.header("¿Qué es la GPL?")
st.markdown("""
La **GNU General Public License (GPL)** es una licencia creada por la **Free Software Foundation (FSF)**.  
Su idea central es el **copyleft**: si distribuyes software derivado, debe mantenerse bajo la misma licencia GPL, garantizando que las libertades del software original persistan.
""")
st.markdown("**Puntos clave de la GPL:**")
st.write("- Permite usar, estudiar, modificar y distribuir el software.")
st.write("- Obliga a distribuir el código fuente de las versiones modificadas bajo la misma licencia (copyleft).")
st.write("- Existen versiones (por ejemplo, **GPLv2** y **GPLv3**), cada una con diferencias legales y técnicas.")

with st.expander("Ejemplos de software bajo GPL"):
    st.write("- El núcleo (kernel) de Linux (GPLv2).")
    st.write("- Proyectos del movimiento GNU (herramientas, utilidades).")
    st.write("- Muchos plugins y proyectos comunitarios usan GPL.")

# --- Comparación ---
st.header("Comparación rápida: GPL vs otras licencias Open Source")
st.markdown("""
| Aspecto | GPL | Licencias permisivas (MIT, BSD, Apache) |
|---|---:|---|
| Copyleft | Sí (obligatorio) | No (opcional o ausente) |
| Restricción para redistribuir bajo otra licencia | Alta | Baja |
| Filosofía | Enfatiza las libertades del usuario | Enfatiza la reutilización y flexibilidad |
""")

# --- Sección: Cuándo usar GPL ---
st.header("¿Cuándo conviene usar GPL?")
st.write("""
- Cuando quieres asegurar que cualquier derivado del proyecto también permanezca libre.  
- Cuando priorizas la preservación de las libertades del usuario por sobre la máxima adopción comercial sin restricciones.  
""")

# --- Recursos ---
st.header("Recursos recomendados")
st.markdown("""
- Free Software Foundation (FSF): https://www.fsf.org/  
- GNU Project — Licencias: https://www.gnu.org/licenses/  
- Open Source Initiative (OSI): https://opensource.org/  
""")

# --- Separador ---
st.markdown("---")

# --- QUIZ ---
st.header("📝 Quiz: Pon a prueba tus conocimientos")
st.markdown("Responde las preguntas y presiona **Enviar respuestas** para ver tu puntuación y explicaciones.")

# Preguntas del quiz
quiz_questions = [
    {
        "q": "1) ¿Qué significa 'copyleft' en el contexto de la GPL?",
        "options": [
            "a) Prohibir la copia del software",
            "b) Obligar a que las versiones derivadas mantengan la misma licencia",
            "c) Permitir el uso comercial sin condición"
        ],
        "answer": 1,
        "explain": "Copyleft obliga a que las versiones derivadas se distribuyan bajo la misma licencia, preservando las libertades."
    },
    {
        "q": "2) ¿Cuál de estas licencias es más permisiva (menos restrictiva)?",
        "options": ["a) GPL", "b) MIT", "c) GPLv3"],
        "answer": 1,
        "explain": "La licencia MIT es permisiva y generalmente permite mayor libertad para relicenciar o usar en proyectos propietarios."
    },
    {
        "q": "3) ¿Es cierto que todo software bajo GPL es Open Source pero no todo Open Source es GPL?",
        "options": ["a) Verdadero", "b) Falso"],
        "answer": 0,
        "explain": "GPL cumple los criterios de Open Source, pero existen otras licencias Open Source distintas a la GPL."
    },
    {
        "q": "4) ¿Qué organización creó la GPL?",
        "options": ["a) Open Source Initiative (OSI)", "b) Free Software Foundation (FSF)", "c) Apache Foundation"],
        "answer": 1,
        "explain": "La GPL fue creada por la Free Software Foundation (FSF), impulsada por Richard Stallman."
    },
    {
        "q": "5) ¿Cuál es una ventaja típica del software Open Source?",
        "options": [
            "a) Transparencia y posibilidad de auditoría del código",
            "b) Prohibición de uso comercial",
            "c) Garantía de soporte técnico pagado"
        ],
        "answer": 0,
        "explain": "La transparencia del código es una ventaja clave; no implica prohibición comercial ni garantía de soporte pagado."
    }
]

# Crear formulario para respuestas
with st.form("quiz_form"):
    user_answers = []
    for idx, q in enumerate(quiz_questions):
        st.write(q["q"])
        choice = st.radio("", q["options"], key=f"q{idx}")
        # convertir selección en índice
        selected_index = q["options"].index(choice)
        user_answers.append(selected_index)
        st.write("")  # espacio
    submitted = st.form_submit_button("Enviar respuestas")

# Evaluación y feedback
if submitted:
    score = 0
    total = len(quiz_questions)
    st.subheader("Resultados del Quiz")
    for i, q in enumerate(quiz_questions):
        user_choice = user_answers[i]
        correct = q["answer"]
        if user_choice == correct:
            score += 1
            st.success(f"Pregunta {i+1}: Correcto ✅ — {q['options'][user_choice]}")
        else:
            st.error(f"Pregunta {i+1}: Incorrecto ❌ — Tu respuesta: {q['options'][user_choice]}  |  Respuesta correcta: {q['options'][correct]}")
        st.caption(q["explain"])
    pct = int((score / total) * 100)
    st.markdown(f"**Puntuación:** {score}/{total} ({pct}%)")
    if pct == 100:
        st.balloons()
        st.success("¡Excelente! Conoces bien la diferencia entre GPL y otras licencias Open Source.")
    elif pct >= 60:
        st.info("Buen trabajo — tienes una comprensión sólida, pero revisa algunos puntos.")
    else:
        st.warning("Te recomiendo volver a leer las secciones y repasar los recursos.")

st.markdown("---")
st.caption("Creado para aprendizaje: explicación básica sobre GPL y Open Source. Si quieres más preguntas o añadir ejemplos prácticos (licencias de proyectos reales), dímelo y lo amplío.")
