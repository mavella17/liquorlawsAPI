# Liquor Laws API
![Checkstyle](https://github.com/mavella17/liquorlawsAPI/actions/workflows/checkstyle.yaml/badge.svg)

## Required Libraries
- Can be found in requirements.txt

## How To Run:
Simply use ```  python3 app.py ``` to launch flask server locally.
Alternatively, use [this link](http://liquorlawsapi.pythonanywhere.com/) to access the hosted API.
## API Endpoints:
### All Laws:
> [http://liquorlawsapi.pythonanywhere.com/laws](http://liquorlawsapi.pythonanywhere.com/laws)

is used to grab a list of all the laws for every state.
### List States/Abbreviations:
> [http://liquorlawsapi.pythonanywhere.com/laws/states.json](http://liquorlawsapi.pythonanywhere.com/laws/states.json)

is used to grab a list of all valid states/territories and their abbreviations.
### Single State Laws:
> [http://liquorlawsapi.pythonanywhere.com/laws/states/<state_code>.json](http://liquorlawsapi.pythonanywhere.com/laws/states/<state_code>.json)

is used with a valid state abbreviation to get all laws of a single state. For example, to look up Georgia, you could use 
> [http://liquorlawsapi.pythonanywhere.com/laws/states/GA.json](http://liquorlawsapi.pythonanywhere.com/laws/states/GA.json)

### Age Laws:
> [http://liquorlawsapi.pythonanywhere.com/laws/age/<state_code>.json](http://liquorlawsapi.pythonanywhere.com/laws/age/<state_code>.json)

is used with a valid state abbreviation to get age laws of a single state. For example, to look up Maine, you could use 
> [http://liquorlawsapi.pythonanywhere.com/laws/age/ME.json](http://liquorlawsapi.pythonanywhere.com/laws/age/ME.json)

Alternatively, you can use 
> [http://liquorlawsapi.pythonanywhere.com/laws/age](http://liquorlawsapi.pythonanywhere.com/laws/age)

to grab age laws for every state.

### Grocery Sales:
> [http://liquorlawsapi.pythonanywhere.com/laws/grocerysales/<state_code>.json](http://liquorlawsapi.pythonanywhere.com/laws/grocerysales/<state_code>.json)

is used with a valid state abbreviation to get grocery sale laws of a single state. For example, to look up New York, you could use 
> [http://liquorlawsapi.pythonanywhere.com/laws/grocerysales/NY.json](http://liquorlawsapi.pythonanywhere.com/laws/grocerysales/NY.json)

Alternatively, you can use 
> [http://liquorlawsapi.pythonanywhere.com/laws/grocerysales](http://liquorlawsapi.pythonanywhere.com/laws/grocerysales)

to grab age grocery sales laws for all states.

### Sale Hours: 
> [http://liquorlawsapi.pythonanywhere.com/laws/salehours/<state_code>.json](http://liquorlawsapi.pythonanywhere.com/laws/salehours/<state_code>.json)

is used with a valid state abbreviation to get alcohol sales hours of a single state. For example, to look up Alaska, you could use 
> [http://liquorlawsapi.pythonanywhere.com/laws/salehours/AK.json](http://liquorlawsapi.pythonanywhere.com/laws/salehours/AK.json)

Alternatively, you can use 
> [http://liquorlawsapi.pythonanywhere.com/laws/salehours](http://liquorlawsapi.pythonanywhere.com/laws/salehours)

to grab age sales hours for all states.

### Alcohol Beverage Control Laws:
> [http://liquorlawsapi.pythonanywhere.com/laws/abc/<state_code>.json](http://liquorlawsapi.pythonanywhere.com/laws/abc/<state_code>.json)

is used with a valid state abbreviation to get ABC laws of a single state. For example, to look up Michigan, you could use 
> [http://liquorlawsapi.pythonanywhere.com/laws/abc/MI.json](http://liquorlawsapi.pythonanywhere.com/laws/abc/MI.json)

Alternatively, you can use 
> [http://liquorlawsapi.pythonanywhere.com/laws/abc](http://liquorlawsapi.pythonanywhere.com/laws/abc)

to grab age ABC laws for all states.

### Notes:
> [http://liquorlawsapi.pythonanywhere.com/laws/notes/<state_code>.json](http://liquorlawsapi.pythonanywhere.com/laws/notes/<state_code>.json)

is used with a valid state abbreviation to get extra notes for a single state. For example, to look up Florida, you could use 
> [http://liquorlawsapi.pythonanywhere.com/laws/notes/FL.json](http://liquorlawsapi.pythonanywhere.com/laws/notes/FL.json)

Alternatively, you can use 
> [http://liquorlawsapi.pythonanywhere.com/laws/notes](http://liquorlawsapi.pythonanywhere.com/laws/notes)

to grab notes for all states.


