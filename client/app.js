
function onClickedPredictLoanStatus() {
  console.log("Predict Loan Status button clicked");
  var gender = document.getElementById("uigender");
  var married = document.getElementById("uimarried");
  var dependents = document.getElementById("uidependents");
  var education = document.getElementById("uieducation");
  var self_employed = document.getElementById("uiself_employed");
  var applicantincome = document.getElementById("uiapplicantincome");
  var coapplicantincome = document.getElementById("uicoapplicantincome");
  var loanamount = document.getElementById("uiloanamount");
  var loan_amount_term = document.getElementById("uiloan_amount_term");
  var credit_history = document.getElementById("uicredit_history");
  var property_area = document.getElementById("uiproperty_area");
  var predictedloanstatus = document.getElementById("uipredictedloanstatus");

  var url = "/predict_loan_status"; //Use this if you are NOT using nginx which is first 7 tutorials
  //var url = "/api/predict_loan_status"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

  $.post(url, {
	  gender : gender.value,
	  married : married.value,
	  dependents : dependents.value,
	  education : education.value,
	  self_employed : self_employed.value,
	  applicantincome : parseInt(applicantincome.value),
	  coapplicantincome : parseFloat(coapplicantincome.value),
	  loanamount : parseFloat(loanamount.value),
	  loan_amount_term : parseFloat(loan_amount_term.value),
	  credit_history : parseFloat(credit_history.value),
	  property_area : property_area.value,
  },
  function(data, status) {
      console.log(data.loan_status);
      predictedloanstatus.innerHTML = "<h2>" + data.loan_status.toString() + "</h2>";
      console.log(status);
  });
}