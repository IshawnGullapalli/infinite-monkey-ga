import random

from deap import base
from deap import creator
from deap import tools

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()


def random_ascii():
    """
    This function returns a random ASCII character.

    :return: a random ASCII character
    """
    return chr(random.randint(32, 127))


def calculate_fitness(individual, target):
    """
    This function calculates the fitness score of an individual. The fitness score is the number of characters in the
    individual that match the target string divided by the number of characters in the target phrase.

    :param target: the target phrase (as a string)
    :param individual: the current phrase (as a list of characters)
    :return: the normalized fitness score
    """
    fitness = 0
    for i in range(len(target)):
        if individual[i] == target[i]:
            fitness += 1
    return (fitness / len(target)),


def mutate_individual(individual, indpb=0.05):
    """
    This function introduces mutations to an individual based on a predetermined mutation rate.

    :param individual: the current phrase
    :param indpb: the probability that a character undergoes mutation
    :return: the mutated element
    """
    for i in range(len(individual)):
        if random.uniform(0, 1) < indpb:
            individual[i] = chr(random.randint(32, 127))


def get_best_element(population, fitnesses):
    """
    This function finds the best individual (by fitness) in the population.

    :param population: the list of individuals
    :param fitnesses: the list of fitness values corresponding to the population list
    :return: the individual with the highest fitness
    """
    index = fitnesses.index(max(fitnesses))
    return population[index]


def display_info(population, fitnesses, generation):
    """
    This function prints out relevant information to the terminal.

    :param population: the list of individuals
    :param fitnesses: the list of fitness values corresponding to the population list
    :param generation: the current generation
    """
    print("Average Fitness:", sum(fitnesses) / len(population))
    print("Generation:", generation)
    print("Best Individual:", ''.join(get_best_element(population, fitnesses)), "\n")


def main(target, population_size, mutation_rate):
    """
    This function is the main genetic algorithm. It generates various individuals until the target phrase is reached.
    Every generation, it prints relevant information to the terminal.

    :param target: the target phrase
    :param population_size: the size of the population
    :param mutation_rate: the probability that a character in an element undergoes mutation
    """
    # Attribute generator
    toolbox.register("attr_char", random_ascii)
    # Structure initializers
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_char, len(target))
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("evaluate", calculate_fitness, target=target)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", mutate_individual, indpb=mutation_rate)
    toolbox.register("select", tools.selTournament, tournsize=3)

    # Instantiate population
    pop = toolbox.population(n=population_size)
    # Evaluate the entire population
    fitnesses = list(map(toolbox.evaluate, pop))

    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    # cxpb  is the probability with which two individuals are crossed
    # mutpb is the probability for mutating an individual
    cxpb, mutpb = 1.0, 1.0

    # Extracting all the fitnesses
    fits = [ind.fitness.values[0] for ind in pop]
    # Variable keeping track of the number of generations
    generations = 0

    # Begin the evolution
    while max(fits) < 1.0 and generations < 1000:
        # A new generation
        generations += 1
        # Select the next generation individuals
        offspring = toolbox.select(pop, len(pop))
        # Clone the selected individuals
        offspring = list(map(toolbox.clone, offspring))
        # Apply crossover and mutation on the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < cxpb:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values
        for mutant in offspring:
            if random.random() < mutpb:
                toolbox.mutate(mutant)
                del mutant.fitness.values
        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = list(map(toolbox.evaluate, invalid_ind))
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit
        pop[:] = offspring

        # Gather all the fitnesses in one list and print the stats
        fits = [ind.fitness.values[0] for ind in pop]
        display_info(pop, fits, generations)


"""
This executes the genetic algorithm with the following parameters:
- Target phrase: To be or not to be.
- Population size: 200
- Mutation rate: 1%
These values can be modified.
"""
if __name__ == '__main__':
    main("To be or not to be.", 200, 0.01)
