import streamlit as st
import math

def Elec_Power(V, I, PF):
    P = V * I * PF
    Q = V * I * math.sqrt(1 - PF**2)
    S = V * I
    return P, Q, S

# Set the title of the app
st.title("2205A21002-PS2")
col1,col2=st.columns(2)
with col1:
    V = st.number_input("Enter Voltage (V)", min_value=100)
    I = st.number_input("Enter Current (I)", min_value=10)
    PF = st.number_input("Enter Power Factor (PF)", min_value=0.9, max_value=0.9)
    compute=st.button("compute")

with col2:
    with st.container(border=True):
        if compute:
            P, Q, S = Elec_Power(V, I, PF)
            st.write(f"Active Power (P): {P:.2f} W")
            st.write(f"Reactive Power (Q):{Q:.2f} VAR")
            st.write(f"Apparent Power (S):{S:.2f}VA")