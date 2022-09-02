def main():
    print(first_word(sequence()))
    chosen = input("What word did you choose? ")
    color = input("What were the colors... G for Green, Y for Yellow, N for No Color? ")
    print(second_word(chosen, color, sequence()))


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
    omit = []
    color_scheme.replace(" ", "")
    maybe_answer = 0
    answer_choices = []
    for i in range(len(color_scheme)):

        if color_scheme[i].lower() == "g":
            greens.append(word_chosen[i])
        else:
            greens.append("yb")

        if color_scheme[i].lower() == "y":
            yellows.append(word_chosen[i].lower())

        if color_scheme[i].lower() == "b":
            omit.append(word_chosen[i].lower())
    for i in range(len(Possible)):
        for j in range(len(Possible[i])):
            if Possible[i][j].lower() == greens[j].lower() or Possible[i][j].lower() in yellows:
                maybe_answer += 1
            if Possible[i][j].lower in omit:
                maybe_answer -= 1
        if maybe_answer == 5:
            answer_choices.append(Possible[i])
    return answer_choices


if __name__ == "__main__":
    main()
