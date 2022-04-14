import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'age':45, 'sex':'1', 'cp':2 ,'trestbps': 150, 'chol': 387, 'fbs':1,
                            'restecg':0,'thalach':139, 'exang':1, 'oldpeak':2.9, 'slope':1,
                            'ca':1,'thal':6})


