color = input()
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

if y2 != y1:
    print("NO")

if color == "White":
    if (x1 == 2):
        if (x2 - x1 == 2) or (x2 - x1 == 1):
            print("YES")

        elif x2 == 1:
            print("NO")

    elif x2 - x1 == 1:
        print("YES")

    elif x2 == 1:
        print("NO")

    else:
        print("NO")

elif color == "Black":
    if (x1 == 7):
        if (x1 - x2 == 2) or (x1 - x2 == 1):
            print("YES")

        elif x2 == 8:
            print("NO")

    elif x1 - x2 == 1:
        print("YES")

    elif x2 == 8:
        print("NO")

    else:
        print("NO")
else:
    print("NO")