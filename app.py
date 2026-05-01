import streamlit as st
from modelo import resolver_citi

st.set_page_config(page_title='Citi CR', page_icon='💼', layout='wide')
st.title('💼 Citi Costa Rica — Optimizador de Analistas')
st.write('Minimiza el tiempo de ciclo de operaciones bancarias.')

# Parámetros ajustables con sliders
st.sidebar.header('⚙️ Parámetros')
analistas = st.sidebar.slider('Analistas disponibles', 5, 20, 12)
min_s     = st.sidebar.slider('Mínimo SWIFT', 1, 8, 4)
min_c     = st.sidebar.slider('Mínimo Cartas', 1, 5, 2)
cap       = st.sidebar.slider('Capacidad mínima', 10, 25, 15)

if st.button('🚀 Optimizar ahora'):
    x1,x2,x3,z = resolver_citi(analistas, min_s, min_c, cap)
    st.success(f'✅ Z* = {z:.0f} horas de ciclo (óptimo)')
    c1,c2,c3 = st.columns(3)
    c1.metric('SWIFT',     int(x1))
    c2.metric('Cartas',    int(x2))
    c3.metric('Garantías', int(x3))
    st.bar_chart({'SWIFT':x1, 'Cartas':x2, 'Garantías':x3})
