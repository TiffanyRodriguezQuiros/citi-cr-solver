import streamlit as st
import pandas as pd
from modelo import resolver_citi

st.set_page_config(
    page_title="Citi CR",
    page_icon="💼",
    layout="wide"
)

st.sidebar.header("⚙️ Parámetros")

analistas = st.sidebar.slider("Analistas disponibles", 5, 20, 12)
min_s = st.sidebar.slider("Mínimo SWIFT", 1, 8, 4)
min_c = st.sidebar.slider("Mínimo Cartas", 1, 5, 2)
cap = st.sidebar.slider("Capacidad mínima", 10, 25, 15)

st.title("💼 Citi Costa Rica — Optimizador de Analistas")
st.write("Minimiza el tiempo de ciclo de operaciones bancarias.")

if st.button("🚀 Optimizar ahora"):

    x1, x2, x3, z, estado = resolver_citi(
        analistas=analistas,
        min_swift=min_s,
        min_cartas=min_c,
        cap_min=cap
    )

    if estado != "Optimal":
        st.error("No se encontró una solución óptima con los parámetros seleccionados.")
    else:
        st.success(f"✅ Z* = {z:.2f} horas de ciclo óptimo")

        c1, c2, c3 = st.columns(3)

        c1.metric("SWIFT", f"{x1:.2f}")
        c2.metric("Cartas", f"{x2:.2f}")
        c3.metric("Garantías", f"{x3:.2f}")

        datos = pd.DataFrame({
            "Proceso": ["SWIFT", "Cartas", "Garantías"],
            "Analistas": [x1, x2, x3]
        })

        st.bar_chart(datos, x="Proceso", y="Analistas")

        st.write(
            f"La solución óptima asigna **{x1:.2f} analistas a SWIFT**, "
            f"**{x2:.2f} a cartas de crédito** y "
            f"**{x3:.2f} a garantías**. "
            f"El valor mínimo de la función objetivo es **{z:.2f}**."
        )
else:
    st.info("Ajustá los parámetros en la barra lateral y presioná **Optimizar ahora**.")
        f'El valor mínimo de la función objetivo es {z:.0f}.'
    )
