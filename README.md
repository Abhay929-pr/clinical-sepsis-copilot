# AI Clinical Co-Pilot for Early Sepsis Detection

This project is a proof-of-concept for an AI-powered clinical decision support tool designed for the early detection and risk stratification of sepsis. It uses a combination of time-series analysis on patient vitals and natural language processing (NLP) on clinical notes to provide a holistic view of a patient's condition.

The application is deployed as a simple, interactive web app using Streamlit.

## Key Features

-   **Data Fusion**: Ingests structured data (vitals, lab results) and unstructured text (clinical notes) to create a comprehensive patient profile.
-   **Sepsis Risk Prediction**: Utilizes a time-series machine learning model (e.g., LSTM or Transformer) to analyze vitals and predict the likelihood of sepsis onset.
-   **Patient Journey Mapping**: Visualizes the patient's risk score over time, allowing clinicians to track their trajectory.
-   **Explainable AI (XAI)**: Includes SHAP (SHapley Additive exPlanations) integration to explain which features are driving the model's predictions, building trust and transparency.
-   **Interactive Web Interface**: A user-friendly Streamlit application allows for easy data upload and visualization of results.

## Technologies Used

-   **Python**: Core programming language.
-   **Pandas**: For data manipulation and preprocessing.
-   **Scikit-Learn**: For classical machine learning models and metrics.
-   **PyTorch / TensorFlow**: For building and training deep learning models (LSTM/Transformer).
-   **Hugging Face Transformers**: For NLP tasks like named entity recognition from clinical notes.
-   **Streamlit**: For building the interactive web application.
-   **SHAP**: For model explainability.

---

## Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites

-   **Python 3.8+**: This project requires a modern version of Python. Python 3.6 and older are **not supported**. It is highly recommended to use Python 3.11 or newer.
-   **Git**: For cloning the repository.

### Installation and Setup

**1. Clone the Repository**

First, clone this repository to your local machine.

```
git clone https://github.com/your-username/clinical-copilot.git
cd clinical-copilot
```

**2. Create and Activate a Virtual Environment**

It is essential to use a virtual environment to manage project dependencies and avoid conflicts.

```
# Create the virtual environment
python -m venv venv

# Activate it
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# On macOS/Linux:
source venv/bin/activate
```

**3. Install Required Libraries**

Install all the necessary Python packages using the `requirements.txt` file.

```
pip install -r requirements.txt
```
*(If you do not have a `requirements.txt` file, you can create one with `pip freeze > requirements.txt` after running the command below)*

```
pip install pandas torch transformers spacy streamlit shap scikit-learn
```

### Running the Application

Once the installation is complete, you can start the Streamlit web application.

```
python -m streamlit run app.py
```

Your default web browser will open with the application running. You can now upload a sample patient data CSV file to see the analysis.

---

## Project Structure

```
clinical-copilot/
│
├── data/
│   └── sample_patient_data.csv   # Sample data for testing
│
├── models/
│   └── sepsis_lstm.pth           # Saved model weights (example)
│
├── scripts/
│   ├── data_preprocessing.py     # Data cleaning and feature engineering
│   ├── nlp_feature_extraction.py # NLP logic
│   └── timeseries_model.py       # Model architecture
│
├── app.py                        # The main Streamlit application file
├── requirements.txt              # Project dependencies
└── README.md                     # This file
```
```
