
# Technical Specification for Jupyter Notebook: Risk Appetite Framework Explorer

This document specifies the design and logical flow for a Jupyter Notebook that simulates an operational risk appetite framework. It aims to provide a hands-on learning experience by allowing users to define risk tolerance levels and observe their implications on a simulated organization's risk profile and capital management.

---

## 1. Notebook Overview

### Learning Goals
This notebook is designed to help users achieve the following learning outcomes:
*   Understand the key insights contained within the provided "Operational Risk Manager Handbook" and supporting data, particularly concerning risk capacity, risk appetite, risk profile, and Key Risk Indicators (KRIs).
*   Learn the fundamental components of an operational risk appetite framework.
*   Explore the dynamic relationship between defined risk appetite, an organization's inherent risk capacity, and its evolving actual risk outcomes.
*   Understand how Key Risk Indicators (KRIs) are effectively utilized to monitor an organization's risk exposure against established appetite thresholds.
*   Appreciate the critical importance of aligning an organization's risk appetite with its overarching business strategy and capital allocation decisions.

### Expected Outcomes
Upon successful completion and interaction with this notebook, users will be able to:
*   Interactively define and modify quantitative risk appetite statements.
*   Visualize the simulated risk capacity and risk profile of an organization over time.
*   Identify and track instances where the simulated risk profile breaches defined risk appetite thresholds.
*   Analyze a dashboard of simulated Key Risk Indicators, observing their status relative to pre-set limits.
*   Understand the conceptual and practical implications of varying risk appetite levels on simulated organizational performance and risk management.

---

## 2. Mathematical and Theoretical Foundations

This section outlines the core concepts and formulas that underpin the simulation, drawing directly from the provided "Operational Risk Manager Handbook" [1].

### 2.1. Foundational Risk Concepts

*   **Risk Capacity:**
    *   **Definition:** The maximum level of risk that an organization can absorb without breaching regulatory capital, damaging its reputation, or failing to meet critical objectives. It represents the absolute maximum risk-taking ability.
    *   **Real-world Application:** Often related to the organization's financial strength (e.g., available capital, liquidity) and operational resilience.

*   **Risk Appetite:**
    *   **Definition:** The amount and type of risk that an organization is willing to pursue, retain, or take to achieve its strategic objectives. It is a more constrained and specific level of risk than risk capacity.
    *   **Real-world Application:** Expressed through quantitative statements (e.g., maximum acceptable loss, VaR limits) and qualitative statements (e.g., willingness to take risks in new markets).

*   **Risk Profile:**
    *   **Definition:** The overall exposure of an organization to various types of risks at a given point in time or over a specific period. It is the aggregate of all risks faced by the organization.
    *   **Real-world Application:** This evolves dynamically based on business activities, external environment, and loss events. The simulation will model this evolution.

*   **Key Risk Indicators (KRIs):**
    *   **Definition:** Metrics used to provide an early warning of increasing risk exposures. They are quantifiable measures that track the health and performance of key risk areas.
    *   **Real-world Application:** Examples include number of failed transactions, employee turnover rates, system downtime, or frequency of customer complaints. KRIs are monitored against predefined thresholds to signal potential breaches of risk appetite.

### 2.2. Quantitative Risk Metrics and Formulas

The simulation will incorporate concepts of Expected Loss and Unexpected Loss, particularly in the context of insurance mitigation as discussed in the provided document [1].

*   **Expected Loss (EL):**
    *   **Definition:** The average or mean loss that an organization expects to incur over a given period, based on historical data and probabilistic models.
    *   **Formula (as adapted from [1], Page 15, for illustrative purposes within insurance context):**
        For a specific loss event with a default probability $PD_A$ and an insured limit $L$, the Expected Loss is given by:
        $$EL = PD_A \cdot L$$
        Where:
        *   $EL$ is the Expected Loss.
        *   $PD_A$ is the probability of a specific adverse event or 'default' occurring (e.g., an operational loss event).
        *   $L$ is the potential magnitude of the loss (e.g., the insured limit).

