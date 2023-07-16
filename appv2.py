from flask import Flask, render_template, request
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np
import pyttsx3

app = Flask(__name__)
# model = load_model('model_classifier.h5')
model=load_model('C:/abhinav/Proj/model_classifier.h5')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    img = request.files['image']
    img_path = 'static/' + img.filename
    img.save(img_path)

    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    pred = model.predict(x)
    result = np.argmax(pred, axis=1)

    denominations = {
        0 : "hundred", 
        1: "two hundred",
        2: "two thousand",
        3: "five hundred",
        4: "fifty",
        5: "ten",
        6: "twenty"
    }
     # Initialize the pyttsx3 engine
    prediction = denominations[result[0]]

    engine = pyttsx3.init()
    
    # Set the speed and volume of the speech
    engine.setProperty('rate', 100)
    engine.setProperty('volume', 0.8)
    
    # Speak the predicted denomination
    engine.say("This is " + prediction+"ruppe note")
    engine.runAndWait()

    prediction = denominations[result[0]]
    return render_template('index.html', prediction=prediction, img_path=img_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
