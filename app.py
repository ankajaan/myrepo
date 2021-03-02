from flask import Flask, jsonify, request, render_template, session

app = Flask(__name__)
app.secret_key = "anks"
contacts_list = [
    {
        "id": 1,
        "name": "Aayisha",
        "city": "Kollam",
        "contact": "9123456789"
    },
    {
        "id": 2,
        "name": "Athira",
        "city": "Calicut",
        "contact": "9123459789"
    },
    {
        "id": 3,
        "name": "Jiss Theresa",
        "city": "Alapuzha",
        "contact": "9123457789"
    }
]


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template("login.html")


@app.route("/enter", methods=["POST"])
def enter():
    if request.method == "POST":
        session["email"] = request.form.get("email")
    return render_template("enter.html")


'''
@app.route("/contacts_list")
def contacts_list():
    if "email" in session:
        return render_template("contacts_list.html", contacts=enumerate(get_contacts()))
    else:
        return "<p>Please Login first</p>"
'''


@app.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email', None)
        return render_template('logout.html')
    else:
        return '<p>User already logged out</p>'


'''
def get_contacts():
    return contacts_list


@app.route("/new")
def new():
    return render_template("new.html")


@app.route("/add", methods=["POST"])
def add_contact():
    id = request.form.get("id")
    name = request.form.get("name")
    city = request.form.get("city")
    contact = request.form.get("contact")
    details = {
        "id": id,
        "name": name,
        "city": city,
        "contact": contact
    }
    contacts_list.append(details)
    return render_template("contacts_list.html", contacts=enumerate(get_contacts()))

'''


@app.route('/profile')
def profile():
    if 'email' in session:
        email = session['email']
        return render_template('profile.html', name=email)
    else:
        return '<p>Please login first</p>'


if __name__ == "__main__":
    app.run(debug=True)
