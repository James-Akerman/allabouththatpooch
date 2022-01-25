from flask import Flask, render_template, request
import boto3
from werkzeug.utils import secure_filename
from captions_generator import captions
import os
from io import BytesIO
from PIL import Image
import json

# Build the machine model
from keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions, ResNet50

app = Flask(__name__)

# Set the port
port = int(os.environ.get("PORT", 5000))

prediction_model = ResNet50()

@app.route('/')  
def home():
    # Return Default Values
    return render_template("index.html", image_link="", name="Your picture's name", image_cap="Get your caption!", breed="Guess what breed your pooch is!")

# Send the json data to logic.js
@app.route("/data")
def json_data():
    # Load the data
    with open('static/data/data.json') as file:
        file_data = json.load(file)
    return json.dumps(file_data)

@app.route("/mtop10")
def mtop10():
    # Load the data
    with open('static/data/mtop10.json') as file:
        file_data = json.load(file)
    return json.dumps(file_data)

@app.route("/mbottom10")
def mbottom10():
    # Load the data
    with open('static/data/mbottom10.json') as file:
        file_data = json.load(file)
    return json.dumps(file_data)

@app.route("/ftop10")
def ftop10():
    # Load the data
    with open('static/data/ftop10.json') as file:
        file_data = json.load(file)
    return json.dumps(file_data)

@app.route("/fbottom10")
def fbottom10():
    # Load the data
    with open('static/data/fbottom10.json') as file:
        file_data = json.load(file)
    return json.dumps(file_data)


@app.route('/upload',methods=['post'])
def upload():

    # Set AWS variables
    access_key = os.environ.get('AWS_ACCESS_KEY_ID', None)
    secret_key = os.environ.get('AWS_SECRET_KEY', None)

    s3 = boto3.client('s3',
                    aws_access_key_id=access_key,
                    aws_secret_access_key=secret_key,
                     )

    BUCKET_NAME='image-cap-assets'
    BUCKET_PATH = "https://image-cap-assets.s3.ap-southeast-2.amazonaws.com/"


    if request.method == 'POST':
        img = request.files['file']
        if img:
                filename = secure_filename(img.filename)
                # Push the image to AWS s3
                s3.upload_fileobj(
                    img,
                    Bucket=BUCKET_NAME,
                    Key=filename,
                    ExtraArgs={'ContentType': 'image/jpeg'}
                )
                image_path = BUCKET_PATH + filename
                # Azure Image Caption Generator
                caps = captions(image_path).capitalize()

                # Keras Classifier model prediction
                file_byte_string = s3.get_object(Bucket=BUCKET_NAME, Key=filename)['Body'].read()
                image = Image.open(BytesIO(file_byte_string))
                image = image.resize((224,224))
                image = img_to_array(image)
                image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
                image = preprocess_input(image)
                yhat = prediction_model.predict(image)
                label = decode_predictions(yhat)
                label = label[0][0]
                classification = '%s (%.2f%%)' % (label[1], label[2]*100)


    return render_template("index.html", image_link=image_path, name=filename,image_cap=caps,breed=classification)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, debug=True)