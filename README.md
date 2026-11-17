This folder has two project which are a score tracker and a word counter. As the name implies, the score tracker is taking input from the user and it is sorting and arranging all from the highest to the count cycle of the word while the word counter is lliterally counting words. 
# python-practice

A collection of small Python programs I am building to strengthen my fundamentals. New practice projects will be added here as I complete them.

## Score Tracker

Takes a line of student scores typed by the user and reports the number of scores, the average, the highest score, the lowest score, and how many students passed. A score of 50 or above counts as a pass.

To run it, open a terminal in this folder and type:

```
python score_tracker.py
```

Enter the scores separated by spaces, for example `70 45 88 62 91`.

## Word Counter

Takes a sentence typed by the user, ignores capital letters and punctuation, then reports how many times each word appears and which word is the most common.

To run it, open a terminal in this folder and type:

```
python word_counter.py
```

## Known limits

- Score Tracker crashes if no scores are entered, or if anything other than whole numbers is typed.
- Word Counter only removes the punctuation marks . , ! ? ; : and does not handle others such as quotes or hyphens. 


## API

A small backend API built with FastAPI. It exposes the Score Tracker and Word Counter as endpoints.

### Setup

Create and activate a virtual environment, then install the packages:

```
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### Run the server

```
uvicorn main:app --reload
```

The server runs at http://127.0.0.1:8000. Open http://127.0.0.1:8000/docs to try every endpoint from the browser.

### Endpoints

**POST /analyse** takes a list of scores and returns the count, average, highest, lowest and number passed.

Request body:
```
{"scores": [70, 45, 88, 62, 91]}
```
Response:
```
{"count": 5, "average": 71.2, "highest": 91, "lowest": 45, "passed": 4}
```
An empty list returns status 400 with the message "Provide at least one score."

**POST /count-words** takes a text and returns how many times each word appears, ignoring capitals and punctuation.

Request body:
```
{"text": "Hi, hi! HI there."}
```
Response:
```
{"hi": 3, "there": 1}
```
Empty or blank text returns status 400 with the message "Provide some text."


### Live demo

https://python-practice-19o7.onrender.com/docs

This runs on a free hosting plan, so it goes to sleep when nobody has used it for a while. The first request after that can take around 30 seconds to wake up.