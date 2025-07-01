import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import h5py
from flask import Flask, request, render_template, redirect, url_for, session
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit upload size to 16 MB
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


import os

'''file_path = r'G:\Rice_leaf_disease_detection_using_CNN\rice_disease_detection_webpage\adam0.001copied.h5'
if os.path.exists(file_path):
    print("✅ Model file found!")
else:
    print("❌ Model file NOT found! Check the path.")'''


'''
# Load your trained model
model = tf.keras.models.load_model('adam0.001copied.h5')

#class names
CLASS_NAMES = ['Bacterial leaf blight','Brown spot','Healthy', 'Hispa', 'Leaf Blast', 'Leaf smut']

'''


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

'''

def preprocess_image(image_path):
    image = Image.open(image_path)

    # Convert to grayscale if the model expects 1 channel
    if model.input_shape[-1] == 1:  
        image = image.convert('L')  # Convert to grayscale

    # Resize the image to match the model's expected input shape
    target_size = (model.input_shape[1], model.input_shape[2])  # Extract height & width from model
    image = image.resize(target_size)

    # Convert to numpy array and normalize
    image_array = np.array(image) / 255.0  # Normalize pixel values to [0,1]

    # Ensure proper shape: Add a channel dimension if missing
    if len(image_array.shape) == 2:  # Grayscale image
        image_array = np.expand_dims(image_array, axis=-1)  # Add channel axis

    # Flatten the image if the model expects 1D input
    if len(model.input_shape) == 2:  
        image_array = image_array.flatten()  # Convert to (height * width * channels,)

    # Add batch dimension
    return np.expand_dims(image_array, axis=0)

'''


@app.route('/')
def home():
    """Load the navigation page first"""
    return render_template('nav.html')





@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            session['image_path'] = file_path  # Store image path in session
            return render_template('index.html', image_path=file_path)
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    image_path = session.get('image_path')
    if not image_path:
        return redirect(url_for('index'))

    
    '''
    # Preprocess the image and make predictions
    image_tensor = preprocess_image(image_path)
    predictions = model.predict(image_tensor)

    # Get the predicted class index
    predicted_class_index = np.argmax(predictions[0])

    # Map index to class name
    if predicted_class_index < len(CLASS_NAMES):
        predicted_class = CLASS_NAMES[predicted_class_index]
    else:
        predicted_class = "Unknown Disease"

    # Return prediction result
    result = {
        'disease': predicted_class,
        'remedies': 'Apply recommended treatments based on disease.',
        'medicines': 'Use appropriate fungicides or bactericides.',
        'pesticides': 'Apply eco-friendly pesticides if necessary.'
    }
    print("Raw Predictions:", predictions)
    print("Predicted Class Index:", predicted_class_index)
    print("Model Input Shape:", model.input_shape)
    '''

    return render_template('result.html')  #(add this later into function ), result=result, image_path=image_path)

if __name__ == '__main__':
    app.run(debug=True)
