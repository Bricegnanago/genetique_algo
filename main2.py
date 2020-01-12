#!/usr/bin/python
# -*- coding: latin-1 -*-
from random import randint


class Individual:
    """Classe repr�sentant un �tudiant.

    On repr�sente un �tudiant par son pr�nom (attribut prenom), son �ge
    (attribut age) et sa note moyenne (attribut moyenne, entre 0 et 20).

    Param�tres du constructeur :
        prenom -- le pr�nom de l'�tudiant
        age -- l'�ge de l'�tudiant
        moyenne -- la moyenne de l'�tudiant

    """

    def __init__(self, adn, fitness):
        self.adn = adn
        self.fitness = fitness

    def __repr__(self):
        return "<Individual {} (adn={}, fitness={})>".format(
            self.adn, self.fitness)


def generate_individual():
    #creer un individu
    ind = Individual()
    for bit in range(0, 8):
        ind.append(randint(0, 1))


individual = Individual([1, 1, 0, 0], 2)
print(individual.fitness)
