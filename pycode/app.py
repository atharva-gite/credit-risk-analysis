from logging import debug
from flask import Flask, render_template, request
import utils
from utils import preprocessdata

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('final.html')


@app.route('/aprroval')
def approval():
    return render_template('aprroval.html')


@app.route('/decline')
def decline():
    return render_template('decline.html')


@app.route('/predict/', methods=['POST'])
def predict():
    if request.method == 'POST':
        Gender = int(request.form.get('gender'))
        Married = int(request.form.get('martstat'))
        Education = int(request.form.get('edu'))
        Self_Employed = int(request.form.get('empstat'))

        # Check if the form fields have valid values before converting to float
        ApplicantIncome = float(request.form.get(
            'inc')) if request.form.get('inc') else 0.0
        CoapplicantIncome = float(request.form.get(
            'coinc')) if request.form.get('coinc') else 0.0
        LoanAmount = float(request.form.get(
            'amt')) if request.form.get('amt') else 0.0
        Loan_Amount_Term = float(request.form.get(
            'term')) if request.form.get('term') else 0.0
        Credit_History = int(request.form.get(
            'hist')) if request.form.get('hist') else 0
        Property_Area = int(request.form.get(
            'house')) if request.form.get('house') else 0

        prediction = utils.preprocessdata(Gender, Married, Education, Self_Employed, ApplicantIncome,
                                          CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,
                                          Property_Area)

        if prediction == 0:
            return render_template('decline.html')
        else:
            return render_template('aprroval.html')

    return render_template('predict.html')


if __name__ == '__main__':
    app.run(debug=True)
