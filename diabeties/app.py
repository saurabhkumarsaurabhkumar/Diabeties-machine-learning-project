import numpy as np
from flask import Flask,request,render_template
import pickle
from sklearn.externals import joblib
model=joblib.load("Model.pkl")
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login',methods=['POST'])
def login():
    if request.method=='POST':
        Pre=int(request.form['Pregnancies'])
        glu=int(request.form['Glucose'])
        blood=int(request.form['BloodPressure'])
        skin=int(request.form['SkinThickness'])
        insu=int(request.form['Insulin'])
        bmi=float(request.form['BMI'])
        diabeties=float(request.form['DiabetesPedigreeFunction'])
        age=int(request.form['Age'])



    prediction=model.predict([[Pre,glu,blood,skin,insu,bmi,diabeties,age]])
    output=bool(prediction)
    return render_template('index.html',prediction_text='This human have diabeties:{}'.format(output))




if __name__=="__main__":
    app.run(debug=True)

