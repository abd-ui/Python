
def syllables(word, num):
    if len(word) % num == 0:
        x = int(len(word)/num)
        while word:
            for i in range(x):
                print(word[i], end="")
            word = word[x:]
            print('', end=" ")
        print(word)
    else:
        print("Error")


syllables("establish", 3)
syllables("recollective", 6)
syllables("strongest", 4)
