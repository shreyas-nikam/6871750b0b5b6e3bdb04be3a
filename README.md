# Module 6 Lab 1: Operational Risk Management with Streamlit

## Project Title and Description

This Streamlit application, **Module 6 Lab 1**, is designed to explore fundamental concepts in operational risk management. It provides an interactive environment to understand risk appetite, risk assessment, and risk mitigation strategies. This lab uses simulated data to demonstrate relationships between risk management parameters and their impact on organizational risk profiles.  The goal is to provide a hands-on learning experience to grasp key risk management concepts.

## Features

*   **Interactive Navigation:**  Easily navigate through different pages of the application using a sidebar menu.
*   **Introduction to Risk:** Understand different types of risk (Operational, Financial, Strategic) with descriptions and visualizations.
*   **Risk Assessment:**  Learn how to assess risk based on likelihood and impact, and visualize the risk scores.
*   **Risk Mitigation:** Explore various risk mitigation strategies and their application.
*   **Data Visualization:** Utilizes Plotly Express for interactive charts and graphs to enhance understanding of the data.
*   **Simulated Data:** Provides a realistic yet controlled environment to learn and experiment with risk management principles.

## Getting Started

These instructions will guide you on setting up and running the Streamlit application on your local machine.

### Prerequisites

*   **Python 3.7+**:  Make sure you have Python 3.7 or a later version installed. You can check your Python version using `python --version` or `python3 --version` in your terminal.
*   **Pip**: Ensure that pip, the Python package installer, is installed.

### Installation

1.  **Clone the Repository:**  Clone this repository to your local machine using Git:

    ```bash
    git clone <repository_url>  # Replace <repository_url> with the actual URL of the repository
    cd <repository_directory>    # Replace <repository_directory> with the directory name
    ```

2.  **Create a Virtual Environment (Recommended):** Create and activate a virtual environment to isolate the project dependencies.

    ```bash
    python -m venv venv       # Create a virtual environment named 'venv'
    source venv/bin/activate  # Activate the virtual environment (Linux/macOS)
    # For Windows, use: venv\Scripts\activate
    ```

3.  **Install Dependencies:** Install the required Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

    **Note:** You'll need to create a `requirements.txt` file.  Based on the `app.py`, `application_pages/page1.py`, `application_pages/page2.py`, and `application_pages/page3.py` files, the `requirements.txt` file should contain the following:

    ```
    streamlit
    pandas
    plotly
    ```

## Usage

1.  **Run the Streamlit Application:** Navigate to the directory containing the `app.py` file and run the application using the following command:

    ```bash
    streamlit run app.py
    ```

2.  **Access the Application:** Streamlit will automatically open the application in your default web browser. If it doesn't, you can access it manually by navigating to the URL provided in the terminal (usually `http://localhost:8501`).

3.  **Navigate and Interact:** Use the sidebar menu to navigate between the different pages of the application.  Interact with the visualizations and explore the risk management concepts presented.

## Project Structure

The project directory is structured as follows:

```
Module6_Lab1/
├── app.py                       # Main Streamlit application file
├── requirements.txt           # List of Python dependencies
├── application_pages/           # Directory containing individual page files
│   ├── page1.py               # Code for "Page 1: Introduction to Risk"
│   ├── page2.py               # Code for "Page 2: Risk Assessment"
│   ├── page3.py               # Code for "Page 3: Risk Mitigation"
│   └── __init__.py            # Makes 'application_pages' a Python package (can be empty)
├── README.md                    # This file
└── .gitignore                   # Specifies intentionally untracked files that Git should ignore
```

## Technology Stack

*   **Python**: Programming language used.
*   **Streamlit**: Framework for building interactive web applications.
*   **Pandas**: Library for data manipulation and analysis.
*   **Plotly Express**: Library for creating interactive visualizations.

## Contributing

We welcome contributions to improve this lab project! If you'd like to contribute, please follow these guidelines:

1.  **Fork the Repository:** Fork the repository to your own GitHub account.
2.  **Create a Branch:** Create a new branch for your changes.
3.  **Make Changes:** Implement your changes, ensuring they are well-documented and tested.
4.  **Submit a Pull Request:** Submit a pull request to the main repository.
5.  **Code Style:**  Follow PEP 8 style guidelines for Python code.
6.  **Testing:**  If you are adding new features, please include appropriate tests.

## License

This project is licensed under the [MIT License](LICENSE). See the `LICENSE` file for details.  (You can add a LICENSE file to the project root if you wish to specify a specific license.)

## Contact

If you have any questions or suggestions, feel free to contact the project maintainers:

*   [QuantUniversity Website](https://www.quantuniversity.com/)
*   [Other relevant contact information] (Replace with your contact info if necessary)
