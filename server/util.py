import pickle
import json
import pandas as pd

__data_columns = None
__model = None

def get_loan_status(Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area):
    data = [Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]
    df = pd.DataFrame([data],columns = __data_columns)
    cat_columns = df.select_dtypes(include='object').columns.tolist()
    for c in cat_columns:
        df[c] = df[c].astype('category')
    pred = __model.predict(df)
    if pred >= 0.5:
        return 'Loan Approved'
    else:
        return 'Loan Rejected' 


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']

    global __model
    if __model is None:
        with open('./artifacts/Loan_data_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")


def get_data_columns():
    return __data_columns

#if __name__ == "__main__":
load_saved_artifacts()
    #print(get_loan_status('Male','No','0','Not Graduate','No',3748,1668.0, 110.0, 360.0, 1.0, 'Semiurban'))