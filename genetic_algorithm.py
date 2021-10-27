# Criar uma população de indivíduos
# Seleção
# Mutação
# Cruzamento
# Fitness

import copy as cp
import numpy as np
import matplotlib.pyplot as plt

def crossover(ind1, ind2):

    p1 = np.random.randint(len(ind1))
    p2 = np.random.randint(len(ind1))

    while p1 == p2:
        p2 = np.random.randint(len(ind1))
    
    if p1 > p2:
        p1,p2 = p2,p1

    off1 = []
    off2 = []

    for i in range(0,p1):
        off1.append(ind1[i])
        off2.append(ind2[i]) 

    for i in range(p1,p2):
        off1.append(ind2[i])
        off2.append(ind1[i])

    for i in range(p2, len(ind1)):
        off1.append(ind1[i])
        off2.append(ind2[i])

    return off1, off2

def mutation(ind):
    
    _ind = cp.copy(ind)
    n = len(ind)

    queen = np.random.randint(n)
    pos = np.random.randint(n)

    _ind[queen] = pos

    return _ind


def fitness(ind):
    # ind = [1,1,3,4]

    conflicts = 0

    for i in range(len(ind)):
        for j in range(len(ind)):
            if i!=j:
                # Check same column conflict
                if ind[i] == ind[j]:
                    conflicts +=1
                
                # Check diagonal conflict 
                if abs(ind[i]-ind[j]) == abs(i-j):
                    conflicts +=1

    return -conflicts


def evolve(pop,ngen=10,prob_mut=0.05):
    
    best_ind = []
    best_fitness = 0

    best_fit_bygen = []

    for i in range(ngen):  
        newpop = []     
        for ind in pop:
            off1,off2 = crossover(ind,pop[np.random.randint(len(pop))]) 

            if np.random.rand() < prob_mut:
                 off1 = mutation(off1)

            if np.random.rand() < prob_mut:
                 off2 = mutation(off2)

            champion = off1 if fitness(off1) >= fitness(off2) else off2

            champion = champion if fitness(champion) >= fitness(ind) else ind
    
            newpop.append(champion)

            if not best_ind:
                best_ind = champion
                best_fitness = fitness(champion)
            elif fitness(champion) >= best_fitness:
                best_ind = champion
                best_fitness = fitness(champion)

        
        best_fit_bygen.append(best_fitness)
        pop = newpop.copy()

    return best_fitness,best_ind,best_fit_bygen


if __name__ == "__main__":

    print(fitness([1,1,1,1]))

    print(mutation([1,1,1,1]))

    o1, o2 = crossover([1,1,1,1,1,1,1,1],[2,2,2,2,2,2,2,2])

    print(o1)
    print(o2)
 
    n = 12
    popsize = 50
    pop = [[np.random.randint(n) for i in range(n)] for j in range(popsize)]

    for ind in pop:
        print(ind)

    best_fitness,best_ind,best_fit_bygen = evolve(pop,ngen=500,prob_mut=0.5)

    print(best_fitness)
    print(best_ind)

    plt.plot(best_fit_bygen)
    plt.show()