# QuLab: Risk Appetite Framework Explorer

## Project Description

QuLab is a Streamlit application designed as a Risk Appetite Framework Explorer. It simulates elements of an operational risk appetite framework, allowing users to define risk tolerance levels and observe their implications on a simulated organization's risk profile and capital management. This interactive tool provides a dynamic way to understand abstract risk concepts related to operational risk management.

## Features

*   **Synthetic Data Generation:** Generates simulated time-series data for business operations (revenue, expenses, profit), operational loss events, and Key Risk Indicators (KRIs).
*   **Risk Profile Visualization:** Displays the simulated 'Risk Capacity' and the evolving 'Risk Profile' of the organization over time, benchmarked against defined risk appetite thresholds.
*   **Breach Monitoring:** Tracks and visualizes instances where the simulated risk profile exceeds the defined risk appetite, presenting these as trend plots.  (Currently not implemented in the provided code but intended)
*   **KRI Dashboard:** Presents a dynamic dashboard of simulated KRIs, highlighting their status relative to pre-set thresholds and indicating potential challenges to the defined risk appetite. (Currently not implemented in the provided code but intended)
*   **Interactive Risk Appetite Definition:**  Allows users to define key risk appetite parameters, such as maximum expected loss, maximum unexpected loss, severe loss event tolerance, and KRI limits, through a user-friendly interface.

## Getting Started

### Prerequisites

*   Python 3.7+
*   Pip package manager

### Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install streamlit pandas numpy plotly
    ```

## Usage

1.  **Run the application:**

    ```bash
    streamlit run app.py
    ```

2.  **Access the application:**

    Open your web browser and navigate to the URL displayed in the terminal (usually `http://localhost:8501`).

3.  **Navigate the Application:**

    *   Use the sidebar to select different pages: "Data Generation", "Risk Appetite Definition", and "Risk Monitoring".

4.  **Data Generation Page:**

    *   Set the desired start and end dates for the simulation.
    *   Adjust the parameters for average daily revenue, revenue volatility, baseline expenses, average daily losses, severity distribution parameters (mu and sigma), and the severe loss threshold.
    *   Review the generated business data and operational losses data displayed as dataframes and interactive plots.

5.  **Risk Appetite Definition Page:**

    *   Define the maximum expected loss threshold, maximum unexpected loss threshold, severe loss event tolerance, and limits for the defined Key Risk Indicators (KRIs).  The number of KRI's to define is adjustable.
    *   Review your defined risk appetite parameters.

6.  **Risk Monitoring Page:**

    *   (Currently not implemented in the provided code) This page is intended to display the organization's risk profile against the defined risk appetite, showing breach monitoring and a KRI dashboard, giving insights into the simulation results based on your parameters in steps 4 and 5.

## Project Structure

```
QuLab/
├── app.py                        # Main Streamlit application file
├── application_pages/            # Directory containing individual page scripts
│   ├── page1.py                  # Data Generation page
│   ├── page2.py                  # Risk Appetite Definition page
│   ├── page3.py                  # Risk Monitoring page (Not Implemented)
│   └── __init__.py
├── README.md                     # This file
└── venv/                         # Virtual environment (optional)
```

## Technology Stack

*   **Python:** Programming language
*   **Streamlit:** Web framework for creating interactive applications
*   **Pandas:** Data analysis and manipulation library
*   **NumPy:** Numerical computing library
*   **Plotly:** Interactive plotting library

## Contributing

Contributions are welcome!  Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with clear, descriptive commit messages.
4.  Submit a pull request to the main branch.

## License

This project is licensed under the [MIT License](LICENSE) - see the `LICENSE` file for details. (Create a LICENSE file and add the appropriate license information.)

## Contact

For questions or issues, please contact:

*   [QuantUniversity](https://www.quantuniversity.com/)
