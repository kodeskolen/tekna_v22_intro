
# (4/3)*pi*radius**3

pi = 3.14

radius_klinkekule = 1
radius_tennisball = 2.5
radius_bowlingball = 7

def kulevolum(radius):
    volum = (4/3)*pi*radius**3
    return volum


print(kulevolum(radius_klinkekule))
print(kulevolum(radius_tennisball))
print(kulevolum(radius_bowlingball))
