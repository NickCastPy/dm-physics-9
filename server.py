from flask import Flask, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from main import Calculeaza_Perioada_Oscilatiilor

class DataForm(FlaskForm):
    lmbd = StringField('Introduceti Lambda (Lungimea de Unda)')
    T = StringField('Introduceti T (Perioada Oscilatiilor de Unda)')
    submit = SubmitField('Calculeaza')

app = Flask(__name__)
app.secret_key = "rtoypup"

@app.route('/', methods=['POST', 'GET'])
def main():
    form = DataForm()
    if request.method == 'POST':
        result = Calculeaza_Perioada_Oscilatiilor.calculate(request.form['lmbd'], request.form['T'])
        return redirect(f'/{result}')
    return render_template('index.html', form=form)

@app.route('/<result>')
def get_result(result):
    return render_template('result.html', res = result)
if __name__ =='__main__':
    app.run(debug=True, port=5001)