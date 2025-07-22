id: 6871750b0b5b6e3bdb04be3a_user_guide
summary: Module 6 Lab 1 User Guide
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# QuLab: Risk Appetite Framework Explorer User Guide

This codelab guides you through the QuLab application, a Risk Appetite Framework Explorer. This application simulates aspects of an operational risk appetite framework, helping you understand risk tolerance and its impact on an organization's risk profile and capital management. Through interactive exploration, you'll gain insights into abstract risk concepts.

## Introduction to Risk Appetite Frameworks
Duration: 00:05

A Risk Appetite Framework (RAF) is a crucial component of an organization's risk management strategy. It defines the types and levels of risk that an organization is willing to accept in pursuit of its strategic objectives. This application allows you to explore and define various elements of such a framework.

Key elements covered in this application:

*   **Risk Appetite:** The level of risk an organization is willing to accept.
*   **Risk Capacity:** The maximum amount of risk an organization can bear without jeopardizing its solvency or strategic goals.
*   **Key Risk Indicators (KRIs):** Metrics used to monitor risk exposures and provide early warnings of potential problems.
*   **Expected Loss (EL):** The average loss an organization anticipates over a given period.  Mathematically expressed as $\text{Expected Loss (EL) = PD_A * L}$, where $PD_A$ is the probability of default and $L$ is the Loss Given Default.
*   **Unexpected Loss (UL):** The potential for losses that exceed the expected loss. We can approximate this as $\text{Unexpected Loss (UL) = 3 * sigma}$, or, expressed differently, $\text{UL = 3 * PD_A * (1 - PD_A) * L}$.

<aside class="positive">
<b>Importance of RAF:</b> A well-defined RAF helps align risk-taking with business strategy, promotes informed decision-making, and enhances risk monitoring and reporting.
</aside>

## Navigating the Application
Duration: 00:02

The application is divided into three main sections, accessible through the sidebar:

*   **Data Generation:** Simulates business data and operational losses.
*   **Risk Appetite Definition:** Allows you to define risk tolerance levels.
*   **Risk Monitoring:** Provides tools to monitor risk exposure against defined appetite.

## Data Generation: Simulating Business and Loss Data
Duration: 00:10

This section allows you to generate synthetic data for your organization's business operations and operational loss events. These simulated data points are critical for exploring how different risk appetite parameters are tested in relation to normal operational events.

1.  **Accessing Data Generation:** In the sidebar, select "Data Generation" from the Navigation dropdown.

2.  **Defining Timeframe:** Specify the start and end dates for the simulation using the "Start Date" and "End Date" date pickers in the sidebar.

3.  **Configuring Business Data:** Adjust the following parameters to simulate your business environment:
    *   **Average Daily Revenue:** Enter the average revenue your organization generates daily.
    *   **Revenue Volatility:** Use the slider to set the volatility of revenue. Higher volatility means more fluctuations in daily revenue.
    *   **Baseline Daily Expenses:** Enter the baseline daily expenses of your organization.

4.  **Simulating Operational Losses:** Configure parameters for simulating operational loss events:
    *   **Average Daily Losses:**  Set the average number of loss events occurring daily.
    *   **Severity Mu:** Adjust the 'mu' parameter for the lognormal distribution that determines the severity of losses.
    *   **Severity Sigma:** Adjust the 'sigma' parameter for the lognormal distribution that determines the severity of losses.
    *   **Severe Loss Threshold:**  Define the threshold above which a loss event is considered severe.

5.  **Reviewing Generated Data:** The application will display two dataframes:
    *   **Business Data:** Shows the simulated revenue, expenses, and profit for each day in the specified timeframe. A line chart visualizing business performance will also be displayed.
    *   **Operational Losses Data:**  Lists each simulated loss event, including the date, loss amount, and whether the loss was classified as severe. A histogram visualizing loss amount distribution and a bar chart showing severe vs. non-severe losses will be displayed.

<aside class="positive">
Experiment with different parameter values to observe their impact on the generated data. For example, increasing revenue volatility will result in more significant fluctuations in the revenue time series.
</aside>

## Risk Appetite Definition: Setting Risk Tolerance
Duration: 00:07

In this section, you will define the organization's risk appetite by setting thresholds for various risk metrics.

1.  **Accessing Risk Appetite Definition:** In the sidebar, select "Risk Appetite Definition" from the Navigation dropdown.

2.  **Setting Loss Thresholds:** Define the maximum acceptable levels for:
    *   **Max Expected Loss Threshold:** The maximum amount of expected loss the organization is willing to tolerate.
    *   **Max Unexpected Loss Threshold:** The maximum amount of unexpected loss the organization is willing to tolerate.
    *   **Severe Loss Event Tolerance:** The maximum number of severe loss events the organization is willing to accept within a given period.

3.  **Configuring Key Risk Indicators (KRIs):**
    *   **Number of KRIs:** Select the number of KRIs you want to define (between 1 and 5).
    *   **KRI Limits:** For each KRI, enter a limit value. This limit represents the threshold beyond which the KRI signals a potential risk appetite breach.

4.  **Reviewing Risk Appetite Parameters:** The application will display a summary of the risk appetite parameters and KRI limits you have defined.

<aside class="negative">
Setting unrealistic or overly conservative risk appetite thresholds can stifle innovation and business growth.  Consider the trade-offs when setting these parameters.
</aside>

## Risk Monitoring: Tracking Risk Exposure
Duration: 00:03

This section (currently under development) will eventually provide tools to monitor the organization's risk profile against the defined risk appetite. This will include visualizing risk capacity, tracking breaches of risk appetite thresholds, and displaying a KRI dashboard. This section is key in understanding how business data and defined risk appetite interact.

1.  **Accessing Risk Monitoring:** In the sidebar, select "Risk Monitoring" from the Navigation dropdown.

2.  **(Future Functionality):** Once implemented, this page will:
    *   Display the simulated 'Risk Capacity' and the evolving 'Risk Profile' of the organization over time, benchmarked against defined risk appetite thresholds.
    *   Track and visualize instances where the simulated risk profile exceeds the defined risk appetite, presenting these as trend plots.
    *   Present a dynamic dashboard of simulated KRIs, highlighting their status relative to pre-set thresholds and indicating potential challenges to the defined risk appetite.

## Understanding Key Equations

Duration: 00:03

The application uses the following equations to model and simulate risk:

*   **Expected Loss (EL):** $\text{EL = PD_A * L}$ -  Represents the average loss anticipated based on probability of default ($PD_A$) and Loss Given Default ($L$).

*   **Unexpected Loss (UL):** $\text{UL = 3 * sigma}$ or $\text{UL = 3 * PD_A * (1 - PD_A) * L}$ - Represents potential losses exceeding the expected loss, calculated using standard deviation ($\sigma$) or probability of default and Loss Given Default.

*   **Net Position After Loss Events:** $\text{S_{net} = sum_{i=1}^{N}X_i - sum_{i=1}^{N}L_{d,c}(X_i)}$ - Calculates the net position after considering loss events and insurance payouts. Where $X_i$ is a random loss event and $L_{d,c}$ is the payout operator, defined as $\text{L_{d,c}(X_i) = min(max(X_i - d, 0), c)}$. Here, $d$ is the deductible and $c$ is the cover per loss event.
