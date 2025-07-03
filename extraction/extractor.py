import re
import spacy

nlp = spacy.load("en_core_web_sm")
def extract_with_regex(text):
    fields = {}
    def extract_int(label):
        match = re.search(fr"{label}[:\s]*\$?([\d,]+)", text, re.IGNORECASE)
        if match:
            return int(match.group(1).replace(",", ""))
        return None
    def extract_str(label):
        match = re.search(fr"{label}[:\s]*(.+)", text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return None
    fields["claim_id"] = extract_str("Claim ID")
    fields["claim_type"] = extract_str("Claim Type")
    fields["claim_amount"] = extract_int("Claim Amount")
    fields["num_documents"] = extract_int("Number of Documents")
    fields["missing_documents"] = extract_int("Missing Documents")
    fields["incident_description_length"] = extract_int("Incident Description Length")
    fields["prior_claims"] = extract_int("Prior Claims")
    fields["customer_age"] = extract_int("Customer Age")
    fields["flag_fraud_risk"] = extract_int("Fraud Risk Flag")
    fields["submission_delay_days"] = extract_int("Submission Delay Days")
    fields["should_auto_approve"] = extract_int("Should Auto Approve")
    return fields

def extract_with_spacy(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return {"name": ent.text}
    return {"name": None}
def extract_claim_fields(text):
    fields = extract_with_regex(text)
    fields.update(extract_with_spacy(text))
    fields["missing_fields"] = sum(1 for k, v in fields.items()
                                   if k not in ["name", "missing_fields"] and v is None)

    return fields
