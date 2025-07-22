
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go

st.markdown(r\"\"
# 1️⃣ Synthetic Data Generation

This section lets you **simulate business operations and operational losses** using configurable parameters.
Adjust sliders in the sidebar and see live updates—visualizations and data tables update instantly!

---
## Simulation Logic

* **Business growth** is modeled exponentially from a base, parameterized by a _growth rate_.
* **Operational losses** are simulated per day using a Poisson (for frequency) × Normal (for severity) model.
* **KRI (Key Risk Indicator)** is drawn daily from a normal distribution with your specified baseline and volatility.

### Synthetic Data Columns
- `Date`: Calendar day of observation
- `BusinessVolume`: Simulated total business activity measure
- `Revenue`: Revenue, computed as $0.1 \times$ Business Volume
- `KRI`: Key Risk Indicator, a hypothetical metric for operational stress/event risk
- `LossAmount`: Simulated individual operational loss events (by day)
\"\"\")
# ------------ Sidebar simulation parameter inputs -------------
with st.sidebar:
    st.subheader("1. Data Generation Parameters")

    c1, c2 = st.columns(2)
    with c1:
        sim_start_date = st.date_input(
            "Simulation Start Date",
            value=datetime(2022,1,1),
            help="Start date for synthetic data generation."
        )
    with c2:
        sim_end_date = st.date_input(
            "Simulation End Date",
            value=datetime(2022,1,31),
            help="End date for synthetic data generation."
        )

    st.markdown("**Business Parameters**")
    growth_rate = st.slider(
        "Growth Rate",
        min_value=0.0, max_value=0.1, value=0.02, step=0.005, format="%.3f",
        help="Annual growth rate for business volume."
    )

    st.markdown("**Loss Frequency Parameters (Poisson)**")
    loss_freq_mean = st.slider(
        "Loss Frequency Mean",
        min_value=0.5, max_value=10.0, value=2.0, step=0.1, format="%.1f",
        help="Average number of loss events per period."
    )
    loss_freq_std = st.slider(
        "Loss Frequency Std Dev",
        min_value=0.1, max_value=5.0, value=1.0, step=0.1, format="%.1f",
        help="Standard deviation for loss event frequency."
    )

    st.markdown("**Loss Severity Parameters (Normal)**")
    loss_sev_mean = st.slider(
        "Loss Severity Mean",
        min_value=100.0, max_value=5000.0, value=1200.0, step=50.0,
        help="Average amount of each loss event."
    )
    loss_sev_std = st.slider(
        "Loss Severity Std Dev",
        min_value=10.0, max_value=1000.0, value=300.0, step=10.0,
        help="Standard deviation of loss event amounts."
    )

    st.markdown("**KRI Parameters**")
    kri_baseline = st.slider(
        "KRI Baseline",
        min_value=10.0, max_value=100.0, value=50.0, step=1.0,
        help="Average level of the Key Risk Indicator."
    )
    kri_volatility = st.slider(
        "KRI Volatility",
        min_value=1.0, max_value=20.0, value=5.0, step=0.5,
        help="Variability of the Key Risk Indicator."
    )

# --------- Data generation function with Streamlit caching ----------
@st.cache_data(show_spinner=False)
def generate_synthetic_data(start_date, end_date, business_params, loss_freq_params, loss_sev_params, kpi_params):
    if not isinstance(start_date, datetime) or not isinstance(end_date, datetime):
        raise TypeError("start_date and end_date must be datetime objects.")
    if start_date > end_date:
        raise ValueError("start_date must be before end_date.")

    dates = pd.date_range(start_date, end_date)
    df_simulated_operations = pd.DataFrame({'Date': dates})

    # Business Volume simulated as geometric progression
    growth_rate = business_params.get('growth_rate', 0.01)
    df_simulated_operations['BusinessVolume'] = 100.0
    for i in range(1, len(df_simulated_operations)):
        df_simulated_operations.loc[i, 'BusinessVolume'] = df_simulated_operations.loc[i-1, 'BusinessVolume'] * (1 + growth_rate)
    df_simulated_operations['BusinessVolume'] = df_simulated_operations['BusinessVolume'].astype(int)

    # Revenue
    df_simulated_operations['Revenue'] = df_simulated_operations['BusinessVolume'] * 0.1

    # Loss events
    loss_mean = loss_freq_params.get('mean', 2)
    loss_std = loss_freq_params.get('std', 1)
    loss_dfs = []
    for date in dates:
        num_losses = np.random.poisson(loss_mean)
        if num_losses > 0:
            loss_amounts = np.random.normal(
                loss_sev_params.get('mean', 1000),
                loss_sev_params.get('std', 200),
                num_losses
            )
            temp_df = pd.DataFrame({'Date': [date] * num_losses, 'LossAmount': loss_amounts})
            loss_dfs.append(temp_df)

    if loss_dfs:
        df_loss_events = pd.concat(loss_dfs, ignore_index=True)
        df_loss_events['LossAmount'] = df_loss_events['LossAmount'].abs() # ensure positive
    else:
        df_loss_events = pd.DataFrame(columns=['Date', 'LossAmount'])

    # KRI
    baseline = kpi_params.get('baseline', 50)
    volatility = kpi_params.get('volatility', 5)
    df_simulated_operations['KRI'] = np.random.normal(baseline, volatility, len(df_simulated_operations))

    return df_simulated_operations, df_loss_events

# ---- Run simulation on every change ----
df_ops, df_losses = generate_synthetic_data(
    sim_start_date, sim_end_date,
    {'growth_rate': growth_rate},
    {'mean': loss_freq_mean, 'std': loss_freq_std},
    {'mean': loss_sev_mean, 'std': loss_sev_std},
    {'baseline': kri_baseline, 'volatility': kri_volatility}
)

st.subheader("Simulated Business Operations Data")
st.write("Preview of generated data (time-series of Business Volume, Revenue, and KRI):")
st.dataframe(df_ops.head())

# Business metrics plot (Business Volume & Revenue)
fig_metric = go.Figure()
fig_metric.add_trace(
    go.Scatter(x=df_ops['Date'], y=df_ops['BusinessVolume'],
               name="Business Volume", yaxis='y1', mode='lines+markers')
)
fig_metric.add_trace(
    go.Scatter(x=df_ops['Date'], y=df_ops['Revenue'],
               name="Revenue", yaxis='y2', mode='lines+markers')
)
fig_metric.update_layout(
    title="Business Volume and Revenue over Time",
    xaxis_title="Date",
    yaxis=dict(title="Business Volume", titlefont=dict(color="#1f77b4"), tickfont=dict(color="#1f77b4")),
    yaxis2=dict(title="Revenue", titlefont=dict(color="#ff7f0e"), tickfont=dict(color="#ff7f0e"),
                anchor="x", overlaying="y", side="right"),
    legend=dict(x=0.01, y=0.99, bordercolor="gray", borderwidth=0.5),
    template="plotly_white"
)
st.plotly_chart(fig_metric, use_container_width=True)

# KRI trend plot
fig_kri = px.line(df_ops, x="Date", y="KRI", title="Key Risk Indicator (KRI) Over Time",
                  markers=True,
                  color_discrete_sequence=["#2ca02c"])
st.plotly_chart(fig_kri, use_container_width=True)

st.subheader("Simulated Loss Events Data")
st.write("Each row marks an individual operational loss. Each day can have 0 or more simulated losses.")
if not df_losses.empty:
    st.dataframe(df_losses.head())

    # Loss histogram
    fig_loss_hist = px.histogram(df_losses, x="LossAmount", nbins=30,
                                 title="Distribution of Simulated Loss Amounts",
                                 color_discrete_sequence=["#9467bd"])
    fig_loss_hist.update_layout(xaxis_title="Loss Amount ($)", yaxis_title="Frequency")
    st.plotly_chart(fig_loss_hist, use_container_width=True)
else:
    st.info("No loss events simulated based on current parameters — try increasing frequency or severity.")

st.markdown(r\"\"
---
> 💡 *You can tune all simulation parameters at left. Results update instantly!*
\"\"\")
