import streamlit as st
import pandas as pd
import joblib

# Load model and encoder
pipeline = joblib.load("pesticide_predictor1.pkl")
label_encoder = joblib.load("label_encoder1.pkl")

# Page config
st.set_page_config(page_title="🌾 Pesticide Adviser", layout="centered")

# Combined CSS: fix white space, fonts, box styling
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Times+New+Roman&display=swap');

    html, body, [class*="css"] {
        font-family: 'Times New Roman', serif;
    }

    .stApp {
        background: linear-gradient(135deg,
            #d0f4f7 0%,
            #fdf6c2 50%,
            #d7f8d1 100%);
        background-attachment: fixed;
        background-size: cover;
        padding-top: 0px !important;
    }

    /* Remove extra white tile */
    header, footer {
        visibility: hidden;
    }

    /* Title Box with glow */
    .title-box {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        margin: 2rem auto 1rem auto;
        max-width: 800px;
        box-shadow: 0 0 15px #8bc34a;
        border: 2px solid #66bb6a;
        color: #2e7d32;
    }

    /* Form/input box */
    .form-box {
        background-color: rgba(255, 255, 255, 0.92);
        padding: 25px;
        border-radius: 15px;
        margin: auto;
        margin-top: 0.5rem;
        max-width: 700px;
        box-shadow: 0 0 8px rgba(0,0,0,0.1);
    }

    .info-box {
        background-color: #e8f5e9;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        font-size: 20px;
        border-left: 6px solid #4caf50;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# ✅ Title Box
st.markdown('<div class="title-box">🌾 Pesticide Adviser For Crop Protection 🌿</div>', unsafe_allow_html=True)
st.write("Help your crops thrive with AI-powered pesticide suggestions.")
st.write("Fill in your field conditions below.")

# Input fields
crop = st.selectbox("🌿 Select Crop", ['Wheat', 'Maize', 'Cotton', 'Tomato'])
pest = st.selectbox("🐛 Select Pest", ['Aphids', 'Cutworms', 'Whiteflies', 'Bollworm', 'Armyworms'])
temperature = st.slider("🌡️ Temperature (°C)", 10.0, 50.0, 30.0)
humidity = st.slider("💧 Humidity (%)", 10.0, 100.0, 60.0)
rainfall = st.slider("🌧️ Rainfall (mm)", 0.0, 300.0, 100.0)
cost = st.slider("💰 Budget / Cost (₹/L)", 50.0, 300.0, 150.0)

effectiveness_map = {'Low': 0, 'Medium': 1, 'High': 2}
effectiveness_label = st.radio("⭐ Desired Effectiveness Level", list(effectiveness_map.keys()), index=2)
effectiveness = effectiveness_map[effectiveness_label]

# Predict button
if st.button("🔍 Predict Pesticide"):
    input_df = pd.DataFrame([{
        'Crop': crop,
        'Pest': pest,
        'Temperature (°C)': temperature,
        'Humidity (%)': humidity,
        'Rainfall (mm)': rainfall,
        'Cost (₹/L)': cost,
        'Effectiveness': effectiveness
    }])

    prediction = model.predict(input_df)[0]
    predicted_pesticide = label_encoder.inverse_transform([prediction])[0]

    st.markdown(f"""
    <div class="info-box">
    🌿 <strong>Recommended Pesticide:</strong> {predicted_pesticide}<br>
    ✅ Based on your input, this is the most suitable pesticide.
    </div>
    """, unsafe_allow_html=True)

# Close form box
st.markdown('</div>', unsafe_allow_html=True)
