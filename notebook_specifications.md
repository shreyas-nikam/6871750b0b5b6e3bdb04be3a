
# Technical Specification: Risk Appetite Framework Explorer Notebook

This document outlines the technical specifications for a Jupyter Notebook designed to simulate elements of an operational risk appetite framework. It focuses on the logical flow, necessary markdown explanations, and conceptual code sections, excluding actual code implementation or deployment details.

---

## 1. Notebook Overview

This Jupyter Notebook provides an interactive simulation of an operational risk appetite framework. Users will be able to define quantitative risk tolerance levels and observe their impact on a simulated organization's risk profile and capital management, drawing insights from foundational risk management concepts.

### Learning Goals
Upon completing this notebook, users will be able to:
- Understand the key insights contained in the uploaded document and supporting data related to risk management.
- Identify the core components of an operational risk appetite framework.
- Explore the intricate relationship between defined risk appetite, an organization's inherent risk capacity, and actual simulated risk outcomes.
- Comprehend how Key Risk Indicators (KRIs) are effectively utilized to monitor an organization's risk exposure against its stated risk appetite.
- Appreciate the critical importance of aligning an organization's risk appetite with its overarching business strategy and capital allocation.

### Expected Outcomes
The notebook will demonstrate:
- Generation and initial analysis of synthetic time-series data for business operations, financial performance, and simulated operational loss events.
- An interactive interface for defining quantitative risk appetite statements.
- Visualizations comparing simulated risk capacity and evolving risk profile against user-defined risk appetite thresholds.
- Tracking and visualization of instances where the simulated risk profile breaches defined risk appetite.
- A dashboard of simulated Key Risk Indicators (KRIs) highlighting their status relative to pre-set thresholds and demonstrating their utility in risk monitoring.

---

## 2. Mathematical and Theoretical Foundations

This section will explain the core concepts and underlying mathematical formulas essential for understanding the Risk Appetite Framework Explorer. Each concept will be accompanied by its definition, relevance, and, where applicable, derivation, using strict LaTeX formatting.

### 2.1. Risk Capacity and Risk Appetite

**Risk Capacity:**
- **Definition:** The maximum level of risk an organization can bear given its capital, resources, and risk management capabilities, without jeopardizing its financial viability or ability to meet obligations.
- **Explanation:** It represents the absolute upper limit of risk the organization can withstand. Conceptually, it's the total amount of risk an entity can afford to take.

**Risk Appetite:**
- **Definition:** The aggregate amount and type of risk that an organization is willing to accept or retain in pursuit of its strategic objectives.
- **Explanation:** Risk appetite is a more deliberate and strategic choice within the bounds of risk capacity. It guides decision-making by setting explicit quantitative and qualitative thresholds for various risk types. This notebook will focus on quantitative aspects.

### 2.2. Key Risk Indicators (KRIs)

**Key Risk Indicators (KRIs):**
- **Definition:** Metrics used to provide an early signal of increasing risk exposure in a specific area. They are often forward-looking and help monitor the status against risk appetite limits.
- **Explanation:** KRIs are vital for proactive risk management. For instance, an increasing trend in 'Number of Operational Incidents' might be a KRI signaling rising operational risk. The notebook will simulate several KRIs and monitor them against defined thresholds (e.g., Green/Amber/Red zones).

### 2.3. Operational Loss Concepts

The simulation will incorporate concepts of Expected Loss and Unexpected Loss from operational risk, drawing from typical industry definitions.

**Expected Loss ($EL$):**
- **Definition:** The amount of loss that is statistically expected to occur over a specific period. It is often covered by operational provisions or budgeted for as a cost of doing business.
- **Formula Derivation (Simplified for context of insurance default, as per [1, Page 15]):**
    Given an insured limit $L$ and a default probability $PD_A$ associated with the insurer's credit rating, the expected loss due to insurer default is:
    $$ EL = PD_A \cdot L $$
    Where:
    - $EL$: Expected Loss
    - $PD_A$: Probability of Default of the insurer with an A rating.
    - $L$: Insured limit of the policy.
