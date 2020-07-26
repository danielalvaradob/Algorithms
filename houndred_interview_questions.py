# global variables


# 3 
# How do you count the occurrence of a given character in a string?
def count_occurrence(_string):
    occurrences = {} 
    for ch in _string:
        if ch in occurrences:
            occurrences[ch] += 1
        else:
            occurrences[ch] = 1
    
    return occurrences

# 4 
# How do you print the first non-repeated character from a string?
def first_non_repeated(_string):
    non_repeated = []
    for ch in _string:
        if ch not in non_repeated:
            non_repeated.append(ch)
        else:
            non_repeated.remove(ch)
    
    element = None
    print(non_repeated)
    if non_repeated != []:
        element = non_repeated.pop(0)
    
    return element

# 5
# How do you convert a given String into int like the atoi()? 
def atoi(_string):
    for i in range(len(_string)):
        pass

        

if __name__ == "__main__":
    s1 = "My name is Danielito, I have one brother named Manrique"
    print("String: ", s1)
    occ = count_occurrence(s1)
    print(occ)

    s2 = "aaabbbasasdib;uerplasdnyueq."
    print("First non repeated: %c" % (first_non_repeated(s2)))

