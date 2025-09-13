import streamlit as st

st.set_page_config(page_title="GPL y Open Source", page_icon="📘", layout="centered")

# --- CSS para fondo ---
page_bg_img = '''
<style>
.stApp {
background-image: url("https://images.unsplash.com/photo-1519389950473-47ba0277781c"); /* fondo general */
background-size: cover;
background-attachment: fixed;
}

h1, h2, h3, h4, h5, h6, .stMarkdown, .stText, .stRadio label {
color: white !important; /* texto blanco sobre fondo oscuro */
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# --- Cabecera ---
st.image("https://upload.wikimedia.org/wikipedia/commons/9/93/GPLv3_Logo.svg", width=120)
st.title("📘 GPL y Open Source")
st.caption("Autor: **Stefanny Isuhuaylas**")
st.caption("Explora temas en pestañas y pon a prueba tus conocimientos con un quiz interactivo.")

# --- Tabs para la información ---
tab1, tab2, tab3 = st.tabs(["🔓 Open Source", "📝 GPL", "⚖️ Comparación"])

with tab1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/42/Open_Source_Initiative_keyhole.png", width=100)
    st.subheader("¿Qué es Open Source?")
    st.write("El **código abierto** permite leer, modificar y redistribuir libremente el software.")
    with st.expander("Ver ventajas"):
        st.write("- Transparencia: cualquiera revisa el código.")
        st.write("- Seguridad: más ojos encuentran errores.")
        st.write("- Innovación: colaboración global.")
        st.write("- Independencia: menos dependencia de un proveedor.")
    st.image("https://opensource.com/sites/default/files/lead-images/open_source_programmer_520.jpg", use_column_width=True)

with tab2:
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/64/Gnu-bash-logo.svg", width=80)
    st.subheader("¿Qué es la GPL?")
    st.write("La **GNU General Public License (GPL)** es una licencia creada por la Free Software Foundation.")
    with st.expander("Principales puntos de la GPL"):
        st.write("- Uso, estudio, modificación y distribución libres.")
        st.write("- **Copyleft**: obliga a mantener la licencia en obras derivadas.")
        st.write("- Versiones: GPLv2, GPLv3, etc.")

with tab3:
    st.subheader("Comparación rápida")
    st.markdown("""
| Aspecto | GPL | MIT/BSD/Apache |
|---|---:|---|
| Copyleft | Sí (obligatorio) | No (opcional) |
| Restricción relicenciar | Alta | Baja |
| Filosofía | Libertades del usuario | Flexibilidad y reutilización |
""")
    with st.expander("Recursos recomendados"):
        st.markdown("- [Free Software Foundation (FSF)](https://www.fsf.org/)")
        st.markdown("- [Licencias GNU](https://www.gnu.org/licenses/)")
        st.markdown("- [Open Source Initiative](https://opensource.org/)")

st.markdown("---")

# --- Quiz interactivo ---
st.header("📝 Quiz interactivo")

questions = [
    {
        "q": "¿Qué significa 'copyleft' en el contexto de la GPL?",
        "options": ["Prohibir la copia del software",
                    "Obligar a que las versiones derivadas mantengan la misma licencia",
                    "Permitir el uso comercial sin condición"],
        "answer": 1
    },
    {
        "q": "¿Cuál de estas licencias es más permisiva (menos restrictiva)?",
        "options": ["GPL", "MIT", "GPLv3"],
        "answer": 1
    },
    {
        "q": "¿Es cierto que todo software bajo GPL es Open Source pero no todo Open Source es GPL?",
        "options": ["Verdadero", "Falso"],
        "answer": 0
    },
    {
        "q": "¿Qué organización creó la GPL?",
        "options": ["Open Source Initiative (OSI)", "Free Software Foundation (FSF)", "Apache Foundation"],
        "answer": 1
    }
]

if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "score" not in st.session_state:
    st.session_state.score = 0

total_q = len(questions)
current = st.session_state.current_q

if current < total_q:
    st.progress(current / total_q)
    q = questions[current]
    st.subheader(f"Pregunta {current+1}/{total_q}")
    st.write(q["q"])
    answer = st.radio("Selecciona una respuesta:", q["options"], key=f"q{current}")
    if st.button("Responder"):
        idx = q["options"].index(answer)
        if idx == q["answer"]:
            st.success("✅ Correcto")
            st.session_state.score += 1
        else:
            st.error("❌ Incorrecto")
        st.session_state.current_q += 1
        st.experimental_rerun()
else:
    st.success(f"¡Quiz completado! Puntuación: {st.session_state.score}/{total_q}")
    st.progress(1.0)
    if st.session_state.score == total_q:
        st.balloons()
    if st.button("Reiniciar quiz"):
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.experimental_rerun()
