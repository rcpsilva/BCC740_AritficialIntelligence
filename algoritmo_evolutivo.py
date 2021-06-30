import numpy as np


def permGenerator(pop_size,n):
    return [np.random.permutation(n) for i in range(pop_size)]


def fitness(ind):

    fitness = 0
    for i in range(len(ind)-1):   # range(5) -> [0,1,2,3,4]
        for j in range(i+1, len(ind)): # range(3,6) -> [3,4,5] 
            deltax = abs(ind[i]-ind[j])
            deltay = abs(i-j) 
            if deltax == deltay:
                fitness -= 1

    return fitness

def mutation(ind):

    pos1 = np.random.randint(0,len(ind))
    pos2 = np.random.randint(0,len(ind))

    ind[[pos1,pos2]] = ind[[pos2,pos1]]
    
    return ind

def crossover(ind1, ind2):
    cut = np.random.randint(0,len(ind1)-1)

    off1 = np.copy(ind1)
    off2 = np.copy(ind2)

    for i in range(cut+1,len(off1)):
        off1[i] = -1
        off2[i] = -1 

    i = cut + 1
    j = cut + 1
    while i < len(ind1):
        if ind2[j] not in list(off1):
            off1[i] = ind2[j]
            i += 1
            j = (j+1)%len(ind2)
        else:
            j = (j+1)%len(ind2)

    i = cut + 1
    j = cut + 1
    while i < len(ind2):
        if ind1[j] not in list(off2):
            off2[i] = ind1[j]
            i += 1
            j = (j+1)%len(ind2)
        else:
            j = (j+1)%len(ind2)
            
    return  off1,off2

def tournament(parents,offspring):

    for i in range(len(parents)):
        if fitness(parents[i]) < fitness(offspring[i]):
            parents[i] = offspring[i].copy()
        
        
        



if __name__ == "__main__":
    pop_size = 5
    board_size = 6 
    pop = permGenerator(pop_size,board_size)
    
    mut = mutation(pop[0])

    print(pop[0])
    print(pop[1])

    ind1, ind2 = crossover(pop[0],pop[1])

    print(ind1)
    print(ind2)

   
    
    