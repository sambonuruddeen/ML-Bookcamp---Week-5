import pickle
from flask import Flask
from flask import request
from flask import jsonify

model_file = 'model1.bin'
vectorizer = 'dv.bin'

with open(model_file, 'rb') as f_in:
    
    model = pickle.load(f_in)
dv = pickle.load(open(vectorizer, 'rb'))
print('Model Loaded')

app = Flask('Churn')

customer = {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0,1]
    churn =  y_pred >= 0.5

    result = {
        'churn_probability': float(y_pred),
        'churn': bool(churn)

    }

    return jsonify(result)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)