- **Explanation:** In the context of the operational risk appetite, $EL$ can also refer to the average historical loss. For the simulation, we will use it as a target for the maximum acceptable $EL$ over a period.

**Unexpected Loss ($UL$):**
- **Definition:** The amount of loss that could be incurred beyond the expected loss, at a certain confidence level. This is typically covered by capital. It is often expressed using measures like Value at Risk ($VaR$).
- **Formula Derivation (Simplified for context of insurance default, as per [1, Page 15]):**
    Assuming $UL = 3\sigma$ where $\sigma$ is the standard deviation for a binary event (full limit loss or no loss) with probability $PD_A$:
    $$ UL = 3 \cdot L \cdot \sqrt{PD_A (1 - PD_A)} $$
    For small $PD_A$, $\sqrt{PD_A (1 - PD_A)} \approx \sqrt{PD_A}$. However, the document uses $UL = 3 PD_A (1-PD_A)L$ which seems like a direct application of the variance of a Bernoulli trial ($p(1-p)$) multiplied by $L^2$ and then taking $3 \sigma$, which implies $3 \cdot L \cdot \sqrt{PD_A(1-PD_A)}$. We will adhere to the provided example which states $UL \approx 300,000$ for $L=100M, PD_A=0.1\%$ implying the direct formula from text:
    $$ UL = 3 \cdot PD_A \cdot (1 - PD_A) \cdot L $$
    Where:
    - $UL$: Unexpected Loss
    - $PD_A$: Probability of Default of the insurer with an A rating.
    - $L$: Insured limit of the policy.
- **Explanation:** In the context of operational risk appetite, $UL$ represents the capital required to cover losses exceeding the expected amount. Users will set a tolerance for $UL$ (e.g., equivalent to $VaR$ at a 99.9% confidence level).

### 2.4. Loss Mitigation (Simplified Actuarial Approach)

The notebook will simulate the impact of risk mitigation strategies, specifically how an "excess of loss policy" impacts the net risk.

**Aggregate Risk After Insurance Mitigation ($S_{net}$):**
- **Definition:** The total risk retained by the organization after accounting for the impact of insurance policies.
- **Formula (as per [1, Page 16]):**
    $$ S_{net} = \sum_{i=1}^N X_i - \sum_{i=1}^N L_{d,c}(X_i) $$
    Where:
    - $S_{net}$: Aggregate risk after insurance mitigation.
    - $X_i$: Random draw of an individual loss event.
    - $N$: Total number of simulated loss events.
    - $L_{d,c}(X_i)$: The portion of loss $X_i$ covered by the insurance policy, given a deductible $d$ and cover limit $c$.

**Payout Function of an Excess of Loss Policy ($L_{d,c}(X_i)$):**
- **Definition:** This function describes how much an insurance policy pays out for a given loss event $X_i$, considering a deductible and a cover limit.
- **Formula (as per [1, Page 16]):**
    $$ L_{d,c}(X_i) = \min(\max(X_i - d, 0), c) $$
    Where:
    - $L_{d,c}(X_i)$: Amount paid by the insurer for loss $X_i$.
    - $X_i$: Individual loss event amount.
    - $d$: Deductible amount. The policy only pays for losses above this amount.
    - $c$: Cover limit (or policy limit) per loss event. The policy will not pay more than this amount for any single event.
- **Explanation:** This formula captures that no payment occurs if $X_i \le d$. If $X_i > d$, the payment is $X_i - d$, up to a maximum of $c$. The retained loss for the organization would be $X_i - L_{d,c}(X_i)$.

---

## 3. Code Requirements

This section details the expected libraries, input/output, algorithms, and visualization requirements for the notebook. No actual Python code will be written here.

### 3.1. Expected Libraries

