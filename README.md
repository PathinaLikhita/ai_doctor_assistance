
# 🩺 AI Doctor Assistant

An intelligent web application that predicts possible diseases based on user-inputted symptoms. It features a user authentication system, symptom analysis, disease prediction using a trained ML model, and a diagnosis history dashboard.

## 👩‍💻 Team Members
- **Pathina Likhita** - [likhithapathina@gmail.com](mailto:likhithapathina@gmail.com)
- **Guruvu Jagadeswari** - Jagadeeswari719
- **Pyla Nalini** - [nalini7072@gmail.com](mailto:nalini7072@gmail.com)

---

## 🚀 Features
- 🔐 User Registration and Login
- 💡 Symptom-based Disease Prediction using Machine Learning
- 📊 Diagnosis History with Timestamps
- 🎨 Clean, user-friendly Bootstrap UI
- 🧠 Trained Model integrated via Flask
- 🗃️ SQLite for local storage

---

## 🛠️ Technologies Used
- **Frontend**: HTML, CSS (Bootstrap), Jinja2 Templates
- **Backend**: Flask, Python
- **Database**: SQLite
- **ML Model**: Scikit-learn
- **Authentication**: Flask-Login

---

## 📁 Project Structure

```
ai_doctor_assistant/
│
├── templates/             # HTML templates
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│
├── static/                # Static assets (CSS, JS, Images)
│
├── models.py              # SQLAlchemy models
├── utils/
│   └── logic.py           # Disease prediction logic
│
├── auth.py                # Authentication Blueprint
├── main.py                # Main views Blueprint
├── app.py                 # Flask app entry point
├── doctor.db              # SQLite database
├── train_model.py         # ML model training script
├── model.pkl              # Trained ML model
└── requirements.txt
```

---

## 🧪 How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/ai_doctor_assistant.git
   cd ai_doctor_assistant
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```

4. **Train the Model (if not already trained)**
   ```bash
   python train_model.py
   ```

5. **Run the App**
   ```bash
   python app.py
   ```

6. **Access in Browser**
   Open [http://localhost:5000](http://localhost:5000)

---

## 📝 Notes
- Ensure `model.pkl` is generated via `train_model.py`.
- Use `doctor.db` for preloaded database or run fresh migrations.

---

## 📌 License
This project is for educational purposes only. All rights reserved to the original authors.

---

## ❤️ Acknowledgements
Thanks to our mentors, open-source contributors, and the Flask + ML communities!
