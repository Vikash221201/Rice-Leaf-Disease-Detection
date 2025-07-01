from flask import Flask, render_template, request, redirect, url_for , session , jsonify
import os
import numpy as np
import tensorflow as tf
from PIL import Image
from werkzeug.utils import secure_filename
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit upload size to 16 MB
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


# Load your trained model
model = tf.keras.models.load_model('our_model.h5' , compile=False)


#class names
'''CLASS_NAMES = ['Bacterial Leaf Blight',
 'Brown Spot',
 'Healthy Rice Leaf',
 'Leaf Blast',
 'Leaf scald',
 'Narrow Brown Leaf Spot',
 'Neck_Blast',
 'Rice Hispa',
 'Sheath Blight']'''
 
CLASS_NAMES = ['Bacterial leaf blight', 'Brown spot', 'Healthy', 'Hispa', 'Leaf Blast','Leaf smut']
 
disease_info = {
    "Bacterial leaf blight": {
        "remedies": "Use resistant varieties, certified seeds, and ensure proper water management.",
        "medicines": "Apply Streptomycin sulfate (100 ppm) or Copper oxychloride (0.25%).",
        "pesticides": "Not typically needed unless pests are present."
    },
    "Brown spot": {
        "remedies": "Improve field drainage and maintain balanced fertilization.",
        "medicines": "Use Mancozeb or Carbendazim (2g/litre of water).",
        "pesticides": "Not necessary unless insect vectors are involved."
    },
    "Healthy": {
        "remedies": "No action needed. Maintain good agricultural practices.",
        "medicines": "None required.",
        "pesticides": "None required."
    },
    "Hispa": {
        "remedies": "Remove infested leaves and reduce standing water.",
        "medicines": "Apply Chlorpyrifos if infestation is severe.",
        "pesticides": "Use Quinalphos 0.05% or Neem-based bio-pesticides."
    },
    
    "Leaf Blast": {
        "remedies": "Avoid excessive nitrogen; plant at proper spacing.",
        "medicines": "Spray Tricyclazole (0.6g/litre).",
        "pesticides": "Not required unless insect damage is also present."
    },
    "Leaf smut": {
        "remedies": "Avoid excessive use of nitrogen and ensure good drainage.",
        "medicines": "Use Carbendazim (0.1%) spray at early stages.",
        "pesticides": "Generally not required."
    },
} 

 
import os
import numpy as np

#dataset_path = "G:/Rice_leaf_disease_detection_using_CNN/mridul da analysis/adam0.001copied/perfectly predicting model/6classdataset/dataset"

#class_counts = {class_name: len(os.listdir(os.path.join(dataset_path, class_name))) 
                #for class_name in os.listdir(dataset_path)}

#print("Class Distribution:", class_counts)





def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(image_path):
    #image = Image.open(image_path)

    # Ensure the image is in RGB format (removing the alpha channel if it exists)
    #image = image.convert("RGB")  # Convert RGBA to RGB

    # Resize the image to match the model's expected input shape
    #target_size = (model.input_shape[1], model.input_shape[2])  # Extract height & width from model
    #image = image.resize((350, 350))

    # Convert to numpy array and normalize
    #image_array = np.array(image) 
    #image_array = tf.keras.preprocessing.image.img_to_array(image)
    #remove below code if needed
    #image_array = np.expand_dims(image_array, axis=0)
    # Convert to numpy array and normalize
    #image_array = image_array / 255.0  # Normalize pixel values to [0,1]
    # Ensure proper shape: Add a channel dimension if missing
    
    
    
    img = image.load_img(image_path, target_size=(350, 350))  # Adjust size based on model requirements
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Normalize if required
    preds = model.predict(img_array)
    return preds
    
    
    
    #if len(image_array.shape) == 2:  # Grayscale image
        #image_array = np.expand_dims(image_array, axis=-1)  # Add channel axis

    # Flatten the image if the model expects 1D input
    #if len(model.input_shape) == 2:  
        #image_array = image_array.flatten()  # Convert to (height * width * channels,)

    # Add batch dimension
    #return image_array













# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index01.html')

@app.route('/model')
def model_page():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            session['image_path'] = file_path  # Store image path in session
            return render_template('predict.html', image_path=file_path)
    return render_template('predict.html')

@app.route('/publications')
def publications():
    return render_template('Publication.html')

@app.route('/Team_members')
def Team_members():
    return render_template('Team_members.html')

@app.route('/Contact_us')
def Contact_us():
    return render_template('Contact.html')



@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return redirect(url_for('home'))

    file = request.files['file']
    if file and allowed_file(file.filename):
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Preprocess the image and make predictions
        #image_tensor = preprocess_image(file_path)
        predictions = preprocess_image(file_path)
        a=predictions[0]
        ind = np.argmax(a)
        print('Prediction result:', CLASS_NAMES[ind])
        result = CLASS_NAMES[ind]
        print("The result is",result)
        print("Prediction Scores:", predictions[0])
        print("Raw Prediction Scores:", predictions)  # Print raw probabilities
        predicted_class_index = np.argmax(predictions[0])
        predicted_class = np.argmax(predictions, axis=1)[0]
        print("Predicted Class Index:", predicted_class_index)
        print("Predicted Class Name:", CLASS_NAMES[predicted_class_index])
        print("Predicted Class Name again:", CLASS_NAMES[predicted_class])
        print("Model Input Shape:", model.input_shape)

        predicted_class_index = np.argmax(predictions[0])

        if predicted_class_index < len(CLASS_NAMES):
            predicted_class = CLASS_NAMES[predicted_class_index]
        else:
            predicted_class = "Unknown Disease"
            
        info = disease_info.get(predicted_class, {
            "remedies": "No specific remedy found.",
            "medicines": "No specific medicine available.",
            "pesticides": "No specific pesticide advised."
        })

        return render_template('result.html', 
                               disease=predicted_class,
                               remedies=info["remedies"],
                               medicines=info["medicines"],
                               pesticides=info["pesticides"])
        
@app.route('/result')
def result():
    disease = request.args.get('disease', 'Unknown')
    remedies = request.args.get('remedies', 'No remedies available.')
    medicines = request.args.get('medicines', 'No medicines suggested.')
    pesticides = request.args.get('pesticides', 'No pesticides suggested.')

    return render_template('result.html', disease=disease, remedies=remedies, medicines=medicines, pesticides=pesticides)



if __name__ == '__main__':
    app.run(debug=True)