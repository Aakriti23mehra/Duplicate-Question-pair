from flask import Flask, request, jsonify, render_template
import pickle
import helper

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = pickle.load(open(r'C:\Users\mehra\Downloads\model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')  # Create a basic index.html in 'templates' folder

@app.route('/predict', methods=['POST'])
def predict():
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')

    if not q1 or not q2:
        return render_template('index.html', prediction='Please enter both questions.')

    query = helper.query_point_creator(q1, q2)
    result = model.predict(query)[0]

    prediction = 'Duplicate' if result else 'Not Duplicate'
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
