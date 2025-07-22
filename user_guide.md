id: 6871750b0b5b6e3bdb04be3a_user_guide
summary: Module 6 Lab 1 User Guide
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# QuLab: Risk Appetite Framework Explorer - User Guide

This codelab provides a step-by-step guide to using the **Risk Appetite Framework Explorer** application. This application allows you to simulate, define, and visualize how an organization's risk appetite interacts with its operational risk profile and key risk indicators (KRIs). This is crucial for organizations seeking to balance opportunity with effective risk management.

## Understanding the Application's Importance

Effective operational risk management is vital for any organization. This application empowers you to:

*   **Simulate** business operations and potential losses using various parameters.
*   **Define** an organization's risk appetite by setting thresholds for Expected Loss ($EL$), Unexpected Loss ($UL$), and KRIs.
*   **Visualize** breaches of these thresholds and monitor the overall risk profile in real-time.
*   **Understand** the crucial interaction between Risk Profile and Risk Capacity.

Let's dive into how to use the application!

## Navigating the Application

Duration: 00:01

The application is structured into three key pages, accessible via the **Navigation** dropdown in the sidebar:

*   **Page 1: Data Generation:** Allows you to create synthetic business and operational loss data.
*   **Page 2: Risk Profile Monitoring:** Enables you to define your organization's risk appetite and monitor its risk profile against the set thresholds.
*   **Page 3: KRI Dashboard & References:** Provides a summary of KRI performance and relevant reference materials.

<aside class="positive">
<b>Tip:</b> Use the sidebar to quickly navigate between the different sections of the application.
</aside>

## Page 1: Data Generation - Simulating Business Operations

Duration: 00:05

This page lets you simulate business operations and operational losses by adjusting various parameters using sliders in the sidebar. The visualizations and data tables update instantly, allowing you to see the impact of each parameter change.

### Understanding the Simulation Logic

The simulation works as follows:

*   **Business Growth:** Modeled exponentially from a base, determined by a growth rate you define.
*   **Operational Losses:** Simulated daily using a Poisson distribution (for frequency) multiplied by a Normal distribution (for severity).  This means you control how often losses occur and how large they are on average.
*   **Key Risk Indicator (KRI):** Drawn daily from a normal distribution with a baseline and volatility that you specify.

### Interacting with the Parameters

The sidebar contains the following parameters:

*   **Simulation Start/End Date:** Defines the period for which the data is generated.
*   **Growth Rate:** Influences the exponential growth of the simulated business volume.
*   **Loss Frequency Mean/Std Dev (Poisson):** Controls the average number of loss events per period and its variability.
*   **Loss Severity Mean/Std Dev (Normal):** Determines the average amount of each loss event and its variability.
*   **KRI Baseline/Volatility:** Sets the average level of the KRI and its fluctuation.

Try adjusting these parameters and observe how the charts and tables below change. For instance, increasing the `Loss Frequency Mean` should lead to more frequent loss events in the "Simulated Loss Events Data" section.

### Interpreting the Output

The page displays:

*   **Simulated Business Operations Data:** A table previewing the generated time-series data for `BusinessVolume`, `Revenue`, and `KRI`.
*   **Business Volume and Revenue over Time:** A chart visualizing the trends of business volume and revenue.
*   **Key Risk Indicator (KRI) Over Time:** A chart showing the KRI's fluctuation over the simulation period.
*   **Simulated Loss Events Data:** A table displaying individual loss events, if any, that occurred during the simulation.
*   **Distribution of Simulated Loss Amounts:** A histogram illustrating the distribution of loss amounts.

## Page 2: Risk Profile Monitoring - Defining Risk Appetite and Monitoring Breaches

Duration: 00:10

This section allows you to define your organization's risk appetite and monitor how the simulated risk profile performs against these thresholds. This involves setting limits on key risk metrics and observing potential breaches.

### Defining Your Risk Appetite

The sidebar in this section lets you define quantitative limits for:

*   **Maximum Expected Loss ($EL$):** The highest average loss your organization anticipates.
*   **Maximum Unexpected Loss ($UL$):** The maximum potential deviation from $EL$.
*   **Maximum Severe Loss Events:** The number of high-impact, low-frequency events the organization is willing to tolerate.
*   **KRI Limit:** A threshold for the Key Risk Indicator (KRI); exceeding it signals increased risk.
*   **Risk Capacity:** The total capital or resources available to absorb losses.

Adjust these parameters to simulate different risk stances and see how they affect the breach status.

### Understanding the Risk Profile

The risk profile is calculated based on the simulated data from Page 1 and the risk appetite you define.  Key elements of the risk profile include:

*   **Expected Loss ($EL$):**  The average loss over a specific period.
    $$ EL = \frac{1}{n} \sum_{i=1}^n L_i $$
*   **Unexpected Loss ($UL$):**  The potential for losses exceeding the expected loss, often measured as the standard deviation of losses.
    $$ UL = \sqrt{\frac{1}{n-1} \sum_{i=1}^n (L_i - EL)^2} $$
*   **KRI:** The Key Risk Indicator level.

### Interpreting the Output

The page displays:

*   **Calculated Risk Profile:** A table displaying the daily $EL$, $UL$, KRI, and KRI status.
*   **Risk Appetite Monitoring:** Tables showing whether $EL$, $UL$, and the KRI are within the defined appetite on each simulated day. "Breached" indicates that the loss has crossed the risk appetite limit set in the sidebar.
*   **Risk Profile vs. Risk Appetite Visualizations:** Charts comparing the calculated $EL$ and $UL$ against the defined thresholds, as well as the KRI performance against its limit.

<aside class="negative">
Pay attention to how different Risk Appetite thresholds impact the frequency and severity of breaches in the visualizations.
</aside>

## Page 3: KRI Dashboard & References - Monitoring KRI Performance

Duration: 00:03

This section provides a summary of the Key Risk Indicator (KRI) performance and provides references for further exploration.

### KRI Performance Dashboard

The KRI is a forward-looking measure that provides insight into an organization's operational risk exposure.  Monitoring KRIs helps identify potential issues before they escalate into actual losses.

### Interpreting the Output

The page shows:

*   **KRI Status Summary:** Total simulation days, days KRI was above limit, and the percentage of days above limit.
*   **Daily KRI Status Table:** A detailed breakdown of KRI status for each day.
*   **KRI Distribution by Status:** A bar chart visualizing the distribution of the KRI status (Within Limit vs. Above Limit).
*   **References:** A list of important references for operational risk management.

<aside class="positive">
Use the KRI Dashboard to quickly assess the overall performance of the simulated system against its key risk indicators.
</aside>

## Conclusion

Duration: 00:01

Congratulations! You've now explored the QuLab: Risk Appetite Framework Explorer application and learned how to simulate business operations, define risk appetite, monitor risk profiles, and track KRI performance. By understanding these concepts and utilizing this tool, you can gain valuable insights into managing operational risk effectively within an organization.
