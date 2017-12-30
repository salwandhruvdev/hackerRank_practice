def array_left_rotation(a, n, k):
    # initial solution uses a new list 
    # initialized with zeros, containing 
    # same number of elements, iterate over 
    # index of 'a' and insert the values and 
    # the new index in the new list
    
    ret_list = [0 for i in range(1, len(a) + 1)]
    temp_index = 0
    for index, value in enumerate(a):
        temp_index = index - k
        ret_list[temp_index] = value
    
    return ret_list
                                 

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
