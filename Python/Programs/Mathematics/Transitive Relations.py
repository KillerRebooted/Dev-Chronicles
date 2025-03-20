import time
import multiprocessing

n = 5

def set_creation(n):
    global set

    set = {(a, b) for a in range(n) for b in range(n)}

    return set

def is_transitive(check_set):

    for a, b in check_set:
        b_never_c = True
        for c, d in check_set:
            if (b is c) and ((a, d) in check_set):
                pass
            elif (b is c):
                b_never_c = False

        if not b_never_c:
            return False

    return True

def check_subsets(n_square, start, end, check_set = set_creation(n)):

    transitive = 0

    for iter in range(start, end):

        binary = bin(iter)[2:]
        binary = "0"*(n_square-len(binary)) + binary
        
        subset = []

        for ind, value in enumerate(check_set):
            if int(binary[ind]):
                subset.append(value)

        transitive += is_transitive(subset)

    return transitive

if __name__ == '__main__':

    start_time = time.time()

    n_square = n**2
    cardinality_of_power_set = 2**(n**2)

    skip = 1000000

    input_values = [(n_square, start, start+skip) if start+skip<cardinality_of_power_set else (n_square, start, cardinality_of_power_set) for start in range(0, cardinality_of_power_set, skip)]
    
    with multiprocessing.Pool(cardinality_of_power_set//1000000 + 1) as pool:
        thread = pool.starmap(check_subsets, input_values)

    end_time = time.time()
    print(f"Number of Transitive Relations for n = {n} is {sum(thread)}")
    print(f"Execution Time: {round(end_time-start_time, 3)} Seconds")