import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import random

# Set random seed for reproducibility
np.random.seed(42)

# 1. Initialize Environment and Libraries
# (Libraries are imported above)

# 2. Define Bird Species Attributes
class Bird:
    def __init__(self, dna_sequence, fitness, mutation_rate, reproduction_type):
        self.dna_sequence = dna_sequence
        self.fitness = fitness
        self.mutation_rate = mutation_rate
        self.reproduction_type = reproduction_type

    def mutate(self):
        dna_list = list(self.dna_sequence)
        for i in range(len(dna_list)):
            if random.random() < self.mutation_rate:
                dna_list[i] = random.choice(['A', 'T', 'C', 'G'])
        self.dna_sequence = ''.join(dna_list)

# 3. Set Up Environmental Variables
environment = {
    'Temperature': 20,  # in degrees Celsius
    'Food_Availability': 100,  # units
    'Predator_Density': 5,
    'Nesting_Sites': 50
}

# 4. Initialize Population
initial_population = [
    Bird('ATCGGCTAAC', 0.80, 0.02, 'Sexual'),
    Bird('TTGCCAGGTA', 0.85, 0.01, 'Sexual'),
    Bird('GGCATATTGC', 0.75, 0.01, 'Sexual')
]

# Expand initial population to 30 birds for diversity
for _ in range(27):
    new_bird = random.choice(initial_population)
    mutated_bird = Bird(new_bird.dna_sequence, new_bird.fitness, new_bird.mutation_rate, new_bird.reproduction_type)
    mutated_bird.mutate()
    initial_population.append(mutated_bird)

# 5. Simulation Loop
generations = 20
data = []

for generation in range(generations):
    # Simulate changes in environment
    environment['Food_Availability'] = max(0, environment['Food_Availability'] + np.random.randint(-10, 10))
    
    # Update fitness based on food availability
    for bird in initial_population:
        if environment['Food_Availability'] < 50:
            bird.fitness -= 0.01
        else:
            bird.fitness += 0.01
        bird.mutate()
    
    # Record data for analysis
    avg_fitness = np.mean([bird.fitness for bird in initial_population])
    genetic_diversity = len(set([bird.dna_sequence for bird in initial_population])) / len(initial_population)
    data.append([generation, avg_fitness, len(initial_population), genetic_diversity])

# 6. Data Analysis and Visualization
results_df = pd.DataFrame(data, columns=['Generation', 'Avg_Fitness', 'Population_Size', 'Genetic_Diversity'])

# Plotting results
plt.figure(figsize=(10, 6))
plt.plot(results_df['Generation'], results_df['Avg_Fitness'], label='Average Fitness')
plt.plot(results_df['Generation'], results_df['Genetic_Diversity'], label='Genetic Diversity')
plt.xlabel('Generation')
plt.ylabel('Metrics')
plt.title('Evolution of Bird Population Over Generations')
plt.legend()
plt.show()

# 7. Export Data
results_df.to_csv('bird_species_evolution.csv', index=False)