The following open-source Python libraries (from PyPI) are expected to be used:
-   **Data Manipulation & Analysis:**
    -   `pandas`: For efficient data structuring (DataFrames) and manipulation of synthetic and calculated risk data.
    -   `numpy`: For numerical operations, array manipulation, and statistical calculations, especially during synthetic data generation and loss modeling.
    -   `scipy.stats`: For generating random numbers from specific statistical distributions (e.g., Poisson for frequency, Lognormal/Pareto for severity) to simulate operational loss events.
-   **Visualization:**
    -   `matplotlib.pyplot`: For creating static and basic interactive plots.
    -   `seaborn`: For enhancing plot aesthetics and creating more complex statistical visualizations with color-blind friendly palettes.
-   **User Interaction:**
    -   `ipywidgets`: For creating interactive controls like sliders, dropdowns, and text inputs, allowing users to define risk appetite parameters dynamically.

### 3.2. Input/Output Expectations

#### Input:
1.  **Synthetic Data Parameters (User Input via Widgets):**
    -   Start and End Dates for simulation.
    -   Average `BusinessVolume` and `Revenue` growth rates.
    -   Base frequency and severity parameters for operational loss events (e.g., mean number of events per period, mean loss amount).
    -   Parameters for KRI generation (e.g., baseline values, volatility).
2.  **Risk Appetite Statements (User Input via Widgets):**
    -   `MaxExpectedLoss_Threshold`: Maximum acceptable Expected Loss (numeric input).
    -   `MaxUnexpectedLoss_Threshold`: Maximum acceptable Unexpected Loss (VaR at a given confidence level, numeric input).
    -   `MaxSevereLossEvents_Threshold`: Maximum acceptable number of 'severe' operational loss events (integer input).
    -   `KRI_1_Limit`, `KRI_2_Limit`, `KRI_3_Limit`: Thresholds for simulated Key Risk Indicators (numeric inputs, potentially with `Green/Amber/Red` definitions).
    -   `RiskCapacity_Value`: A fixed value representing the organization's risk capacity (numeric input).
3.  **Optional Lightweight Sample Data:** A small CSV or Parquet file (<= 5 MB) containing pre-generated synthetic data. This allows the notebook to run without user input for data generation if needed. This will be loaded as a `pandas.DataFrame`.

#### Output:
1.  **DataFrames:**
    -   `df_simulated_operations`: Contains time-series data for business volume, revenue, and other operational metrics.
    -   `df_loss_events`: Details of simulated individual operational loss events (date, type, amount).
    -   `df_risk_profile`: Aggregated time-series data of calculated risk profile metrics (e.g., monthly/quarterly aggregated losses, KRI values).
    -   `df_breaches`: Records instances and details of risk appetite breaches.
2.  **Visualizations:** As specified in Section 3.4.
3.  **Summary Statistics:** Descriptive statistics for generated data and calculated risk metrics.
4.  **Narrative Explanations:** Markdown cells explaining each step and key findings.

### 3.3. Algorithms and Functions to be Implemented (No Code)

This section describes the logical operations and functions that will be part of the notebook's code cells.

1.  **`configure_notebook_environment()`**:
    -   Purpose: Set up display options for pandas, configure logging, and import all necessary libraries.
    -   Inputs: None.
    -   Outputs: Configured environment.

2.  **`generate_synthetic_data(start_date, end_date, business_params, loss_freq_params, loss_sev_params, kpi_params)`**:
    -   Purpose: Create realistic synthetic time-series data.
    -   Logic:
        -   Generate a date range.
        -   Simulate `BusinessVolume` and `Revenue` with trends and seasonality.
        -   Simulate `NumLossEvents` using a Poisson distribution (frequency).
        -   Simulate `LossAmount` for each event using a heavy-tailed distribution (e.g., Lognormal or Pareto) (severity).
        -   Combine frequency and severity to get `AggregatedLoss`.
        -   Simulate `KRI_1`, `KRI_2`, `KRI_3` (e.g., operational incidents, system downtime, employee turnover) with trends and random fluctuations.
        -   Introduce some `severe` loss events based on a configurable threshold.
    -   Outputs: `df_simulated_operations`, `df_loss_events`.

