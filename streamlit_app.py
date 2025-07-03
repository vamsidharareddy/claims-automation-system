# streamlit_app.py

import streamlit as st
import pandas as pd
import os
import tempfile
from ingestion.reader import load_claim_file
from extraction.extractor import extract_claim_fields
from workflow.router import predict_complexity

st.set_page_config(page_title="Claims Prioritizer", layout="wide")
st.title("Claims Automation and Prioritization")

uploaded_files = st.file_uploader(
    "Upload multiple claim files (.txt or .pdf)", type=["txt", "pdf"], accept_multiple_files=True
)

if uploaded_files:
    results = []

    for file in uploaded_files:
        suffix = file.name.split('.')[-1]
        with tempfile.NamedTemporaryFile(delete=False, suffix='.' + suffix) as tmp:
            tmp.write(file.read())
            tmp_path = tmp.name

        text = load_claim_file(tmp_path)
        fields = extract_claim_fields(text)
        fields["filename"] = file.name
        fields["complexity"] = predict_complexity(fields)

        results.append(fields)

    if results:
        df = pd.DataFrame(results)
        df_sorted = df.sort_values(by="complexity", ascending=False)  # High → Low
        st.success("✅ Claims analyzed and prioritized (High → Low):")
        st.dataframe(df_sorted)
