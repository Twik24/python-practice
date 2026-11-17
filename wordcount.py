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
