x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

if x1 < 0 or y1 < 0:
    print("Please Enter Valid Coordinates.")
elif x2 != x1 and y2 != y1:
    print("Invalid Move.")
elif x2 == x1 and y2 == y1:
    print("Please Make A Move.")
else:
    print("Valid Move.")
