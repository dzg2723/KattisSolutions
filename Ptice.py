questions = input()
answers = input()

adrian = ['A', 'B', 'C']
bruno = ['B', 'A', 'B', 'C']
goran = ['C', 'C', 'A', 'A', 'B', 'B']

adrian_correct = 0
bruno_correct = 0
goran_correct = 0


for char in range(len(answers)):
##    print(answers[char], adrian[char%3], bruno[char%4], goran[char%6])
    if (adrian[char%3] == answers[char]):
        adrian_correct += 1
    if (bruno[char%4] == answers[char]):
        bruno_correct += 1
    if (goran[char%6] == answers[char]):
        goran_correct += 1

most_correct = max(adrian_correct, bruno_correct, goran_correct)

print(most_correct)
if adrian_correct == most_correct:
    print("Adrian")
if bruno_correct == most_correct:
    print("Bruno")
if goran_correct == most_correct:
    print("Goran")
