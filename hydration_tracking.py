import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Title and Introduction
st.title("Hydration Tracker")
st.subheader("Monitor your daily water intake and stay hydrated!")

# Daily Water Intake Monitoring
st.header("Hydration Tracking")
water_intake = st.number_input("Enter your water intake (ml)", min_value=0, step=100, key="intake")
st.write(f"Today's water intake: {water_intake} ml")

# Customized Reminders
st.header("Customized Reminders")
activity_level = st.selectbox("Select your activity level:", ["Low", "Moderate", "High"], key="activity")

# Environmental Factors
st.header("Environmental Factors")
temperature = st.slider("Current temperature (°C):", min_value=-10, max_value=50, key="temp")
humidity = st.slider("Current humidity (%):", min_value=0, max_value=100, key="humidity")

st.write(f"Temperature: {temperature}°C, Humidity: {humidity}%")

# Hydration Recommendations
st.header("Hydration Recommendations")

def calculate_recommendation(temp, humidity, activity):
    base_intake = 2000  # in ml
    if activity == "High":
        base_intake += 500
    if temp > 30:
        base_intake += 300
    if humidity > 70:
        base_intake += 200
    return base_intake

recommended_intake = calculate_recommendation(temperature, humidity, activity_level)
st.write(f"Recommended daily water intake: {recommended_intake} ml")

# Calculate Hydration Goal
goal = recommended_intake - water_intake
if goal < 0:
    goal = 0  # Ensure the goal is not negative

st.header("Hydration Goal")
if water_intake >= recommended_intake:
    st.write("Congratulations! You've met your hydration goal for today.")
    st.write("Keep it up and stay hydrated!")
else:
    st.write(f"To achieve your hydration goal, you need to drink {goal} ml more water.")

# Visualization with Plotly
st.header("Hydration Visualization")

# Create data for plotting
data = {
    'Metric': ['Current Intake', 'Recommended Intake', 'Goal'],
    'Amount (ml)': [water_intake, recommended_intake, max(goal, 0)]  # Use max to avoid negative goal values
}

df = pd.DataFrame(data)

# Plotly bar chart
fig = go.Figure(data=[go.Bar(x=df['Metric'], y=df['Amount (ml)'] , marker_color=['blue', 'orange', 'green'])])
fig.update_layout(title_text='Hydration Metrics', xaxis_title='Metric', yaxis_title='Amount (ml)', template='plotly_white')

st.plotly_chart(fig)

# Display an image related to hydration
st.image("https://www.ukbusinesssupplies.co.uk/cdn/shop/articles/stay-hydrated_500x.jpg?v=1660566417", caption="Stay Hydrated!")
