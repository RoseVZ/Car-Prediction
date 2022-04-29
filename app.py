
from crypt import methods

from flask import Flask, render_template, request, url_for, redirect

import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

import os

app = Flask(__name__)

model = pickle.load(open("random_forest_regression.pkl","rb"))
standard_to = StandardScaler()

@app.route('/', methods= ['GET', 'POST'])
def home():
    
    if request.method=='POST':
        Fuel_Type_Diesel=0
        Fuel_Type_Petrol=0
        Kms_Driven = int(request.form["kms"])
        Owner=int(request.form["Owners"])
        Present_Price = request.form["sp"]
        No_Year=2022-int(request.form["Year"])
        if request.form["fuel"] == "Petrol":
            Fuel_Type_Petrol=1
        elif request.form["fuel"] == "Diesel":
            Fuel_Type_Diesel=1
        if request.form["SellType"] == "Individual":
            Seller_Type_Individual=1
        else:
            Seller_Type_Individual=0
        if request.form["Transmission"]=="Manual":
            Transmission_Manual=1
        else:
            Transmission_Manual=0
        prediction=model.predict([[Present_Price,Kms_Driven,Owner,No_Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual]])
      
        return render_template('predict.html', output=prediction)
        
    else:
        
        return render_template('index.html')




if __name__ == "__main__":
    app.run(debug=True)