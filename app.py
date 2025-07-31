from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required, current_user
from models import db, User, DiagnosisHistory
from utils.logic import predict_disease
from auth import auth
from pytz import timezone, UTC

app = Flask(__name__)
app.secret_key = 'secret123'  # Use environment variable in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///doctor.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize DB
db.init_app(app)

# Register Blueprint
app.register_blueprint(auth)

# Setup Login
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# DB create
with app.app_context():
    db.create_all()

# Routes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diagnose', methods=['POST'])
@login_required
def diagnose():
    checkbox_symptoms = request.form.getlist('symptoms')
    voice_symptoms = request.form.get('voice_symptoms')

    # Combine both inputs
    combined = checkbox_symptoms
    if voice_symptoms:
        combined += [s.strip() for s in voice_symptoms.lower().split(',') if s.strip()]

    symptoms_input = ','.join(combined)
    result = predict_disease(symptoms_input)

    # Save result to DB
    history = DiagnosisHistory(
        user_id=current_user.id,
        symptoms=symptoms_input,
        disease=result["disease"],
        advice=result["advice"],
        emergency=result["emergency"]
    )
    db.session.add(history)
    db.session.commit()

    return render_template('result.html', result=result)

@app.route('/dashboard')
@login_required
def dashboard():
    history = DiagnosisHistory.query.filter_by(user_id=current_user.id)\
        .order_by(DiagnosisHistory.timestamp.desc()).all()

    # Convert UTC to IST
    ist = timezone('Asia/Kolkata')
    for entry in history:
        if entry.timestamp:
            if entry.timestamp.tzinfo is None:
                entry.timestamp = UTC.localize(entry.timestamp).astimezone(ist)
            else:
                entry.timestamp = entry.timestamp.astimezone(ist)

    return render_template('dashboard.html', history=history)

if __name__ == '__main__':
    app.run(debug=True)
