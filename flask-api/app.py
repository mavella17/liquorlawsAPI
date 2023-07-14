import git
from flask import Flask, jsonify, render_template
from flask import url_for, flash, redirect, request
import pandas as pd
import sqlalchemy as db
from sqlalchemy import select
from sqlalchemy.sql import text as sa_text
app = Flask(__name__)
engine = db.create_engine('sqlite:///laws.db')
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', subtitle='Home Page',
                           text='This is the home page')


# gets a list of all laws
@app.route('/laws', methods=['GET'])
def laws():
    sql = """Select * from laws;"""
    df = pd.read_sql(sql, con=engine)
    results = df.to_dict('records')
    return jsonify(results)


# gets a list of all states
@app.route('/laws/states.json', methods=['GET'])
def get_states():




    # Logic to retrieve and format the list of states
    states = {'AK': 'Alaska',
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


# Look up indivdual states
@app.route('/laws/states/<state_code>.json', methods=['GET'])
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


# gets every states ages
@app.route('/laws/age', methods=['GET'])
def age():
    sql = """Select Abbreviation, "Age: Consumption", """
    sql += """"Age: Purchasing" from laws;"""
    df = pd.read_sql(sql, con=engine)
    results = df.to_dict('records')
    return jsonify(results)


# allows grabbing of age laws for specific state
@app.route('/laws/age/<state_code>.json', methods=['GET'])
def age_sc(state_code):
    sql = """Select Abbreviation, "Age: Consumption", """
    sql += """"Age: Purchasing" from laws """
    sql += "where Abbreviation='" + state_code + "';"
    df = pd.read_sql(sql, con=engine)
    results = df.to_dict('records')
    return jsonify(results)


# returns all notes from all states
@app.route('/laws/notes', methods=['GET'])
def notes():
    sql = "Select Abbreviation, Location, Notes from laws;"
    df = pd.read_sql(sql, con=engine)
    results = df.to_dict('records')
    return jsonify(results)


# grab notes for a specific state
@app.route('/laws/notes/<state_code>.json', methods=['GET'])
def notes_sc(state_code):
    sql = "Select Abbreviation, Location, Notes from laws "
    sql += "where Abbreviation='" + state_code + "';"
    df = pd.read_sql(sql, con=engine)
    results = df.to_dict('records')
    return jsonify(results)


# grocery sale laws for every state
@app.route('/laws/grocerysales', methods=['GET'])
def grocerysales():
    sql = """Select Abbreviation, Location, "Grocery store sales: Beer",
               "Grocery store sales: Wine",
               "Grocery store sales: Distilled Spirits" from laws;"""
    df = pd.read_sql(sql, con=engine)
    results = df.to_dict('records')
    return jsonify(results)


# gets grocery sale laws for one state
@app.route('/laws/grocerysales/<state_code>.json', methods=['GET'])
def grocerysales_sc(state_code):
    sql = """Select Abbreviation, Location, "Grocery store sales: Beer",
               "Grocery store sales: Wine",
               "Grocery store sales: Distilled Spirits" from laws """
    sql += "where Abbreviation='" + state_code + "';"
    df = pd.read_sql(sql, con=engine)
    results = df.to_dict('records')
    return jsonify(results)


# sale hours for every state
@app.route('/laws/salehours', methods=['GET'])
def salehours():
    sql = """Select Abbreviation, Location, "Alcohol sale hours: On-premises",
               "Alcohol sale hours: Off-premises" from laws;"""
    df = pd.read_sql(sql, con=engine)
    results = df.to_dict('records')
    return jsonify(results)


# sale hours for a single state
@app.route('/laws/salehours/<state_code>.json', methods=['GET'])
def salehours_sc(state_code):
    sql = """Select Abbreviation, Location, "Alcohol sale hours: On-premises",
               "Alcohol sale hours: Off-premises" from laws """
    sql += "where Abbreviation='" + state_code + "';"
    df = pd.read_sql(sql, con=engine)
    results = df.to_dict('records')
    return jsonify(results)


# alcohol beverage controlled laws for every state
@app.route('/laws/abc', methods=['GET'])
def abc():
    sql = """Select Abbreviation, Location,
               "Alcoholic beverage control state: Beer",
               "Alcoholic beverage control state: Wine",
               "Alcoholic beverage control state: Distilled spirits"
                from laws;"""
    df = pd.read_sql(sql, con=engine)
    results = df.to_dict('records')
    return jsonify(results)


# alcohol beverage controlled laws for every state
@app.route('/laws/abc/<state_code>.json', methods=['GET'])
def abc_sc(state_code):
    sql = """Select Abbreviation, Location,
               "Alcoholic beverage control state: Beer",
               "Alcoholic beverage control state: Wine",
               "Alcoholic beverage control state: Distilled spirits"
                from laws """
    sql += "where Abbreviation='" + state_code + "';"
    df = pd.read_sql(sql, con=engine)
    results = df.to_dict('records')
    return jsonify(results)


# used with webhooks to update server
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
