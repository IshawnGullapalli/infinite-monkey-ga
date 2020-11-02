"""
Author: Ishawn Gullapalli
Email: ishawn@gatech.edu
Credits: Daniel Shiffman, The Coding Train, https://shiffman.net/
"""

import random


def initialize_population(target, population_size):
    """
    This function creates a list representing the population. Each element of this list is a string of randomly
    generated ASCII characters.

    :param target: the target phrase
    :param population_size: the size of the population
    :return: a list of strings representing the population
    """
    return [''.join([chr(random.randint(32, 127)) for _ in range(len(target))])
            for _ in range(population_size)]


def calculate_fitness(target, element):
    """
    This function calculates the fitness score of an element. The fitness score is the number of characters in the
    element that match the target string divided by the number of characters in the target phrase.

    :param target: the target phrase
    :param element: the current phrase
    :return: the normalized fitness score
    """
    fitness = 0
    for i in range(len(target)):
        if target[i] == element[i]:
            fitness += 1
    return fitness / len(target)


def mutate_element(element, mutation_rate):
    """
    This function introduces mutations to an element based on a predetermined mutation rate.

    :param element: the current phrase
    :param mutation_rate: the probability that a character undergoes mutation
    :return: the mutated element
    """
    mutated = ""
    for i in range(len(element)):
        if random.uniform(0, 1) < mutation_rate:
            mutated += chr(random.randint(32, 127))
        else:
            mutated += element[i]
    return mutated


def get_best_element(population, fitnesses):
    """
    This function finds the best element (by fitness) in the population.

    :param population: the list of elements
    :param fitnesses: the list of fitness values corresponding to the population list
    :return: the element with the highest fitness
    """
    index = fitnesses.index(max(fitnesses))
    return population[index]


def display_info(population, population_size, fitnesses, generation):
    """
    This function prints out relevant information to the terminal.

    :param population: the list of elements
    :param population_size: the size of the population
    :param fitnesses: the list of fitness values corresponding to the population list
    :param generation: the current generation
    """
    print("Average Fitness:", sum(fitnesses) / population_size)
    print("Generation:", generation)
    print("Best Element:", get_best_element(population, fitnesses), "\n")


def genetic_algorithm(target, population_size, mutation_rate):
    """
    This function is the main genetic algorithm. It generates various elements until the target phrase is reached.
    Every generation, it prints relevant information to the terminal.

    :param target: the target phrase
    :param population_size: the size of the population
    :param mutation_rate: the probability that a character in an element undergoes mutation
    """
    # Create initial population and calculate initial fitness values
    population = initialize_population(target, population_size)
    fitnesses = [calculate_fitness(target, element) for element in population]
    generation = 0

    # Loop until the target phrase is generated
    while target not in population:

        # Create the next generation
        new_population = []
        for _ in range(population_size):

            # Pick parents proportionally to their fitness values
            parent_a = random.choices(population, weights=fitnesses, k=1)[0]
            parent_b = random.choices(population, weights=fitnesses, k=1)[0]

            # Create a child containing part of parent_a's characters and part of parent_b's characters
            midpoint = random.randrange(0, len(target))
            child = parent_a[:midpoint] + parent_b[midpoint:]
            child = mutate_element(child, mutation_rate)

            # Add the child to the new generation
            new_population.append(child)

        # Update the population and its associated fitness values
        population = new_population
        fitnesses = [calculate_fitness(target, element) for element in population]
        generation += 1

        # Print relevant information to the terminal
        display_info(population, population_size, fitnesses, generation)


"""
This executes the genetic algorithm with the following parameters:
- Target phrase: To be or not to be.
- Population size: 200
- Mutation rate: 1%
These values can be modified.
"""
genetic_algorithm("To be or not to be.", 200, 0.01)
