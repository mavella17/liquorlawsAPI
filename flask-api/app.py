import git
from flask import Flask, jsonify, render_template, url_for, flash, redirect, request
import pandas as pd
import sqlalchemy as db
from sqlalchemy import select
from sqlalchemy.sql import text as sa_text
app = Flask(__name__)
engine = db.create_engine('sqlite:///laws.db')

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', subtitle='Home Page',
                           text='This is the home page')

@app.route('/states.json', methods=['GET'])
def get_states():
    # Logic to retrieve and format the list of states
    states = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming',
    'PR': 'Puerto Rico'
}
    return jsonify(states)


@app.route('/states/<state_code>.json', methods=['GET'])
def get_state_liquor_laws(state_code):
    # Logic to retrieve and format liquor laws for the given state
    columns = ['Location',
               'Abbreviation',
               'Alcoholic beverage control state: Beer',
               'Alcoholic beverage control state: Wine',
               'Alcoholic beverage control state: Distilled spirits',
               'Alcohol sale hours: On-premises',
               'Alcohol sale hours: Off-premises',
               'Grocery store sales: Beer',
               'Grocery store sales: Wine',
               'Grocery store sales: Distilled Spirits',
               'Age: Purchasing',
               'Age: Consumption',
               'Notes: Notes']
    sql = "Select * FROM laws where Abbreviation='" + state_code + "';"
    df = pd.read_sql(sql, con=engine)
    results = df.to_dict('records')
    return jsonify(results)

@app.route('/age.json', methods =['GET'])
def age():
    sql = """Select Abbreviation, "Age: Consumption", "Age: Purchasing" from laws;"""
    df = pd.read_sql(sql, con=engine)
    results = df.to_dict('records')
    return jsonify(results)

@app.route('/notes.json', methods =['GET'])
def notes():
    sql = "Select Abbreviation, Location, Notes from laws;"
    df = pd.read_sql(sql, con=engine)
    results = df.to_dict('records')
    return jsonify(results)

@app.route('/grocerysales.json', methods =['GET'])
def grocerysales():
    sql = """Select Abbreviation, Location, "Grocery store sales: Beer",
               "Grocery store sales: Wine",
               "Grocery store sales: Distilled Spirits" from laws;"""
    df = pd.read_sql(sql, con=engine)
    results = df.to_dict('records')
    return jsonify(results)

@app.route('/salehours.json', methods =['GET'])
def salehours():
    sql = """Select Abbreviation, Location, "Alcohol sale hours: On-premises",
               "Alcohol sale hours: Off-premises" from laws;"""
    df = pd.read_sql(sql, con=engine)
    
    results = df.to_dict('records')
    return jsonify(results)

@app.route('/abc.json', methods =['GET'])
def abc():
    sql = """Select Abbreviation, Location, "Alcoholic beverage control state: Beer",
               "Alcoholic beverage control state: Wine",
               "Alcoholic beverage control state: Distilled spirits" from laws;"""
    df = pd.read_sql(sql, con=engine)
    results = df.to_dict('records')
    return jsonify(results)


@app.route("/update_server", methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('/home/liquorlawsAPI/liquorlawsAPI')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
