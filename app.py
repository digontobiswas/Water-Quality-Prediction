import gradio as gr
import pandas as pd
import pickle
import numpy as np

with open("water_quality_model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_potability(ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity):
    input_df = pd.DataFrame([[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]],
                            columns=['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity', 'Organic_carbon', 'Trihalomethanes', 'Turbidity'])
    prediction = model.predict(input_df)[0]
    return "Drinkable" if prediction == 1 else "Not Drinkable"

inputs = [
    gr.Slider(0, 14, value=7, label="pH"),
    gr.Slider(0, 500, value=200, label="Hardness"),
    gr.Slider(0, 50000, value=20000, label="Solids"),
    gr.Slider(0, 20, value=7, label="Chloramines"),
    gr.Slider(0, 500, value=300, label="Sulfate"),
    gr.Slider(0, 1000, value=400, label="Conductivity"),
    gr.Slider(0, 30, value=15, label="Organic Carbon"),
    gr.Slider(0, 150, value=60, label="Trihalomethanes"),
    gr.Slider(0, 10, value=4, label="Turbidity")
]

app = gr.Interface(
    fn=predict_potability,
    inputs=inputs,
    outputs="text",
    title="Water Quality Prediction"
)

app.launch(share=True)