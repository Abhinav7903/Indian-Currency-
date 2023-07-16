const video = document.getElementById('video');
const stopButton = document.getElementById('stop-button');
const prediction = document.getElementById('prediction');

// Load the model
let model;
mobilenet.load().then(m => {
  model = m;
});

// Start the webcam stream
navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => {
    video.srcObject = stream;
  })
  .catch(err => {
    console.log(`Error: ${err}`);
  });

// Stop the webcam stream
stopButton.onclick = () => {
  video.srcObject.getTracks().forEach(track => {
    track.stop();
  });
};

// Make predictions
setInterval(() => {
  // Check if the model has been loaded
  if (model) {
    // Capture the current frame of the video stream
    const imageCapture = new ImageCapture(video);
    imageCapture.grabFrame().then(imageBitmap => {
      // Resize the image
      const tfImage = tf.browser.fromPixels(imageBitmap).resizeNearestNeighbor([224, 224]);
      // Normalize the pixel values
      const tfImageNormalized = tfImage.div(255.0);
      // Add a batch dimension
      const tfImageBatched = tfImageNormalized.expandDims(0);
      // Make the prediction
      model.classify(tfImageBatched).then(predictions => {
        prediction.innerHTML = `Predicted currency: ${predictions[0].className}`;
      });
    });
  }
}, 1000);
