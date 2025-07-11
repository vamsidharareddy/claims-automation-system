# Claims Automation System

This project automates the processing of insurance claims by classifying them as either simple (auto-approvable) or complex (requires human review). It handles input formats like `.txt` and `.pdf`, extracts fields using NLP (spaCy + regex), and routes the claims based on a trained Decision Tree model.

---

## Features

- Accepts PDF and TXT claim documents
- Extracts fields like amount, claim type, and date using regex and spaCy
- Predicts claim complexity using a Decision Tree model
- Routes simple claims automatically and flags complex ones for manual review
- Trained on structured claim data
- Streamlit UI for uploading multiple claims and prioritizing them

---

## Project Structure

<pre>claims-automation-system/ 
├── data
├── processed
├── ingestion
├── extraction
├── decision_engine
├── workflow
├── train_model.py
├── main.py
├── streamlit_app.py 
├── requirements.txt 
└── README.md </pre>

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm

2. Train the model:
   ```bash
   python train_model.py

3. Run the pipeline:
   ```bash
   python main.py

4. Optional - Launch Streamlit UI:
   ```bash
   streamlit run streamlit_app.py


## Sample Output

![Sample Output](assets/sample_output.png)

Skills Demonstrated -

AI/ML: Decision Tree model, feature selection, model training

NLP: Information extraction using regex and spaCy

Document Handling: PDF and TXT parsing

Engineering: Modular architecture (ingestion → extraction → ML → routing)

Deployment: GitHub-based release, Streamlit for UI

## Author

A. Vamsidhara Reddy
B.Tech CSE, Woxsen University
GitHub: @vamsidharareddy
