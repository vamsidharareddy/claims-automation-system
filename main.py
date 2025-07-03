import os
from ingestion.reader import load_claim_file
from extraction.extractor import extract_claim_fields
from workflow.router import predict_complexity

def process_claim(file_path):
    text = load_claim_file(file_path)
    fields = extract_claim_fields(text)
    fields["format"] = file_path.split('.')[-1]
    print(f"File: {file_path}")
    for k, v in fields.items():
        print(f"{k}: {v}")

    complexity = predict_complexity(fields)
    print(f"Predicted Complexity: {complexity}")

    if complexity == "Low":
        print("Routing Decision: Auto-Approved")
    else:
        print("Routing Decision: Sent for Review")

if __name__ == "__main__":
    data_dir = "data"
    claim_files = [f for f in os.listdir(data_dir) if f.endswith((".txt", ".pdf"))]

    if not claim_files:
        print("No claim files found in 'data/' folder.")
    else:
        for file in claim_files:
            process_claim(os.path.join(data_dir, file))
