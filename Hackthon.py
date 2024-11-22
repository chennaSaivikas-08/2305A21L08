import streamlit as st
import math


def calculate_Resonance(R, L, C):
    FR = 1 / (2 * math.pi * math.sqrt(L * C))  # Resonance Frequency
    BW = R / (2 * math.pi * L)                 # Bandwidth
    Q = FR / BW                                # Quality Factor
    FL = FR - (BW / 2)                         # Lower Cutoff Frequency
    FU = FR + (BW / 2)                         # Upper Cutoff Frequency
    return FR, BW, Q, FL, FU


st.title("2305A21L08-PS3")
st.write("Calculate resonance frequency (FR), bandwidth (BW), quality factor (Q), upper cutoff frequency (FU), and lower cutoff frequency (FL) based on R, L, and C values for a series resonance circuit.")


col1, col2 = st.columns(2)

with col1:
    with st.container():
        R = st.number_input("Resistance (R) in Ohms:", value=100.0, step=1.0)
        L = st.number_input("Inductance (L) in Henry:", value=0.01, step=0.01)
        C = st.number_input("Capacitance (C) in Farads:", value=0.01, step=0.01)

        compute = st.button("Compute")


with col2:
    with st.container():
        if compute:
            FR, BW, Q, FL, FU = calculate_Resonance(R, L, C)

            
            st.write("### Results:")
            st.write(f"Resonance Frequency (FR): {FR:.2f} Hz")
            st.write(f"Bandwidth (BW): {BW:.2f} Hz")
            st.write(f"Quality Factor (Q): {Q:.2f}")
            st.write(f"Lower Cutoff Frequency (FL): {FL:.2f} Hz")
            st.write(f"Upper Cutoff Frequency (FU): {FU:.2f} Hz")