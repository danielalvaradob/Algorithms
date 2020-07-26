# https://www.youtube.com/watch?v=5o-kdjv7FD0
#
#
#


def num_ways(n):
    if n == 1 or n == 0:
        return 1
    else:
        return num_ways(n-1) + num_ways(n-2)




memory = {}

# Optimized way using dinamic memory
def num_ways2(n):
    if n in memory:
        return memory[n]
    
    # compute the term
    if n == 0 or n ==1:
        value = 1
    elif n >=  2: 
        value = num_ways2(n-1) + num_ways2(n-2)
    
    #  dynamic memory values
    memory[n] = value
    return value


if __name__ == "__main__":
    print(num_ways(4))
    print(num_ways2(11))

