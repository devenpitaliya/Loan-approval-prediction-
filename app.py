from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('loan_appruval_lr_model.pkl', 'rb'))


@app.route('/', methods=['GET'])
def Home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        income = int(request.form['income'])
        co_income = int(request.form['co_income'])
        loan_amount = int(request.form['loan_amount'])
        loan_amount_term = int(request.form['loan_amount_term'])

        credit_history = request.form['credit_history']
        if (credit_history == 'credit_history_yes'):
            credit_history = 1
        else:
            credit_history = 0

        Gender = request.form['Gender']
        if (Gender == 'male'):
            Gender = 1
        else:
            Gender = 0

        married = request.form['married']
        if (married == 'married'):
            married = 1
        else:
            married = 0

        Dependant = request.form['Dependant']
        if (Dependant == 'one'):
            Dependents_1 = 1
            Dependents_2 = 0
            Dependents_3 = 0
        elif (Dependant == 'two'):
            Dependents_1 = 0
            Dependents_2 = 1
            Dependents_3 = 0
        elif (Dependant == 'three'):
            Dependents_1 = 0
            Dependents_2 = 0
            Dependents_3 = 1
        else:
            Dependents_1 = 0
            Dependents_2 = 0
            Dependents_3 = 0

        Graduated = request.form['Graduated']
        if (Graduated == 'not_Graduated'):
            Graduated = 1
        else:
            Graduated = 0

        Employed = request.form['Employed']
        if (Employed == 'self_Employed'):
            Employed = 1
        else:
            Employed = 0

        property_area = request.form['property_area']
        if (property_area == 'semi_urban'):
            semi_urban = 1
            urban = 0
        elif (property_area == 'urban'):
            semi_urban = 0
            urban = 1
        else:
            semi_urban = 0
            urban = 0

        prediction = model.predict([[income, co_income, loan_amount, loan_amount_term, credit_history,
                                     Gender, married, Dependents_1, Dependents_2 ,
                                     Dependents_3,  Graduated, Employed, semi_urban , urban]])[0]

        return render_template('result.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True, port=9090)
