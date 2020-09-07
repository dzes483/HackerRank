import math

side_ab = int(input())
side_bc = int(input())

hypotenuse = math.hypot(side_ab, side_bc)

angle = math.degrees(math.acos(side_bc/hypotenuse))

print(str(round(angle)) + '°')
