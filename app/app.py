from flask import Flask, request, render_template
from pickle import load
app = Flask(__name__)
with open('../models/clf_tree_model.pkl', 'rb') as file:
    model = load(file)
class_dict = {'0': 'setosa', '1': 'versicolor', '2': 'virginica'}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=='POST':
        val1 = float(request.form['val1'])
        val2 = float(request.form['val2'])
        val3 = float(request.form['val3'])
        val4 = float(request.form['val4'])
        data = [[val1, val2, val3, val4]]
        prediction = str(model.predict(data)[0])
        pred_class = class_dict[prediction]
    else:
        pred_class = None
    return render_template('app/entry.html', prediction=pred_class)

if __name__ == '__main__':
    app.run(debug=True)