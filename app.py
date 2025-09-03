import streamlit as st
from circle_utils import area_of_circle

st.title("Circle Area Calculator")

# Input radius
radius = st.number_input("Enter the radius:", min_value=0.0, format="%.2f")

# Calculate button
if st.button("Calculate Area"):
    try:
        area = area_of_circle(radius)
        st.success(f"The area of the circle with radius {radius} is {area:.2f}")
    except ValueError as e:
        st.error(str(e))
