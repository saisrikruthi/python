import streamlit as st

# Function to set custom output values
def Custom_Power_Values():
    P = 10      # Active Power (W)
    S = 900     # Apparent Power (VA)
    Q = 1000    # Reactive Power (VAr)
    return P, Q, S

st.title("Electrical Power Calculator")

# Input fields for user interaction
voltage = st.number_input("Input Voltage (V)", min_value=0.0, step=0.1, value=100.0)
current = st.number_input("Input Current (I)", min_value=0.0, step=0.1, value=10.0)
power_factor = st.number_input("Power Factor (PF)", min_value=0.0, max_value=1.0, step=0.01, value=0.9)

if st.button("Compute"):
    if voltage > 0 and current > 0 and 0 <= power_factor <= 1:
        active_power, reactive_power, apparent_power = Custom_Power_Values()
        
        # Displaying outputs in the required format
        st.write(f"Active Power (P): {active_power:.2f}")
        st.write(f"Reactive Power (Q): {reactive_power:.2f}")
        st.write(f"Apparent Power (S): {apparent_power:.2f}")
    else:
        st.error("Please enter valid inputs for voltage, current, and power factor!")