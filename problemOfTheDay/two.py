
def syllobales(word, num):
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


syllobales("establish", 3)
syllobales("recollective", 6)
syllobales("strongest", 4)
