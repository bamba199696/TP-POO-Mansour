from math import *

class Point:
    # Je crée un constructeur
    def __init__(self, a, b):
        self.x = a
        self.y = b

    def afficher(self):
        return f"Les coordonnées sont ({self.x}, {self.y})"

class Cercle:
    def __init__(self, point, rayon, couleur):
        self.centre = (point.x, point.y)
        self.__rayon = rayon
        self.couleur = couleur

    def getRayon(self):
        return self.__rayon

    def setRayon(self, val):
        self.__rayon = val

    def presenter(self):
        print(f"On a un cercle de centre {self.centre}, de rayon {self.__rayon} et de couleur {self.couleur}")    

    def surface(self):
        aire = pi * self.__rayon**2
        return aire

    def appartenir(self, point):
        norm = sqrt(pow((point.x - self.centre[0]), 2) + pow((point.y - self.centre[1]), 2))
        if norm <= self.__rayon:
            return f'Le point de coordonées ({point.x},{point.y}) appartient au cercle'
        else:
            return f'Le point de coordonées ({point.x},{point.y}) n\'appartient pas au cercle'


class Cylindre(Cercle):
    def __init__(self, point, rayon, couleur, hauteur):
        super().__init__(point, rayon, couleur)
        self.hauteur = hauteur

    def Volume(self):
        vol = super().surface() * self.hauteur
        print(f'Le volume est {vol}')


P1 = Point(1, 2)
C1 = Cercle(P1, 5, "noire")
C1.setRayon(197)
C1.presenter()
print(C1.centre)
P2 = Point(-2, 2)
print(C1.appartenir(P2))

Cy1 = Cylindre(P1, 7, 'verte', 9)
Cy1.Volume()