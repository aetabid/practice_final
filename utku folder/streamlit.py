import streamlit as st

st.set_page_config(page_title="NYC EMS Predictor", page_icon="🚑", layout="wide")
st.markdown("""
<style>
.big-title {font-size: 40px; font-weight: 600; margin-bottom: 0.2rem;}
.sub {font-size: 16px; color: #6b7280; margin-top: 0;}
.card {padding: 18px; border: 1px solid #e5e7eb; border-radius: 14px; background: white;}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<div class='big-title'>🚑🚑 NYC EMS Call & Response Time Predictor🚑🚑</div>", unsafe_allow_html=True)
st.markdown("<p class='sub'>Forecasting call volume and response time by borough (9/1/2024 00:00:00 - 8/31/2025 23:00:00).</p>", unsafe_allow_html=True)
st.divider()

tableau_url = "https://public.tableau.com/views/predictcallsbyborough/Dashboard2?:showVizHome=no"

st.components.v1.iframe(tableau_url, height=1200, scrolling=True)

