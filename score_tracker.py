
def analyse(scores):
    
    count = len(scores)


    total = 0
    for s in scores:
        total = total + s
    average = total/count


    ordered=sorted(scores)
    highest = ordered[-1]
    lowest = ordered[0]

    counter=0
    for c in scores:
        if c >= 50:
            counter = counter + 1

    values = {"count":count , "average":average , "highest":highest , "lowest":lowest , "passed":counter }
    return values

line = input("Enter scores separated by spaces: ")
parts = line.split()

scores = []
for a in parts:
    scores.append(int(a))

result = analyse(scores)
print(result)
