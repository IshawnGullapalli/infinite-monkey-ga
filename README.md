# Phrase Evolution
This Python project was adapted from and built upon the [Genetic Algorithm series](https://www.youtube.com/watch?v=9zfeTw-uFCw&list=PLRqwX-V7Uu6bJM3VgzjNV5YxVxUwzALHV) by [Daniel Shiffman](https://shiffman.net/) on his YouTube channel, [The Coding Train](https://www.youtube.com/channel/UCvjgXvBlbQiydffZU7m1_aw). This is an example of an application of a genetic algorithm to solve a problem inspired by the [Infinite Monkey Theorem](https://en.wikipedia.org/wiki/Infinite_monkey_theorem).

### Infinite Monkey Theorem
In essence, this theorem states that given an infinite amount of time, a monkey hitting random keys on a keyboard will be almost guaranteed to type any (and every) given text. While this scenario would be interesting to simulate, it is unfortunately not feasible. However, it serves as the basis for the problem solved by this algorithm.

### The Problem
Given a target phrase consisting only ASCII characters, generate the phrase and print it to the terminal. This problem is actually an expanded version of the [One Max Problem](https://tracer.lcc.uma.es/problems/onemax/onemax.html).

### The Solution
1. We will start by generating a list of phrases which will act as our population. 
    - Each of these phrases will initially be sequences of random ASCII characters.
    - Each phrase will have the same number of characters as the target phrase.
2. Then, we will calculate the fitness scores of every element in the population. 
    - The fitness of an element is defined as the number of characters in the element that match characters in the target phrase divided by the length of the target phrase. 
    - For example, if the target phrase was "hello", the element "jello" would have a fitness score of 0.8.
3. Next, we will generate the next generation.
    - We will select two elements out of the current population proportionately to their fitness scores.
    - From these two elements, we will create a new element consisting of a random number of characters from both.
    - This element will have a chance to be mutated to introduce more variation into the population.
    - Then, this element will be added to the new population.
    - This process will be repeated for every element in the current population.
4. Now, we will step forward one generation.
    - The current population will be replaced by the new population.
    - Fitness scores will be recalculated for the new population.
    - Relevant information will be printed to the terminal.
5. Steps 3 and 4 will repeat until the population contains an element that has a fitness score of 1.0 (meaning that the target phrase was generated).

### Conclusion
While this problem can be easily solved through other means (printing the target phrase directly to the terminal, for example), it serves as a good example of the usage and implementation of a genetic algorithm. This type of algorithm can be applied to other problems which are not as trivial.

### Note
This repository contains two files, "phrase_evolution.py" and "phrase_evolution_deap.py". The former is a solution implemented without the use of specialized external packages. The latter makes use of the [DEAP framework](https://github.com/deap/deap) to solve the same problem.
