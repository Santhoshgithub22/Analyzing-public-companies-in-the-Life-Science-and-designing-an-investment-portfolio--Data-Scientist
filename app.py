from flask import Flask,render_template,request
import pickle
import sklearn
import numpy as np
import pandas as pd
app = Flask(__name__)

filename = "rfc_model.pkl"
with open(filename, 'rb') as file:
    model = pickle.load(file)

@app.route("/")
def home():
    return render_template(["index.html"])

@app.route("/predict",methods = ["GET","POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    pred = model.predict([np.array(float_features)])
    if pred[0] == 0:
        result = "Opps, the Stock will be in Loss"
    else:
        result = "Congratulations the Stock will be in Profit"

    return render_template("predict.html",prediction = result)




if __name__ == "__main__":
    app.run(debug = True)