*   **Unexpected Loss (UL):**
    *   **Definition:** The potential loss that exceeds the expected loss at a certain confidence level. It represents the variability or volatility of losses around the mean. Often associated with Value at Risk (VaR).
    *   **Formula (as provided in [1], Page 15, derived from a simplified two-event probability space for an insured limit):**
        The Unexpected Loss is expressed as a multiple of the standard deviation $\sigma$. For the specific simplified probability space of a full limit loss ($L$) with probability $PD_A$ and no loss ($0$) with probability $1-PD_A$, the standard deviation $\sigma$ is implicitly considered to lead to:
        $$UL = 3 \cdot PD_A \cdot (1 - PD_A) \cdot L$$
        Where:
        *   $UL$ is the Unexpected Loss.
        *   $PD_A$ is the probability of the adverse event.
        *   $(1 - PD_A)$ is the probability of no adverse event.
        *   $L$ is the potential magnitude of the loss.
        *   The factor of 3 is an illustrative multiplier for $\sigma$ to define an unexpected loss threshold (e.g., approximating a 99.7% confidence interval if losses were normally distributed around 0, though not directly applicable here given the specific loss model).

### 2.3. Operational Loss Mitigation via Insurance (Advanced Concept)

The notebook will conceptually explain how insurance can mitigate operational risk, utilizing the formulas provided in the document for transferred and net risk.

*   **Transferred Loss Function ($L_{d,c}(X_i)$):**
    *   **Definition:** This function calculates the portion of a single loss event ($X_i$) that is covered by an insurance policy, given a deductible ($d$) and a maximum cover ($c$).
    *   **Formula (from [1], Page 16):**
        $$L_{d,c}(X_i) = \min(\max(X_i - d, 0), c)$$
        Where:
        *   $X_i$ is the magnitude of an individual operational loss event.
        *   $d$ is the deductible, the amount of loss the organization must bear before insurance coverage begins.
        *   $c$ is the maximum cover provided by the insurance policy for a single event.

*   **Net Aggregate Risk ($S_{net}$):**
    *   **Definition:** The total risk retained by the organization after accounting for the impact of insurance mitigation over a period.
    *   **Formula (from [1], Page 16):**
        $$S_{net} = \sum_{i=1}^{N} X_i - \sum_{i=1}^{N} L_{d,c}(X_i)$$
        Where:
        *   $N$ is the total number of loss events in the period.
        *   $\sum_{i=1}^{N} X_i$ is the gross aggregate risk (total losses before insurance).
        *   $\sum_{i=1}^{N} L_{d,c}(X_i)$ is the total amount of risk transferred to the insurer.

---

## 3. Code Requirements

This section specifies the logical flow, required libraries, data handling, algorithms, and visualizations for the Jupyter Notebook. No Python code will be written directly.

### 3.1. Logical Flow and Code Sections

The notebook will be structured into distinct sections, each with narrative markdown cells explaining "what" and "why," followed by corresponding code cells.

#### Section 1: Notebook Setup and Configuration
*   **Markdown Explanation:** Introduce the notebook's purpose, learning goals, and necessary library imports.
*   **Code Section:**
    *   Import necessary libraries (`pandas`, `numpy`, `scipy.stats`, `matplotlib.pyplot`, `seaborn`, `plotly.express`, `ipywidgets`).
    *   Set up global visualization parameters (e.g., color-blind friendly palette, font sizes).
    *   Define default parameters for synthetic data generation and risk appetite.

