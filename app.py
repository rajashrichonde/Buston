import pandas as pd
import numpy as np
import pickle
import json
import config

class BostonHouseprices():
    
    def __init__(self,CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT):
        
        self.CRIM=CRIM
        self.ZN=ZN
        self.INDUS=INDUS
        self.CHAS=CHAS
        self.NOX=NOX
        self.RM=RM
        self.AGE=AGE
        self.DIS=DIS
        self.RAD=RAD
        self.TAX=TAX
        self.PTRATIO=PTRATIO
        self.B=B
        self.LSTAT=LSTAT
        
    def load_model(self):
        
        with open(config.MODEL_FILE_PATH,"rb") as f :
            self.lr_model=pickle.load(f)
        print("model_file_loaded")
        with open(config.JSON_FILE_PATH,"r") as f:
            self.json_data=json.load(f)
        print("json file loaded")
            
    def get_predict_house_price(self):
        self.load_model()
        test_array=np.zeros(len(self.json_data["columns"]))
        test_array[0]=self.CRIM
        test_array[1]=self.ZN
        test_array[2]=self.INDUS
        test_array[3]=self.CHAS
        test_array[4]=self.NOX
        test_array[5]=self.RM
        test_array[6]=self.AGE
        test_array[7]=self.DIS
        test_array[8]=self.RAD
        test_array[9]=self.TAX
        test_array[10]=self.PTRATIO
        test_array[11]=self.B
        test_array[12]=self.LSTAT
        
        print("Test_array",test_array)
        prediction_charges=self.lr_model.predict([test_array])[0]
        
        return prediction_charges
        
        


