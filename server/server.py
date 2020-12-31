from flask import Flask, request, jsonify, render_template
import server.util as util
#import util

app = Flask(__name__, static_url_path="/client", static_folder='../client', template_folder="../client")

@app.route('/', methods=['GET'])
def index():
    if request.method=="GET":
        return render_template("app.html")


@app.route('/predict_loan_status', methods=['GET', 'POST'])
def predict_loan_status():
    Gender = request.form['gender']
    Married = request.form['married']
    Dependents = request.form['dependents']
    Education = request.form['education']
    Self_Employed = request.form['self_employed']
    ApplicantIncome = int(request.form['applicantincome'])
    CoapplicantIncome = float(request.form['coapplicantincome'])
    LoanAmount  = float(request.form['loanamount'])
    Loan_Amount_Term = float(request.form['loan_amount_term'])
    Credit_History = float(request.form['credit_history'])
    Property_Area = request.form['property_area']
    
    response = jsonify(
        {'loan_status': 
         util.get_loan_status(Gender,Married,
                              Dependents,Education,Self_Employed,
                              ApplicantIncome,CoapplicantIncome,
                              LoanAmount,Loan_Amount_Term,
                              Credit_History,Property_Area)
         })
    response.headers.add('Access-Control-Allow-Origin', '*')
    
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Loan Status Prediction...")
    app.run()
