from math import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherCoord(self):
        print(f'Les coordonnées du point sont ({self.x}, {self.y})')

class Cercle:
    def __init__(self, O, rayon):
        # a, b = 0, 0
        # self.O = [a, b]
        self.O = O
        self._rayon = rayon

    def getRayon(self):
        return self._rayon

    def setRayon(self, val):
        self._rayon = val

    def surface(self):
        surf = pi * (self.getRayon()**2)
        return surf

    def perimetre(self):
        perim = 2 * pi *self.getRayon()
        return perim

    def testAppartenance(self, x, y):
        if (abs(x) > self.getRayon() and abs(y) > self.getRayon()) or (abs(x) + abs(y)) > self.getRayon():
            return f"({x}, {y}) n'appartient pas au cercle C"
        else:
            return f"({x}, {y}) appartient au cercle C"

class Cylindre(Cercle):
    def __init__(self, O, rayon, hauteur):
        super().__init__(O, rayon)
        self.hauteur = hauteur

    def Volume(self):
        vol = pi * self.getRayon()**2 * self.hauteur
        return vol

# CREATION DU POINT 
P1 = Point(0, 0)

# CREATION DU CERCLE 
C1 = Cercle([P1.x, P1.y], 5)
print('Surface  du Cercle : ',C1.surface())
print('Perimetre du Cercle : ',C1.perimetre())

P2 = Point(0, 4)
print(C1.testAppartenance(P2.x, P2.y))

# CREATION DU CYLINDRE 
Cy1 = Cylindre({0, 0}, 5, 4)
print('Volume du Cylindre : ',Cy1.Volume())
