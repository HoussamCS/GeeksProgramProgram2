import random
import time

# --- Step 1: Gene class ---
class Gene:
    def __init__(self, value=None):
        self.value = random.choice([0, 1]) if value is None else value

    def mutate(self):
        """Flip the gene value"""
        self.value = 1 - self.value

    def __repr__(self):
        return str(self.value)


# --- Step 2: Chromosome class ---
class Chromosome:
    def __init__(self, genes=None):
        self.genes = genes if genes else [Gene() for _ in range(10)]

    def mutate(self):
        """Each gene has a 50% chance to flip"""
        for gene in self.genes:
            if random.random() < 0.5:
                gene.mutate()

    def is_all_ones(self):
        return all(gene.value == 1 for gene in self.genes)

    def __repr__(self):
        return ''.join(str(gene.value) for gene in self.genes)


# --- Step 3: DNA class ---
class DNA:
    def __init__(self, chromosomes=None):
        self.chromosomes = chromosomes if chromosomes else [Chromosome() for _ in range(10)]

    def mutate(self):
        """Each chromosome has a 50% chance to mutate"""
        for chromosome in self.chromosomes:
            if random.random() < 0.5:
                chromosome.mutate()

    def is_all_ones(self):
        return all(chromosome.is_all_ones() for chromosome in self.chromosomes)

    def __repr__(self):
        return '\n'.join(str(chromosome) for chromosome in self.chromosomes)


# --- Step 4: Organism class ---
class Organism:
    def __init__(self, dna, environment_factor):
        self.dna = dna
        self.environment_factor = environment_factor

    def mutate(self):
        """Mutate based on environment probability"""
        if random.random() < self.environment_factor:
            self.dna.mutate()


# --- Step 5: Simulation with visible progress ---
def simulate_evolution(population_size=10, environment_factor=0.8, max_generations=1000):
    population = [Organism(DNA(), environment_factor) for _ in range(population_size)]
    generation = 0

    while generation < max_generations:
        generation += 1
        print(f"🧬 Generation {generation} ...")

        for organism in population:
            organism.mutate()
            if organism.dna.is_all_ones():
                print(f"\n✅ Evolution complete after {generation} generations!")
                print("Winning DNA:\n")
                print(organism.dna)
                return generation

        time.sleep(0.05)  # Small delay so output is readable

    print("\n❌ Evolution stopped after reaching the generation limit.")
    return None


if __name__ == "__main__":
    simulate_evolution(population_size=10, environment_factor=0.9, max_generations=200)