#### Section 2: Synthetic Data Generation
*   **Markdown Explanation:** Describe the generation of synthetic time-series data for business operations, financial performance, simulated operational loss events, and Key Risk Indicators (KRIs). Explain the rationale behind using synthetic data (e.g., privacy, reproducibility, demonstrative clarity).
*   **Code Section:**
    *   Function: `generate_business_data(start_date, end_date, avg_revenue, revenue_volatility, baseline_expenses)`
        *   Generates daily time-series for revenue, expenses, and profit.
        *   Uses random walks or simple trends with noise.
    *   Function: `simulate_operational_losses(start_date, end_date, avg_daily_losses, severity_params, severe_loss_threshold)`
        *   Simulates operational loss events using a frequency-severity approach.
        *   **Frequency:** Generate daily number of loss events (e.g., using Poisson distribution).
        *   **Severity:** Generate loss magnitudes for each event (e.g., using Log-Normal or Pareto distribution).
        *   Identify 'severe' loss events based on a configurable threshold.
    *   Function: `generate_kri_data(start_date, end_date, num_kris, baseline_values, volatility_factors, link_to_losses=False)`
        *   Generates time-series data for multiple KRIs.
        *   Some KRIs may be linked to simulated operational performance or losses to demonstrate their sensitivity.
    *   Function: `combine_synthetic_data(business_df, losses_df, kri_df)`
        *   Merges all generated data into a single comprehensive DataFrame.
    *   Execution: Call the above functions to create the initial synthetic dataset.

#### Section 3: Data Handling and Validation
*   **Markdown Explanation:** Detail the importance of data validation to ensure the integrity and expected structure of the generated synthetic dataset before analysis.
*   **Code Section:**
    *   Function: `validate_data(dataframe, expected_columns, expected_dtypes, critical_fields_no_na, pk_column=None)`
        *   Confirm presence of `expected_columns` and their `expected_dtypes`.
        *   Assert no missing values in `critical_fields_no_na`.
        *   Assert primary-key uniqueness if `pk_column` is provided (e.g., 'Date').
        *   Log summary statistics for numeric columns (`.describe()`).
        *   Provide feedback on validation status.
    *   Execution: Apply validation function to the combined synthetic dataset.

#### Section 4: Risk Appetite Definition (User Interaction)
*   **Markdown Explanation:** Explain how users can define the organization's quantitative risk appetite using interactive controls, linking it to the theoretical concepts of EL, UL, and KRI thresholds.
*   **Code Section:**
    *   **User Inputs (using `ipywidgets`):**
        *   Slider: `max_expected_loss_threshold` (e.g., percentage of revenue or absolute value). Inline help: "Define the maximum acceptable Expected Loss over a fiscal period."
        *   Slider: `max_unexpected_loss_threshold_multiplier` (e.g., multiplier for EL, or directly VaR%). Inline help: "Set the tolerance for Unexpected Loss (e.g., as a multiple of Expected Loss or VaR%). This represents potential extreme losses."
        *   Slider: `severe_loss_event_tolerance` (e.g., max number of severe events per period). Inline help: "Specify the maximum acceptable number of 'severe' operational loss events per quarter/year."
        *   Sliders/Text Inputs: `kri_thresholds` (e.g., a dictionary mapping KRI names to their green/amber/red thresholds). Inline help: "Set specific thresholds for each Key Risk Indicator to monitor performance."
    *   **Function:** `display_risk_appetite_inputs()`
        *   Initializes and displays the interactive widgets.
        *   Captures user selections for risk appetite parameters.

#### Section 5: Risk Capacity and Risk Profile Calculation
*   **Markdown Explanation:** Describe how the simulated data is used to calculate the organization's evolving risk profile and its static or dynamically determined risk capacity, setting the stage for comparison with risk appetite.
*   **Code Section:**
    *   Function: `calculate_risk_capacity(financial_data, capital_multiple=0.15)`
        *   Calculates a proxy for risk capacity (e.g., 15% of average annual profit or a fixed capital buffer).
    *   Function: `calculate_risk_profile(daily_losses, daily_kris)`
        *   Aggregates daily operational losses and KRI statuses over defined periods (e.g., monthly, quarterly).
        *   Combines these into a single "risk profile" metric or set of metrics to be compared against appetite.
    *   Function: `apply_insurance_mitigation(loss_series, deductible, cover_limit)`
        *   Calculates the transferred loss for each event using $L_{d,c}(X_i) = \min(\max(X_i - d, 0), c)$.
        *   Calculates the net retained losses $S_{net} = \sum X_i - \sum L_{d,c}(X_i)$.
        *   *This function would be called before calculating the "net" risk profile if insurance is active.*
    *   Execution: Apply calculations across the synthetic dataset.

