import sys

correct = 0
time = 0
questions = []

for a in range(0, 25):
    questions.append(0)

for i in sys.stdin:
    i = i.split()
    if (len(i) < 3):
        break
    
    if (i[2] == 'wrong'):
        questions[ord(i[1])-65] += 1
    else:
        correct += 1
        time += int(i[0]) + (20 * questions[ord(i[1])-65])


print(correct, time)
