# QuLab: Risk Appetite Framework Explorer

## Project Title and Description

**QuLab: Risk Appetite Framework Explorer** is an interactive Streamlit application designed to simulate, define, and visualize an organization's risk appetite, its operational risk profile, and key risk indicators (KRIs). This application serves as a practical tool for understanding how risk appetite interacts with operational risk management, allowing users to explore different scenarios and gain insights into risk mitigation strategies. It is specifically designed to be a hands-on learning tool within the context of operational risk management training.

## Features

*   **Synthetic Data Generation:** Simulate business operations and operational losses using configurable parameters such as growth rate, loss frequency, loss severity, and KRI baselines.
*   **Risk Profile Monitoring:** Define organizational risk appetite by setting thresholds for Expected Loss (EL), Unexpected Loss (UL), and KRIs.
*   **Interactive Visualization:** Monitor breaches in real time through interactive visualizations of risk profiles against defined risk appetites.
*   **KRI Dashboard:** Summarize KRI performance against defined limits, providing insights into potential risk exposures.
*   **Formulae Implementation:** Includes implementation and visualization of key risk management formulas, such as Expected Loss and Unexpected Loss.
*   **Multi-Page Navigation:** Provides a structured navigation experience through a sidebar with three distinct pages: Data Generation, Risk Profile Monitoring, and KRI Dashboard & References.
*   **Customizable Parameters:** Offers a wide range of customizable parameters to simulate different business environments and risk scenarios.
*   **Clear Explanations and Context**: Includes informative markdown sections to explain business context and key concepts

## Getting Started

### Prerequisites

*   Python 3.7 or higher
*   Pip package manager

### Installation

1.  **Clone the repository:**

    ```bash
    git clone <your_repo_url>  # Replace with the actual repository URL
    cd QuLab
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    *   On Windows:

        ```bash
        venv\Scripts\activate
        ```

    *   On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

4.  **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

    If a `requirements.txt` is not provided explicitly, generate it after installing the following core dependencies:
    ```bash
    pip install streamlit pandas numpy plotly
    ```

## Usage

1.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

2.  **Access the application in your browser:**  Streamlit will provide a URL (usually `http://localhost:8501`) where you can access the application.

3.  **Using the application:**

    *   **Page 1: Data Generation:**  Adjust simulation parameters in the sidebar to generate synthetic business operation and loss event data.  Explore the generated data in the displayed tables and visualizations.
    *   **Page 2: Risk Profile Monitoring:**  Define your organization's risk appetite by setting thresholds for EL, UL, and KRI limits in the sidebar.  Observe how the simulated risk profile performs against these thresholds.
    *   **Page 3: KRI Dashboard & References:** Review the KRI performance summary and access references related to operational risk management.

## Project Structure

```
QuLab/
├── app.py                       # Main Streamlit application file
├── application_pages/         # Directory containing individual page modules
│   ├── page1.py                # Module for Data Generation
│   ├── page2.py                # Module for Risk Profile Monitoring
│   ├── page3.py                # Module for KRI Dashboard & References
├── README.md                    # This file (project documentation)
├── requirements.txt             # List of Python package dependencies
└── venv/                        # Virtual environment directory (optional)
```

*   `app.py`:  The main entry point of the Streamlit application. It sets up the UI, handles page navigation, and imports the page-specific modules.
*   `application_pages/`:  This directory contains the code for each individual page of the application.  Each `pageX.py` file defines the UI elements, logic, and data processing for that specific page.  This modular structure enhances code organization and maintainability.
*   `requirements.txt`: Lists the Python packages required to run the application, ensuring that the environment can be easily reproduced.

## Technology Stack

*   **Python**: Primary programming language.
*   **Streamlit**: Framework for creating interactive web applications with Python.
*   **Pandas**: Library for data manipulation and analysis.
*   **NumPy**: Library for numerical computing.
*   **Plotly**: Library for creating interactive plots and visualizations.

## Contributing

Contributions are welcome! To contribute to this project, please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive messages.
4.  Test your changes thoroughly.
5.  Submit a pull request to the main branch.

Please ensure that your code adheres to PEP 8 style guidelines and includes appropriate documentation.

## License

This project is licensed under the [MIT License](LICENSE) - see the `LICENSE` file for details.
(Replace `LICENSE` with the actual license filename if different or omit if no license is provided).

## Contact

For questions, suggestions, or issues, please contact:

*   [Your Name/Organization]
*   [Your Email Address]
*   [Link to Repository]
