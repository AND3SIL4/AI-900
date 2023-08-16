import requests

# Declaración de variables
prediction_url = "YOUR_PREDICTION_URL"
prediction_key = "YOUR_PREDICTION_KEY"

# Código para llamar al servicio Custom Vision para la clasificación de imágenes
img_num = 1
if len(sys.argv) > 1 and int(sys.argv[1]) in range(1, 4):
    img_num = int(sys.argv[1])

img = f"https://raw.githubusercontent.com/MicrosoftLearning/AI-900-AIFundamentals/main/data/vision/animals/animal-{img_num}.jpg"

headers = {
    "Prediction-Key": prediction_key,
    "Content-Type": "application/json"
}

body = {
    "url": img
}

print("Analyzing image...")
response = requests.post(prediction_url, headers=headers, json=body)
prediction = response.json()

print(f"\n{prediction['predictions'][0]['tagName']}\n")
