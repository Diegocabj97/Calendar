from flask import Flask, render_template, request, jsonify
import calendar

app = Flask(__name__)

def create_calendar_matrix(year, month):
    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]
    return {
        "month_name": month_name,
        "year": year,
        "calendar": cal
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_calendar', methods=['POST'])
def get_calendar():
    year = int(request.form['year'])
    month = int(request.form['month'])
    return jsonify(create_calendar_matrix(year, month))

if __name__ == '__main__':
    app.run(debug=True)