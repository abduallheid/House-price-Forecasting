from ast import Import
import os
import csv
# from crypt import methods
import re
from urllib import response
import joblib
import pandas as pd
import io
import jsonify
import numpy as np
import requests
from flask import Flask, redirect, render_template, request, send_file, url_for,Response,make_response
from xgboost import cv

app = Flask(__name__,template_folder='templates')



@app.route("/home")

def home():
   
   return render_template('demo.html')

@app.route('/predict',methods=['POST',"GET"])
def predict():

    model = joblib.load('XGB.ml')
  
    price_House = model.predict(np.array([[int(request.args['OverallQual']),
                            int(request.args['GrLivArea']),
                            int(request.args['YearBuilt']),
                            int(request.args['GarageArea']),
                            int(request.args['TotalBsmtSF']),
                            int(request.args['GarageCars']),
                            int(request.args['FirstFlrSF']),                            
                            int(request.args['BsmtQual']),
                            int(request.args['KitchenQual']),
                            int(request.args['ExterQual']),
                            int(request.args['YearRemodAdd']),
                            int(request.args['MSSubClass']),
                            int(request.args['GarageFinish']),
                            int(request.args['FullBath']),
                            int(request.args['Foundation']),
                            int(request.args['LotFrontage']),
                            int(request.args['GarageType']),
                            int(request.args['FireplaceQu']),
                            int(request.args['SecondFlrSF'])
                           ]]))
    output = str(round(price_House[0],2))  
    DATA={"OverallQual":[request.args['OverallQual']],
        "GrLivArea":[request.args['GrLivArea']], 
        "YearBuilt":[request.args['YearBuilt']], 
        "GarageArea":[request.args['GarageArea']], 
        "TotalBsmtSF":[request.args['TotalBsmtSF']], 
        "GarageCars":[request.args['GarageCars']], 
        "FirstFlrSF":[request.args['FirstFlrSF']], 
        "BsmtQual":[request.args['BsmtQual']], 
        "KitchenQual":[request.args['KitchenQual']], 
        "ExterQual":[request.args['ExterQual']], 
        "YearRemodAdd":[request.args['YearRemodAdd']], 
        "MSSubClass":[request.args['MSSubClass']], 
        "GarageFinish":[request.args['GarageFinish']], 
        "FullBath":[request.args['FullBath']], 
        "Foundation":[request.args['Foundation']], 
        "LotFrontage":[request.args['LotFrontage']], 
        "GarageType":[request.args['GarageType']], 
        "Fire0placeQu":[request.args['FireplaceQu']], 
        "SecondFlrSF":[request.args['SecondFlrSF']]

        }
    df=pd.DataFrame(data=DATA)    

# def getPlotCSV():
#     # with open("outputs/Adjacency.csv") as fp:
#     #     csv = fp.read()
#     csv = '1,2,3\n4,5,6\n'
#     return Response(
#         csv,
#         mimetype="text/csv",
#         headers={"Content-disposition":
#                  "attachment; filename=myplot.csv"})


    req = requests.get(df)
    url_content = req.content
    csv_file = open('downloaded.csv', 'wb')

    download=csv_file.write(url_content)
    
    
    



    if request.method =="POST":

        return render_template('demo.html', price='Your house price:$ {}'.format(output))
    else :
        
        return download
    

   
      
if __name__ == "__main__":
    app.run(debug=True)