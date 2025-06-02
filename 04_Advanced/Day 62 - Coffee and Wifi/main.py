from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

# Define a WTForms form for adding a cafe
class CafeForm(FlaskForm):
    # Choices for coffee rating represented by coffee cup emojis
    RATING_CHOICES = [
        '☕️',
        '☕️☕️',
        '☕️☕️☕️',
        '☕️☕️☕️☕️',
        '☕️☕️☕️☕️☕️'
    ]

    # Choices for Wifi strength, including '✘' to represent no wifi
    WIFI_CHOICES = [
        '✘',
        '💪',
        '💪💪',
        '💪💪💪',
        '💪💪💪💪',
        '💪💪💪💪💪',
    ]

    # Choices for power socket availability, including '✘' for none
    SOCKET_CHOICES = [
        '✘',
        '🔌',
        '🔌🔌',
        '🔌🔌🔌',
        '🔌🔌🔌🔌',
        '🔌🔌🔌🔌🔌',
    ]

    # Define form fields with labels and validators
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    op_time = StringField('Opening Time (e.g. 8AM)', validators=[DataRequired()])
    cl_time = StringField('Closing Time (e.g. 5:30PM)', validators=[DataRequired()])
    rating = SelectField('Coffee Rating', choices=RATING_CHOICES, validators=[DataRequired()])
    wifi = SelectField('Wifi Strength Rating', choices=WIFI_CHOICES, validators=[DataRequired()])
    socket = SelectField('Power Socket Availability', choices=SOCKET_CHOICES, validators=[DataRequired()])
    submit = SubmitField('Submit')


# Create Flask app instance
app = Flask(__name__)

# Secret key needed by Flask-WTF to protect against CSRF
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

# Initialize Bootstrap 5 for styling support in templates
Bootstrap5(app)


# Route for home page, renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


# Route for adding a new cafe entry
# Accepts GET to show the form and POST to submit data
@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    # If form is submitted and validates correctly
    if form.validate_on_submit():
        # Open CSV file in append mode, with UTF-8 encoding and no extra newline chars
        with open('cafe-data.csv', mode='a', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            # Collect data from form fields into a list matching CSV columns
            row = [
                form.cafe.data,
                form.location.data,
                form.op_time.data,
                form.cl_time.data,
                form.rating.data,
                form.wifi.data,
                form.socket.data
            ]
            print(row)  # Debug: print the row being written
            writer.writerow(row)  # Append the new cafe data to the CSV file
        # After successful submission, redirect user to the cafes list page
        return redirect(url_for('cafes'))

    # If GET request or form validation fails, render the form page again
    return render_template('add.html', form=form)


# Route to display all cafes stored in the CSV
@app.route('/cafes')
def cafes():
    # Open CSV in read mode
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        # Read all rows into a list
        for row in csv_data:
            list_of_rows.append(row)
    # Render cafes.html and pass the list of cafes to it for display
    return render_template('cafes.html', cafes=list_of_rows)


# Run the app if this file is executed directly (not imported)
if __name__ == '__main__':
    app.run(debug=True)
