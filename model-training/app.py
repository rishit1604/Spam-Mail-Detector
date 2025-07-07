import joblib
from flask import Flask, request, jsonify
from collections import Counter
from flask_cors import CORS
# Load models and vectorizer
LRmodel = joblib.load('logistic_model.pkl')
NBmodel = joblib.load('naive_bayes_model.pkl')
SVMmodel = joblib.load('svm_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

app = Flask(__name__)
CORS(app)
@app.route('/predict', methods=["POST"])
def predict():
    data = request.json
    email = data.get('email', '')
    
    # Convert email text to vector
    email_features = vectorizer.transform([email])
    
    # Get predictions from each model
    predictions = [
        SVMmodel.predict(email_features)[0],
        NBmodel.predict(email_features)[0],
        LRmodel.predict(email_features)[0]
    ]
    
    spam_cout = predictions[0]+predictions[1]+predictions[2]
    
    # Return JSON response
    return jsonify({"isSpam": bool(spam_cout>=2)})

if __name__ == "__main__":
    app.run(debug=True)
