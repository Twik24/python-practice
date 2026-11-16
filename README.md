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