import numpy as np
import joblib


def preprocessdata(Gender, Married, Education, Self_Employed, ApplicantIncome,
                   CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,
                   Property_Area):
    test_data = [[Gender, Married, Education, Self_Employed, ApplicantIncome,
                  CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,
                  Property_Area]]
    trained_model = joblib.load("model.pkl")
    prediction = trained_model.predict(test_data)
    CoapplicantIncome = int(CoapplicantIncome)
    ApplicantIncome = int(ApplicantIncome)
    Loan_Amount_Term = int(Loan_Amount_Term)
    LoanAmount = int(LoanAmount)
    a = (0.05*CoapplicantIncome)+(0.1*ApplicantIncome)
    a = a*Loan_Amount_Term
    if a < (0.73*LoanAmount):
        q = 0
        return q

    return prediction
