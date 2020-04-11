from flask import Flask, request, jsonify, render_template
import utils
import os
from werkzeug.utils import secure_filename





app = Flask(__name__)


@app.route('/')
def home() :
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    url = request.form['URL']
    prediction_text = 'predicted flare : ' + utils.model_prediction(url)
    return render_template('index.html',prediction_text= prediction_text)

@app.route('/automated_testing',methods=['POST'])
def automated_testing():
    r = request.files['']
    filename = secure_filename(r.filename)

    r.save(os.path.join('uploaded_data',filename))

    with open('uploaded_data/'+filename,'r') as f:
        data = f.read()
        ret_val = dict()
        for i in data.split():
            prediction = utils.model_prediction(i)
            ret_val[i] = prediction
        return jsonify(ret_val)

    return "donononnonn"


if(__name__)=='__main__':
    app.run()
