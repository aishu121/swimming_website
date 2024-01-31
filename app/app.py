from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates',static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://sushmithabanda@localhost:5432/sushmithabanda"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    experience = db.Column(db.String(100), nullable=True)

with app.app_context():
    db.create_all()

@app.route('/', endpoint='registration')
def index():
    return render_template('registration_form.html')

@app.route('/details', endpoint='form_details', methods=['GET', 'POST'])
def get_results():
    if request.method == 'POST':
        full_name = request.form.get('fullName')

        if full_name:
            user = Registration.query.filter_by(full_name=full_name).first()

            if user:
                return render_template('form_details.html', user=user)
            else:
                return render_template('form_details.html', error='User not found')

    # If it's a GET request or the form is not submitted yet
    return render_template('form_details.html')
# @app.route('/', endpoint='registration_form')
# def registration():
#     return render_template('registration_form.html')

@app.route('/home', endpoint='home')
def home():
    return render_template('home.html')

@app.route('/contactus', endpoint='contactus')
def contactus():
    return render_template('contactus.html')

@app.route('/find_details', endpoint='find_details')
def find_details():
    return render_template('find_details.html')

@app.route('/resources', endpoint='resources')
def resources():
    return render_template('resources.html')

@app.route('/get_started', endpoint='get_started')
def resources():
    return render_template('get_started.html')


if __name__ == '__main__':
    app.run(debug=True)
