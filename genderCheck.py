def gender_checker(word):
    letters = []
    nonRepeating = []
    for i in word:
        letters.append(i)

    for i in letters:
        if (letters.count(i) == 1):
            nonRepeating.append(i)
    if len(nonRepeating) % 2 == 0:
        print('Boy')
    else:
        print('Girl')


gender_checker('aakq')
