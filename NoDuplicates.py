def main():
    sentence = input()
    sentence = "THE RAIN IN SPAIN"
    split = sentence.split()

    for i in range(len(split)):
        count = 0
        for word in split:
            if split[i] == word:
                count += 1
        if (count >= 2):
            return "no"

    return "yes"

print(main())
