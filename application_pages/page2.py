
import streamlit as st
import pandas as pd

def run_page2():
    st.header("Risk Appetite Definition")

    max_expected_loss_threshold = st.sidebar.number_input("Max Expected Loss Threshold", value=50000.0)
    max_unexpected_loss_threshold = st.sidebar.number_input("Max Unexpected Loss Threshold", value=150000.0)
    severe_loss_event_tolerance = st.sidebar.number_input("Severe Loss Event Tolerance", value=5)

    num_kris = st.sidebar.number_input("Number of KRIs", value=2, min_value=1, max_value=5)

    kri_limits = {}
    for i in range(num_kris):
        kri_name = f"KRI {i+1}"
        kri_limit = st.sidebar.number_input(f"{kri_name} Limit", value=100.0)
        kri_limits[kri_name] = kri_limit

    st.subheader("Risk Appetite Parameters")
    st.write(f"Max Expected Loss Threshold: {max_expected_loss_threshold}")
    st.write(f"Max Unexpected Loss Threshold: {max_unexpected_loss_threshold}")
    st.write(f"Severe Loss Event Tolerance: {severe_loss_event_tolerance}")

    st.subheader("KRI Limits")
    for kri_name, kri_limit in kri_limits.items():
        st.write(f"{kri_name}: {kri_limit}")
