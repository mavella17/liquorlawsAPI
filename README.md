# Liquor Laws API
![Checkstyle](https://github.com/mavella17/liquorlawsAPI/actions/workflows/checkstyle.yaml/badge.svg)

## Required Libraries
- Can be found in requirements.txt

## How To Run:
Simply use ```  python3 app.py ``` to launch flask server locally.
Alternatively, use [this link](http://liquorlawsapi.pythonanywhere.com/) to access the hosted API.
## API Endpoints:
> [http://liquorlawsapi.pythonanywhere.com/laws](http://liquorlawsapi.pythonanywhere.com/laws)

is used to grab a list of all the laws for every state.
***
> [http://liquorlawsapi.pythonanywhere.com/laws/states.json](http://liquorlawsapi.pythonanywhere.com/laws/states.json)

is used to grab a list of all valid states/territories and their abbreviations.
***
> [http://liquorlawsapi.pythonanywhere.com/laws/states/<state_code>.json](http://liquorlawsapi.pythonanywhere.com/laws/states/<state_code>.json)

is used with a valid state abbreviation to get all laws of a single state. For example, to look up Georgia, you could use 
> [http://liquorlawsapi.pythonanywhere.com/laws/states/GA.json](http://liquorlawsapi.pythonanywhere.com/laws/states/GA.json)

***

> [http://liquorlawsapi.pythonanywhere.com/laws/age.json](http://liquorlawsapi.pythonanywhere.com/laws/age.json)

is used to look up age laws for all states.

***

> [http://liquorlawsapi.pythonanywhere.com/laws/notes.json](http://liquorlawsapi.pythonanywhere.com/laws/notes.json)

is used to look up extra notes for all states.

> [http://liquorlawsapi.pythonanywhere.com/laws/grocerysales.json](http://liquorlawsapi.pythonanywhere.com/laws/grocerysales.json)

is used to look up grocery sale laws for all states.

> [http://liquorlawsapi.pythonanywhere.com/laws/salehours.json](http://liquorlawsapi.pythonanywhere.com/laws/salehours.json)

is used to look up alcohol sales hours for each state.

> [http://liquorlawsapi.pythonanywhere.com/laws/abc.json](http://liquorlawsapi.pythonanywhere.com/laws/abc.json)

is used to look up grocery sale laws for all states.