3.  **`validate_and_preprocess_data(df_simulated_operations, df_loss_events)`**:
    -   Purpose: Confirm data integrity and prepare for analysis.
    -   Logic:
        -   Check for expected column names and data types.
        -   Assert no missing values in critical fields (`LossAmount`, `Date`, KRI columns).
        -   Log summary statistics for numeric columns.
        -   Handle any edge cases or initial data cleaning.
    -   Outputs: Validated and preprocessed DataFrames.

4.  **`define_risk_appetite_parameters()`**:
    -   Purpose: Allow users to set their risk appetite thresholds interactively.
    -   Logic:
        -   Utilize `ipywidgets` to create sliders and text inputs for:
            -   `MaxExpectedLoss_Threshold`
            -   `MaxUnexpectedLoss_Threshold` (VaR equivalent)
            -   `MaxSevereLossEvents_Threshold`
            -   `KRI_1_Limit`, `KRI_2_Limit`, `KRI_3_Limit` (with amber/red zones).
            -   `RiskCapacity_Value`
        -   Provide inline help text/tooltips for each control.
    -   Outputs: User-defined threshold values.

5.  **`calculate_risk_profile(df_simulated_operations, df_loss_events, user_parameters)`**:
    -   Purpose: Compute the organization's simulated risk profile over time.
    -   Logic:
        -   Aggregate `LossAmount` over defined periods (e.g., monthly or quarterly) to derive `AggregatedLoss`.
        -   Calculate `ExpectedLoss` (historical average or based on simulation parameters).
        -   Calculate `UnexpectedLoss` (e.g., as VaR at a high confidence level from the simulated loss distribution).
        -   Incorporate `KRI` values from `df_simulated_operations`.
        -   Optionally, apply simplified `Ld,c(X_i)` and `Snet` logic to demonstrate mitigation, if insurance parameters are provided.
    -   Outputs: `df_risk_profile` (time-series of $EL$, $UL$, KRIs, actual aggregated loss).

6.  **`monitor_risk_appetite(df_risk_profile, risk_appetite_params)`**:
    -   Purpose: Compare the risk profile against defined appetite and capacity.
    -   Logic:
        -   Compare `AggregatedLoss` against `MaxExpectedLoss_Threshold`.
        -   Compare simulated `UnexpectedLoss` against `MaxUnexpectedLoss_Threshold`.
        -   Compare `NumSevereLossEvents` against `MaxSevereLossEvents_Threshold`.
        -   Evaluate `KRI` values against their respective limits (Green/Amber/Red status).
        -   Identify any instances where `AggregatedLoss` or `UnexpectedLoss` exceeds `RiskCapacity_Value`.
    -   Outputs: `df_breaches`, `df_kri_status`.

### 3.4. Visualization Requirements

All visualizations must adhere to the following style and usability guidelines:
-   **Color Palette:** Adopt a color-blind-friendly palette (e.g., from `seaborn` or `matplotlib` colormaps).
-   **Font Size:** Font size for titles, labels, and legends should be `≥ 12 pt`.
-   **Labels:** Supply clear titles, labeled axes (including units), and legends where necessary.
-   **Interactivity:** Enable interactivity where the environment supports it (e.g., `plotly` for Jupyter notebooks if `ipywidgets` allows, or `mpl_toolkits.mplot3d` if 3D is used).
-   **Static Fallback:** For each interactive plot, provide code to save a static `.png` image.

#### Core Visuals to be Generated:

1.  **Trend Plot: Risk Profile vs. Risk Appetite & Capacity**
    -   **Type:** Line or Area Plot.
    -   **Content:**
        -   Time-series of `SimulatedAggregatedLoss` (e.g., monthly).
        -   Horizontal lines for `MaxExpectedLoss_Threshold`, `MaxUnexpectedLoss_Threshold` (or VaR equivalent), and `RiskCapacity_Value`.
        -   Optionally, highlight periods of breaches.
    -   **Purpose:** Visualize the organization's risk profile evolution in relation to its defined risk tolerance and capacity.

