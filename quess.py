from random import randint

result = randint(1, 100)
#print(result)


while True: 
    quess: int = int(input('Odhad 1-100: '))

    if quess == result:
        print('Spravny odhad')
    elif quess < result:
        print('Tajne cislo je vetsi')
    elif quess > result:
        print('Tajne cislo je mensi')