#### Section 6: Breach Monitoring and Analysis
*   **Markdown Explanation:** Detail how the defined risk appetite is used to monitor and identify instances where the simulated risk profile exceeds acceptable thresholds, highlighting critical periods.
*   **Code Section:**
    *   Function: `monitor_breaches(risk_profile_df, risk_appetite_params)`
        *   Compares simulated EL, UL, severe event count, and KRI values against user-defined risk appetite thresholds.
        *   Flags periods where breaches occur for any of these metrics.
        *   Calculates duration and severity of breaches.
    *   Execution: Run monitoring and store breach data.

#### Section 7: Visualization and Dashboard
*   **Markdown Explanation:** Explain how visualizations provide insights into the simulated risk landscape, enabling users to understand trends, relationships, and the impact of their defined risk appetite.
*   **Code Section:**
    *   Function: `plot_time_series_metrics(df, metrics, title, y_label)`
        *   **Core Visual 1: Trend Plot (Line/Area)**
        *   Generate a time-series plot of simulated business performance (Revenue, Profit).
        *   Generate a time-series plot of aggregate operational losses over time.
        *   Generate a time-series plot showing Risk Capacity vs. Risk Profile, with EL/UL appetite thresholds as horizontal lines. Highlight breach areas (e.g., shaded red zones).
        *   Generate time-series plots for individual KRIs, displaying green/amber/red thresholds.
        *   Style: Clear titles, labeled axes, legends, color-blind friendly palette, font size >= 12 pt. Interactivity enabled if `plotly` is used, with static `matplotlib`/`seaborn` fallback saved as PNG.
    *   Function: `plot_kri_dashboard(kri_status_df)`
        *   **Core Visual 3: Aggregated Comparison (Bar/Heatmap)**
        *   Generate a bar chart showing the count or percentage of time each KRI spent in 'Green', 'Amber', 'Red' zones.
        *   Alternatively, a heatmap showing KRI status over time.
    *   Function: `plot_loss_distribution_and_kri_correlation(losses_df, kri_df)`
        *   **Core Visual 2: Relationship Plot (Scatter/Pair Plot)**
        *   Generate a scatter plot of aggregated monthly/quarterly losses vs. key business metrics (e.g., profit, number of transactions) or relevant KRIs to show potential correlations.
        *   Plot distributions of loss severity.
    *   Function: `display_breach_summary_table(breach_df)`
        *   Present a table summarizing identified breaches (Date, Metric, Actual Value, Threshold, Status).
    *   Execution: Call all plotting functions to render the dashboard.

### 3.2. Input/Output Expectations

*   **Input Data (Internal/Synthetic):**
    *   `start_date` (datetime), `end_date` (datetime) for simulation period.
    *   Numerical parameters for synthetic data generation: `avg_revenue`, `revenue_volatility`, `avg_daily_losses`, `severity_params` (e.g., `(mu, sigma)` for log-normal), `severe_loss_threshold`, `num_kris`, `baseline_values`, `volatility_factors`.
    *   User-defined risk appetite parameters via `ipywidgets` as specified in Section 3.1.
*   **Output Data (DataFrames, Visualizations):**
    *   `business_data_df`: DataFrame with simulated `Date`, `Revenue`, `Expenses`, `Profit`.
    *   `operational_losses_df`: DataFrame with simulated `Date`, `Loss_Amount`, `Loss_Category`, `Is_Severe`.
    *   `kri_data_df`: DataFrame with `Date` and various KRI values.
    *   `risk_profile_df`: DataFrame with `Date`, `Aggregated_EL`, `Aggregated_UL`, `Severe_Event_Count`, and KRI status (e.g., `KRI_1_Status`).
    *   `breach_summary_df`: DataFrame listing all identified breaches.
    *   A series of plots (as described in 3.1) embedded within the notebook, with PNG fallbacks saved to disk.