2.  **Trend Plot: Key Risk Indicator (KRI) Performance**
    -   **Type:** Line Plot, potentially with shaded regions for thresholds.
    -   **Content:**
        -   Time-series of each simulated KRI (`KRI_1`, `KRI_2`, `KRI_3`).
        -   Horizontal lines or shaded regions indicating Green, Amber, and Red thresholds for each KRI.
    -   **Purpose:** Show the dynamics of individual KRIs and their proximity to trigger points for risk action.

3.  **Relationship Plot: Operational Loss Characteristics**
    -   **Type:** Scatter Plot (e.g., `LossAmount` vs. `BusinessVolume`) or Pair Plot (for multiple relationships).
    -   **Content:**
        -   Individual `LossAmount` values against relevant business metrics (e.g., `Revenue`, `BusinessVolume`).
        -   Highlight 'severe' loss events with a distinct color or marker.
    -   **Purpose:** Examine potential correlations between business activity and the frequency/severity of operational losses.

4.  **Aggregated Comparison: KRI Status Dashboard**
    -   **Type:** Bar Chart or Heatmap.
    -   **Content:**
        -   A bar chart showing the average or latest status (e.g., numerical score mapping Green/Amber/Red) for each KRI.
        -   Alternatively, a heatmap showing KRI status over time (e.g., month vs. KRI, colored by status).
    -   **Purpose:** Provide a quick overview of the current or historical risk posture based on KRI performance against appetite.

5.  **Loss Distribution Plot (Optional but Recommended):**
    -   **Type:** Histogram or Density Plot.
    -   **Content:**
        -   Distribution of `LossAmount` or `AggregatedLoss`.
        -   Mark `ExpectedLoss` and `UnexpectedLoss` (VaR) points on the distribution.
    -   **Purpose:** Illustrate the characteristics of the simulated loss data and how $EL$ and $UL$ relate to the loss distribution.

---

## 4. Additional Notes or Instructions

### 4.1. Assumptions
-   The synthetic data generation adequately simulates the complexities of real-world business operations, financial performance, and operational loss events for the purpose of demonstrating the risk appetite framework.
-   The simplified mathematical models for $EL$ and $UL$ (especially concerning insurance default) are sufficient for illustrative purposes within this educational simulation.
-   The user is familiar with basic Jupyter Notebook navigation and interaction with `ipywidgets`.

### 4.2. Constraints
-   **Performance:** The notebook must execute end-to-end on a mid-spec laptop (8 GB RAM) in fewer than 5 minutes. This implies optimizations in synthetic data generation size and simulation complexity.
-   **Libraries:** Only open-source Python libraries available on PyPI may be used.
-   **Code Comments & Narratives:** All major code steps must be accompanied by inline code comments. Additionally, brief narrative (Markdown) cells preceding code blocks must describe **what** is happening in the following code and **why** it is important to the overall analysis.

### 4.3. Customization Instructions
-   **Interactive Controls:** The notebook should prominently feature interactive parameters (sliders, dropdowns, text inputs) using `ipywidgets` for key settings such as:
    -   Parameters for synthetic data generation (e.g., simulation duration, average growth rates, loss frequency/severity).
    -   All quantitative risk appetite thresholds (Maximum $EL$, Maximum $UL$/VaR, Max 'severe' loss events, KRI limits).
-   **Inline Help:** Inline help text or tooltips should be provided for each interactive control to guide learners on its purpose and impact.

### 4.4. References

This notebook draws foundational concepts and inspiration from the following sources:

[1] Chapter 3: The Risk Management Framework, Chapter 5: Risk Information, Operational Risk Manager Handbook, PRMIA.
[2] dalmirPereira/module6_labWork: Lab Exercises from Module 6 - GitHub, https://github.com/dalmirPereira/module6_labWork. (General context on lab exercises)

---
