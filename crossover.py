from typing import List, Tuple
import itertools

def cycle(p1: List[int], p2: List[int]) -> Tuple[List[int], List[int]]:
    n = len(p1)

    start = 0
    cycles = []
    while True:
        # We went out of population
        if start >= n:
            break

        # Initialize cycle
        this_cycle = [0]*n
        
        # Start looking for cycles 
        first_allele = p1[start]
        allele = first_allele
        it = 0
        while True:
            # Check if cycle closed
            if it != 0 and allele == first_allele:
                start += 1
                # Make sure cycle is unique
                if this_cycle not in cycles: # TODO not efficient at all
                    cycles.append(this_cycle)
                break
            p1_idx = p1.index(allele)
            this_cycle[p1_idx] =  allele
            p2_idx = p2.index(allele)
            allele = p1[p2_idx]
            it += 1
        
        # Check if single element cycle 
        if len([v for v in this_cycle if v != 0]) <=1:
            break
    
    # Generators for parents switching
    p1_generator = itertools.cycle([p1,p2])
    p2_generator = itertools.cycle([p2,p1])
    
    child1 = [-1]*n
    child2 = [-1]*n
    
    for _cycle in cycles:
        _p1 = next(p1_generator)
        _p2 = next(p2_generator)
        for i, allele in enumerate(_cycle):
            if allele == 0:
                continue
            child1[i] = _p1[i]
            child2[i] = _p2[i]

    return child1, child2
