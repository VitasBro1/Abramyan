import math
def RectPS(x_1 , x_2 , y_1, y_2):
    P = (abs(x_1 - x_2) + abs(y_1 - y_2)) * 2
    S = abs(x_1 - x_2) * abs(y_1 - y_2)
    return P , S

print(RectPS(6 , 2 , 8 , 3))
