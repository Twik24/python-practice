

def count_words(text):
    #lowered is turning the text into lowercase, so all the characters will be in lowercase
    marks = ".,!?;:"
    lowered = text.lower()
    for m in marks:
      lowered=lowered.replace(m,"")
    #split() is allowing us to split the words from a sentence and put it into a list of words
    words = lowered.split()
    counts = {}
    for w in words: 
       if w in counts:
         counts[w] = counts[w] + 1
       else:
            counts[w] = 1
    return counts 

user_text = input("Enter some text: ")
counts = count_words(user_text)
best_word = ""
highest_number = 0
for word, tally in counts.items():
    if tally > highest_number:
        best_word = word
        highest_number = tally
print(f"Most common: {best_word} ({highest_number})")     

for word,tally in counts.items():
    print(f"{word}: {tally}")