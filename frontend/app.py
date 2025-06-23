import streamlit as st
import requests

# App Title and Styling
st.markdown("""
    <h1 style='text-align: center; color: #333;'>🔥 Calorie Prediction App 🔥</h1>
    <hr style='border: 1px solid #eee;'/>
""", unsafe_allow_html=True)

st.markdown("### 📝 Fill out your details below")

# Create layout columns for input
with st.form("calorie_form"):
    st.markdown("#### 📌 Basic Information")
    col1, col2 = st.columns(2)
    with col1:
        sex = st.selectbox("Your Sex", ["Male", "Female"], key="sex")
        age = st.slider("Your Age", 20, 80, key="age")
        height = st.number_input("Your Height (cm)", value=100, key="height", placeholder="Height")
        weight = st.number_input("Your Weight (kg)", value=60, key="weight", placeholder="Weight")

    with col2:
        duration = st.number_input("How long you exercise (minutes)", value=20, key="duration", placeholder="Time")
        heart_rate = st.slider("What is your heart rate", 40, 200, key="heart_rate")
        body_temp = st.number_input("Your Body Temp (°C)", value=37, key="body_temp", placeholder="Temperature")

    st.markdown("---")
    submitted = st.form_submit_button("🎯 Predict Burned Calories")

    if submitted:
        user_input = dict(
            Sex=sex.lower(),
            Age=age,
            Height=height,
            Weight=weight,
            Duration=duration,
            Heart_Rate=heart_rate,
            Body_Temp=body_temp
        )
        url = "http://127.0.0.1:8000/predict"
        response = requests.post(url=url, json=user_input)
        result = response.json()
        prediction = result['prediction']

        st.success(f"✅ Calories Burned: **{prediction:.2f} kcal**")

# Footer
st.markdown("<hr style='border: 1px solid #eee;'/>", unsafe_allow_html=True)
st.caption("Built with ❤️ using Streamlit")
