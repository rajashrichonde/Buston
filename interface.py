from flask import Flask,jsonify
import config
from project_new.app import BostonHouseprices
app=Flask(__name__)


@app.route("/")
def Basic_APT():
    print("Welcome to new world")
    return jsonify({"rajashre":"chonde"})

@app.route("/prediction_price")
def prediction_price_house():
    CRIM =0.00632
    ZN =18.00000
    INDUS =2.31000
    CHAS =0.00000
    NOX =0.53800
    RM =6.57500
    AGE =65.20000
    DIS =4.09000
    RAD =1.00000
    TAX =296.00000
    PTRATIO =15.30000
    B =396.90000
    LSTAT =4.98000

    print("CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT",CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT)
    
    price=BostonHouseprices(CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT)
    
    BostonHouse_prices=price.get_predict_house_price()
    
    return jsonify({"Result":f"Boston house prize is:{BostonHouse_prices}"})
    
    
if __name__=="__main__":
   app.run(debug=True)


