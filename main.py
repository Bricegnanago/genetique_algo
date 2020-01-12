#!/usr/bin/python
# -*- coding: latin-1 -*-
# Etapes
# creation de n individus sur 8 bit Ok
# Ordonner
# selection : les individu les plus solide seront selectionne
# Mutation : une fonction qui permettra d ajouter une caractéristique a un individu

from random import randint


def individual_to_string():
    pass


# Generer un individu
def generate_individual():
    individual = []
    for bit in range(0, 8):
        individual.append(randint(0, 1))

    return individual


def generate_population():
    population = []
    for i in range(0, 8):
        population.append(generate_individual())
    return population


# il s'agit ici de calculer la robustesse d'un individu
def compute_fitness(individual):
    score = 0
    for i in range(0, 8):
        score = sum(individual)
    return score


def storage_all_fitness(sample):
    getter_fitness = []
    for i in range(0, 8):
        current_dic = (i, compute_fitness(sample[i]))
        getter_fitness.append(current_dic)

    return getter_fitness


def order_by_fitness(pop_fitness):
    pop_fitness = sorted(pop_fitness, key=lambda column: column[1], reverse=True)
    return pop_fitness


def get_a_new_generation(pop, location_ordered):
    new_generation = []
    location = []
    # recuperation des indices des individu les plus robuste
    for i in range(0, 4):
        location.append(location_ordered[i][0])
    # recupération des indivu les plus robuste
    for i in range(0, 4):
        new_generation.append(pop[location[i]])
    return new_generation


population = generate_population()
fits = storage_all_fitness(population)
fits_ordered = order_by_fitness(fits)

new_generation = get_a_new_generation(population, fits_ordered)

# print(population)
# print(fits)
print(fits_ordered)
#print(population)
print(new_generation)