### 3.3. Expected Libraries and Usage

*   `pandas`: Essential for data manipulation, DataFrame creation, and time-series handling.
*   `numpy`: For numerical operations, random number generation for synthetic data.
*   `scipy.stats`: For sampling from statistical distributions (e.g., Poisson, Log-Normal, Pareto) to simulate loss frequency and severity.
*   `matplotlib.pyplot`: For static plotting and as a backend for `seaborn`. Required for PNG fallbacks.
*   `seaborn`: For enhanced static statistical visualizations.
*   `plotly.express`: Recommended for interactive plots (trend plots, scatter plots) where the environment supports interactivity.
*   `ipywidgets`: For creating interactive user controls (sliders, dropdowns) to define risk appetite.

---

## 4. Additional Notes or Instructions

### Assumptions
*   The synthetic data generation models are simplified proxies of real-world business operations and risk events. They are designed for illustrative purposes rather than precise financial modeling.
*   Risk capacity is calculated as a direct multiple of simulated financial performance, which is a simplification for demonstration.
*   The relationship between KRIs and overall risk profile is illustrative and does not represent complex causal relationships found in real organizations.
*   The formula for Unexpected Loss ($UL = 3 \cdot PD_A \cdot (1 - PD_A) \cdot L$) is used as provided in the reference document [1], acknowledging its derivation from a simplified two-event probability model for loss.
*   The optional lightweight sample data, if provided, assumes the same structure and naming conventions as the synthetic data generated within the notebook.

### Constraints
*   **Performance:** The notebook must execute end-to-end on a mid-spec laptop (8 GB RAM) within 5 minutes. This implies efficient data generation and visualization techniques.
*   **Library Usage:** Only open-source Python libraries available on PyPI may be used.
*   **No Deployment Specifics:** The specification strictly avoids any references to deployment steps, cloud platforms, or specific web frameworks (e.g., Streamlit).
*   **No Direct Code:** Python code is described conceptually, not written explicitly in the specification.
*   **Narrative Clarity:** All major logical steps in the notebook will be accompanied by descriptive markdown cells explaining "what" is happening and "why."
*   **Visual Style:** All visualizations must adhere to a color-blind-friendly palette. Font size for labels and titles must be equal to or greater than 12pt. Plots must have clear titles, labeled axes, and legends.
*   **Interactivity & Fallback:** Where the Jupyter environment supports interactive visualizations (e.g., `plotly`), interactivity should be enabled. A static fallback (saved PNG image) must be provided for environments where interactivity is not supported.
*   **User Interaction:** Parameters for analysis (e.g., risk appetite thresholds) will be exposed through interactive widgets (sliders, dropdowns, text inputs). Each control must include inline help text or tooltips.

### Customization Instructions
The notebook will be designed to encourage user customization:
*   Users can easily modify the parameters used for synthetic data generation (e.g., simulation duration, average revenue, loss frequency, KRI volatility) to observe different organizational scenarios.
*   Users can define and adjust the various risk appetite thresholds (Expected Loss, Unexpected Loss, severe event count, KRI limits) via interactive widgets to immediately see the impact on breach monitoring and risk profile assessment.
*   The KRI thresholds can be customized to explore different levels of sensitivity for early warning signals.

### References
*   [1] Chapter 3: The Risk Management Framework, Chapter 5: Risk Information, Operational Risk Manager Handbook, PRMIA.
*   [2] dalmirPereira/module6_labWork: Lab Exercises from Module 6 - GitHub, https://github.com/dalmirPereira/module6_labWork.
*   [3] International convergence of capital measurement and capital standards, BIS, June 2006.
*   [4] Recognising the risk-mitigating impact of insurance in operational risk modeling, BIS, October 2010.
*   [5] Loss Models, by Stuart A. Klugman, Harry H. Panjer, Gordon E. Willmot.
