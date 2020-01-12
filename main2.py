#!/usr/bin/python
# -*- coding: latin-1 -*-
from random import randint


class Individual:
    """Classe représentant un étudiant.

    On représente un étudiant par son prénom (attribut prenom), son âge
    (attribut age) et sa note moyenne (attribut moyenne, entre 0 et 20).

    Paramètres du constructeur :
        prenom -- le prénom de l'étudiant
        age -- l'âge de l'étudiant
        moyenne -- la moyenne de l'étudiant

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
