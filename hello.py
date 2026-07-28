from flask import Flask, request, redirect, render_template,session


import mysql.connector

app = Flask(__name__,  template_folder="templates",
            static_folder="static")
app.secret_key="healinghands"
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",      # XAMPP default
    database="Healing_hands"
)

print("Database Connected Successfully!")

@app.route('/')
def home():
    return render_template("Healing_hands.html")

@app.route('/register', methods=['GET'])
def register_page():
    return render_template("register.html")

@app.route('/register', methods=['POST'])
def register():

    full_name = request.form['full_name']
    email = request.form['email']
    password = request.form['password']

    cursor = db.cursor()

    sql = """
    INSERT INTO register(full_name, email, User_password)
    VALUES (%s, %s, %s)
    """

    values = (full_name, email, password)

    cursor.execute(sql, values)
    db.commit()

    return redirect("/login")



@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']


        cursor = db.cursor()

        sql = """SELECT * FROM register WHERE email=%s AND User_password=%s"""

        cursor.execute(sql, (email, password))

        user = cursor.fetchone()

        if user:
            session['user']=email
            insert_sql = """ INSERT INTO login(email, User_password, Date_and_time) VALUES (%s, %s, NOW()) """

            cursor.execute(insert_sql, (email, password))
            db.commit()

            return redirect("/")
        else:
            return "Invalid Email or Password"

    return render_template("login.html")

@app.route('/appointment', methods=['GET', 'POST'])
def appointment():

    if 'user' not in session:
        return redirect('/login')

    if request.method == 'POST':

        username = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        service = request.form['service']
        date = request.form['date']
        time = request.form['time']
        note = request.form['message']

        cursor = db.cursor()

        sql = """
        INSERT INTO appointment
        (UserName, email, phone_number, services,
        date_of_appointment, time_of_appointment, note)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            username,
            email,
            phone,
            service,
            date,
            time,
            note
        )

        cursor.execute(sql, values)
        db.commit()

        return redirect("/")

    return render_template("appointment1.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():

    if 'user' not in session:
        return redirect('/login')

    if request.method == 'POST':

        username = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        subject = request.form['subject']
        message = request.form['message']

        cursor = db.cursor()

        sql = """
INSERT INTO contact
(user_Name, email, phone_number, sub, queries)
VALUES (%s, %s, %s, %s, %s)
"""

        values = (
            username,
            email,
            phone,
            subject,
            message
        )

        cursor.execute(sql, values)
        db.commit()

        return redirect("/")

    return render_template("contact_us.html")
@app.route('/about')
def about():
    return render_template("about_us.html")

@app.route('/services')
def services():
    return render_template("services_by_us.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)  