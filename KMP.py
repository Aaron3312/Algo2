def prefix_search(pattern, m, store_prefx):
    length = 0
    store_prefx[0] = 0
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            store_prefx[i] = length
        else:
            if length != 0:
                length = store_prefx[length - 1]
                i -= 1
            else:
                store_prefx[i] = 0
        i += 1  

def pattern_search(orgn_string, patt, loc_array):
    n = len(orgn_string)
    m = len(patt)
    i = j = location = 0
    prefix_array = [0] * m
    
    prefix_search(patt, m, prefix_array)
    
    while i < n:
        if orgn_string[i] == patt[j]:
            i += 1
            j += 1
        if j == m:
            loc_array[location] = i - j
            location += 1  
            j = prefix_array[j - 1]
        elif i < n and patt[j] != orgn_string[i]:
            if j != 0:
                j = prefix_array[j - 1]
            else:
                i += 1
                
    return location

def main():
    # declare the original text
    orgn_str = "aabbaaccaabbaadde"
    # pattern to be found
    patrn = "aabbaa"
    # array to store the locations of the pattern
    location_array = [0] * len(orgn_str)
    index = pattern_search(orgn_str, patrn, location_array)
    
    for i in range(index):
        print("Pattern found at location:", location_array[i])

if __name__ == "__main__":
    main()