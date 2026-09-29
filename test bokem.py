def get(x, y):
    while (x != y):
        while(x>y):
            x -= y
            print(x,y)
        while(x<y):
            y -= x
            print(x,y)
    return x
print(get(3056567657567056565887687686565454354243254364765876876876, 2545675675670))