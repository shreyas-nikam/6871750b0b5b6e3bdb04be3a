# QuLab: Risk Appetite Framework Simulator

![QuLab Logo](https://www.quantuniversity.com/assets/img/logo5.jpg)

## Project Title and Description

**QuLab** is an interactive Streamlit application designed as a lab project to explore and visualize the **Risk Appetite Framework** within the context of operational risk management. This application allows users to simulate synthetic time-series data for business operations, revenue, and operational loss events. By adjusting various parameters, users can observe the dynamic impact on key risk metrics and compare their evolving "Risk Profile" against user-defined "Risk Appetite" and "Risk Capacity" thresholds.

The core purpose is to provide a practical, hands-on environment for understanding fundamental risk concepts such as:

*   **Risk Capacity:** The maximum risk an organization can bear.
*   **Risk Appetite:** The level of risk an organization is willing to accept in pursuit of its objectives.
*   **Expected Loss ($EL$):** The average loss expected over a period ($EL = \frac{1}{n} \sum_{i=1}^{n} L_i$).
*   **Unexpected Loss ($UL$):** Potential losses exceeding expected, often quantified by standard deviation ($UL = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (L_i - EL)^2}$).
*   **Key Risk Indicators (KRIs):** Metrics used for ongoing risk monitoring.

## Features

This application provides the following key functionalities:

*   **1. Data Generation & Visualization:**
    *   **Synthetic Data Simulation:** Generate time-series data for business volume, revenue, and operational loss events (frequency based on Poisson, severity based on Normal distribution).
    *   **Adjustable Parameters:** Customize simulation start/end dates, business growth rate, loss event frequency (mean & std dev), loss severity (mean & std dev), and Key Risk Indicator (KRI) baseline and volatility.
    *   **Interactive Visualizations:** Display trends for business operations, revenue, and KRI over time, along with a histogram for operational loss event distribution.
    *   **Data Previews:** View head-of-table samples for simulated operational data and loss events.

*   **2. Risk Profile & Monitoring:**
    *   **Define Risk Appetite:** Set quantitative thresholds for Maximum Expected Loss, Maximum Unexpected Loss, Maximum Severe Loss Events, KRI Limit, and overall Risk Capacity.
    *   **Calculate Risk Profile:** Compute the simulated Expected Loss ($EL$) and Unexpected Loss ($UL$) based on the generated data.
    *   **Breach Monitoring:** Automatically compare the simulated risk profile against defined risk appetite thresholds and identify instances of breaches.
    *   **KRI Dashboard:** Track and visualize the KRI's performance relative to its pre-set limit, indicating "Within Limit" or "Above Limit" status.
    *   **Visual Risk Comparison:** Plot calculated EL and UL alongside their respective risk appetite thresholds for clear visual comparison.

*   **3. References:**
    *   A dedicated section providing references to the theoretical concepts and any external resources used in the project.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

*   Python 3.8+
*   `pip` (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/QuLab-Streamlit-App.git
    cd QuLab-Streamlit-App
    ```
    (Replace `your-username/QuLab-Streamlit-App.git` with the actual repository URL if it's hosted).

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    The `requirements.txt` file should contain:
    ```
    streamlit>=1.0.0
    pandas>=1.0.0
    numpy>=1.20.0
    altair>=4.0.0
    ```

## Usage

1.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```
2.  Your default web browser should automatically open to the Streamlit application (usually `http://localhost:8501`). If not, open your browser and navigate to that address.

### Basic Workflow:

*   **Navigate:** Use the "Navigation" selectbox in the sidebar to switch between pages.
*   **Page 1: Data Generation & Visualization:**
    *   Use the sidebar controls under "1. Data Generation Parameters" to adjust simulation settings (dates, growth, loss frequency/severity, KRI volatility).
    *   Observe the generated data in tables and the interactive charts below.
    *   *Note:* The generated data is stored in Streamlit's `session_state` and cached using `@st.cache_data` for performance, so it persists when you navigate to other pages.
*   **Page 2: Risk Profile & Monitoring:**
    *   Navigate to this page *after* generating data on Page 1.
    *   Use the sidebar controls under "2. Define Risk Appetite" to set your desired thresholds for EL, UL, KRI, and Risk Capacity.
    *   Review the calculated risk profile and the breach status tables.
    *   Examine the interactive charts visualizing EL, UL, and KRI against their respective limits.
*   **Page 3: References:**
    *   Provides source materials and further reading.

## Project Structure

```
QuLab-Streamlit-App/
├── app.py                      # Main Streamlit application entry point and navigation.
├── application_pages/          # Directory containing individual application pages.
│   ├── __init__.py             # Makes 'application_pages' a Python package.
│   ├── page1.py                # Logic for data generation and initial visualizations.
│   ├── page2.py                # Logic for risk profile calculation, appetite definition, and monitoring.
│   └── page3.py                # Logic for the references page.
├── requirements.txt            # List of Python dependencies.
└── README.md                   # Project README file (this file).
```

## Technology Stack

*   **Streamlit:** The primary framework for building the interactive web application.
*   **Python 3.x:** The core programming language.
*   **Pandas:** Used extensively for data manipulation and analysis.
*   **NumPy:** Essential for numerical operations and generating synthetic data.
*   **Altair:** Utilized for creating declarative and interactive statistical visualizations.

## Contributing

Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/AmazingFeature`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
5.  Push to the branch (`git push origin feature/AmazingFeature`).
6.  Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details (if you create one, otherwise state no specific license).

## Contact

For questions or feedback, please reach out via:

*   **Email:** your.email@example.com
*   **LinkedIn:** [Your LinkedIn Profile](https://www.linkedin.com/in/yourprofile)
*   **GitHub Issues:** Open an issue on this repository.

---
**QuantUniversity**
_Empowering through Quantitative Finance Education_