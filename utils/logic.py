# utils/logic.py
import pandas as pd

df = pd.read_csv('data/symptoms_diseases.csv')

def predict_disease(symptom_input):
    input_symptoms = set(symptom_input.lower().split(','))
    best_match = 0
    predicted_disease = "Unknown"
    
    for _, row in df.iterrows():
        disease_symptoms = set(map(str.strip, row['symptoms'].lower().split(',')))
        match_count = len(input_symptoms & disease_symptoms)
        if match_count > best_match:
            best_match = match_count
            predicted_disease = row['disease']
    
    return {
        "disease": predicted_disease,
        "advice": get_advice(predicted_disease),
        "emergency": "Yes" if predicted_disease == "Flu" else "No"
    }

def get_advice(disease):
    advice_dict = {
        "Common Cold": "Rest and drink plenty of fluids.",
        "Flu": "Seek medical attention if symptoms persist.",
        "Migraine": "Avoid light and loud sounds. Take pain relievers.",
        "Unknown": "Please consult a healthcare professional."
    }
    return advice_dict.get(disease, "Consult a doctor.")
