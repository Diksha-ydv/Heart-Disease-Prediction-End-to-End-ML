from flask import Flask,request,render_template
from src.pipeline.predict_pipeline import predict,predict_datapnt

application = Flask(__name__)
app = application 

@app.route("/",methods=["GET","POST"])
def predict_datapoint():
    if request.method=="GET":
        return render_template("home.html",results=None)
    else:
        Age=request.form.get("Age")
        Sex=request.form.get("Sex")
        ChestPainType=request.form.get("ChestPainType")
        RestingBP=request.form.get("RestingBP")
        Cholesterol=request.form.get("Cholesterol")
        FastingBS=request.form.get("FastingBS")
        RestingECG=request.form.get("RestingECG")
        MaxHR=request.form.get("MaxHR")
        ExerciseAngina=request.form.get("ExerciseAngina")
        Oldpeak=request.form.get("Oldpeak")
        ST_Slope = request.form.get("ST_Slope")

        predict_data_obj = predict_datapnt(Age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,Oldpeak,ST_Slope)
        data = predict_data_obj.csv_to_dataframe()
        print(data)

        predict_obj = predict()
        value = predict_obj.pred_val(data)


        if value == 1:
            result = "High Risk of Heart Disease"
        else:
            result = "Low Risk of Heart Disease"

        print("Prediction:", value)


        return render_template(
            "home.html",
            results=result
        )
if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=8000)
