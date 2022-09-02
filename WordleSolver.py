omit = []


def main():
    print(first_word(sequence()))
    i = 6
    color = ""
    while i > 0 and color != "ggggg":
        chosen = input("What word did you choose? ")
        color = input("What were the colors... g for Green, y for Yellow, b for No Color? ")
        print(second_word(chosen, color, sequence()))
        i -= 1


def sequence():
    with open('PossibleAnswers') as file:
        lines = file.readlines()

    all_words = []
    for line in lines:
        all_words.append(line.rstrip().upper())
    return all_words


def first_word(Possible):
    first = []
    for i in range(len(Possible)):
        vowel_count = 0
        for j in range(len(Possible[i])):
            if Possible[i][j].lower() in ["a", "e", "i", "o", "u"]:
                vowel_count += 1
        if vowel_count > 3:
            first.append(Possible[i])
    return first


def second_word(word_chosen, color_scheme, Possible):
    greens = []
    yellows = []
    color_scheme.replace(" ", "")
    amount = 0
    answer_choices = []
    for i in range(len(color_scheme)):
        if color_scheme[i].lower() == "g":
            greens.append(word_chosen[i])
            amount += 100
        else:
            greens.append("yb")

        if color_scheme[i].lower() == "y":
            yellows.append(word_chosen[i].lower())
            amount += 7
        if color_scheme[i].lower() == "b":
            omit.append(word_chosen[i].lower())
            amount += 1

    for i in range(len(Possible)):
        count = 0
        for j in range(len(Possible[i])):
            if Possible[i][j].lower() == greens[j].lower():
                count += 100
            elif Possible[i][j].lower() in yellows:
                count += 7
            elif Possible[i][j].lower() not in omit:
                count += 1
        if count == amount:
            answer_choices.append(Possible[i])
    return answer_choices


if __name__ == "__main__":
    main()
