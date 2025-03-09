import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify
from PIL import Image
import pickle

app = Flask(__name__)

MODEL_PATH = "fashion_cnn_model_tensorflow.h5"
model = tf.keras.models.load_model(MODEL_PATH)

with open("label_encoders.pkl", "rb") as f:
    encoders = pickle.load(f)

@app.route("/predict", methods=["POST"])
def prediction():
    if "image" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["image"]
    image = Image.open(file).convert("RGB").resize((224, 224))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)

    predictions = model.predict(image)

    decoded_predictions = {
        "baseColour": encoders["baseColour"].inverse_transform([np.argmax(predictions[0])])[0],
        "articleType": encoders["articleType"].inverse_transform([np.argmax(predictions[1])])[0],
        "season": encoders["season"].inverse_transform([np.argmax(predictions[2])])[0],
        "gender": encoders["gender"].inverse_transform([np.argmax(predictions[3])])[0],
    }

    return jsonify(decoded_predictions)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)  