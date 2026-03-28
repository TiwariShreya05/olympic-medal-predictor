import streamlit as st
import pickle
import numpy as np

# ---------- Page Config ----------
st.set_page_config(
    page_title="Olympic Medal Predictor",
    page_icon="🥇",
    layout="centered"
)

# ---------- Load Model ----------
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# ---------- UI ----------
st.title("🥇 Olympic Medal Predictor")
st.markdown("Predict how many Olympic medals a country's team will win based on their squad size and past performance.")

st.divider()

col1, col2 = st.columns(2)

with col1:
    athletes = st.number_input(
        "👥 Number of Athletes",
        min_value=1,
        max_value=2000,
        value=100,
        step=1,
        help="Total number of athletes the country is sending to the Olympics"
    )

with col2:
    prev_medals = st.number_input(
        "🏅 Previous Medals Won",
        min_value=0,
        max_value=500,
        value=10,
        step=1,
        help="Total medals the country won in the previous Olympics"
    )

st.divider()

if st.button("🔮 Predict Medals", use_container_width=True, type="primary"):
    input_data = np.array([[athletes, prev_medals]])
    prediction = model.predict(input_data)[0]
    prediction = max(0, round(prediction))  # clip negatives, round to int

    st.success(f"### 🎯 Predicted Medals: **{prediction}**")

    if prediction == 0:
        st.info("The model predicts no medals this time — but every Olympics is a new chance!")
    elif prediction <= 5:
        st.info("A solid performance is expected!")
    elif prediction <= 20:
        st.info("This country is expected to perform very well!")
    else:
        st.info("🔥 This is a powerhouse team — a dominant performance is expected!")

st.divider()
st.caption("Model: Linear Regression trained on Olympic data (pre-2012). Built with Streamlit & scikit-learn.")
