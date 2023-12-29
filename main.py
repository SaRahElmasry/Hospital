from datetime import datetime
from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Configure the MySQL database
DATABASE = {
    'host': 'localhost',
    'database': 'hospital_project',
    'user': 'root',
    'password': '3124166'
}

def get_db():
    db = mysql.connector.connect(**DATABASE)
    return db



@app.route('/')
def index():
    return render_template('main_page.html')

@app.route('/nurse', methods=['GET', 'POST'])
def nurse():
    if request.method == 'POST':
        # Handle form submission for nurse table
        n_id = request.form['id']
        name = request.form['name']
        phone = request.form['phone']
        # Insert data into the nurse table
        db = get_db()
        cursor = db.cursor()
        query = "INSERT INTO nurse (n_id, name, phone) VALUES (%s, %s, %s)"
        values = (n_id, name, phone)

        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()

        return "Data successfully submitted to Nurse table!"

    return render_template('nurse.html')

@app.route('/doctor', methods=['GET', 'POST'])
def doctor():
    if request.method == 'POST':
        # Handle form submission for doctor table
        d_id = request.form['id']
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        specialization = request.form['specialization']
        nurse_id = request.form['nurse_id']

        # Insert data into the doctor table
        db = get_db()
        cursor = db.cursor()
        query = "INSERT INTO doctor (d_id, name, phone, email, specialization, nurse_id) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (d_id, name, phone, email, specialization, nurse_id)

        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()

        return "Data successfully submitted to Doctor table!"

    return render_template('doctor.html')

@app.route('/patient', methods=['GET', 'POST'])
def patient():
    if request.method == 'POST':
        # Handle form submission for patient table
        p_id = request.form['id']
        name = request.form['name']
        phone = request.form['phone']
        gender = request.form['gender']
        street = request.form['street']
        city = request.form['city']
        age = request.form['age']

        # Insert data into the patient table
        db = get_db()
        cursor = db.cursor()
        query = "INSERT INTO patient (p_id, name, phone, gender, street, city, age) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (p_id, name, phone, gender, street, city, age)

        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()

        return "Data successfully submitted to Patient table!"

    return render_template('patient.html')

@app.route('/appointment', methods=['GET', 'POST'])
def appointment():
    if request.method == 'POST':
        # Handle form submission for appointment table
        a_id = request.form['id']
        patient_id = request.form['patient_id']
        doctor_id = request.form['doctor_id']
        a_datetime_str = request.form['datetime']
        # Convert to datetime object
        a_datetime = datetime.strptime(a_datetime_str, '%Y-%m-%dT%H:%M')
        notes = request.form['notes']

        # Insert data into the appointment table
        db = get_db()
        cursor = db.cursor()
        query = "INSERT INTO appointment (a_id, patient_id, doctor_id, a_datetime, notes) VALUES (%s, %s, %s, %s, %s)"
        values = (a_id, patient_id, doctor_id, a_datetime, notes)

        cursor.execute(query, values)
        db.commit()
        cursor.close()
        db.close()

        return "Data successfully submitted to Appointment table!"

    return render_template('appointment.html')

if __name__ == '__main__':
    app.run()
