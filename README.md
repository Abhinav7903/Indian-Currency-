# IndianCurrencyDetection
Detection of currency notes using deep learning


Foreign and visually disable people in India often find difficulties in recognizing different currency notes. Even if some time it is also difficult for Indian healthy people to identify same amount of currency notes with different-new designs. Human eye has also some limitation so some time fake currency not identifiable by them. In this paper deep learning model is trained with dataset and is being tested with different Indian currency with good accuracy.

Training the machine to learn to detect and recognize object from given input, so the machine learning is based on what it sees and learns from their image dataset. Therefore, with a good amount of quality images we can improve machine’s learning ability.

## Technologies used :
- Python, Tensorflow, Streamlit

- Dataset is taken from Kaggle

## Files :
- currencydetectionmodel.ipynb :
  - Here we load the data and preprocess the same
  - build the ML deep learning model
  - train the model with the dataset
  - plot graphs for clear understanding
- app.py : 
  - Contains python code for streamlit library
  - Initial display, Uploading image, Displaying result
- img_classification.py :
  - Contains python code to predict the result
  - Takes uploaded image, loads the ML model, Computes

## Building model :
We have used 2 Convolution Layers and a dense layer in our model.
-	Convolution: A Convolution Neural Network have a n numbers of layers which can learn to detect different features from an image data, and the output of each processed image is used as the input to the next layer. It has set of convolutional filters, which find features from images, so images pass through these all filters.

-	Dense: Dense layer is collections of neurons. It describes how neurons connected to the next layer of neurons (In short, each neuron is connected to every neuron in the next layer). It is also known as Fully Connected layer


## How to run the file from cmd :
- Go to the file location
- use the command : Streamlit run app.py

## Result :

The model gives us 
1.	Accuracy - 0.9647
2.	Loss – 0.1195
3.	Validation Accuracy – 0.8730
4.	Validation Loss – 0.5291

## Future scope :

We used Convolution and Dense layers to create our model which helps in detecting Indian Currency accurately to a good extent.
Futher we can add audio files which will tell us the identified currency and can be used to help the visually disabled, foreign and aged people.
