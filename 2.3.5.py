# creating an acronym


def main():

    phrase = input('What is the phrase?: ')
    x = phrase.split()
    print(x)
    acro = []
    for stuff in x:
        acro.append(stuff[0])
    acro1 = ''.join(acro).upper()
    print(acro1)


main()
