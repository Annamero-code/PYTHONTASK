def sum_even_element(lists):
    even = 0
    for numbers in lists:
        if numbers % 2 == 0:
            even += numbers 
        
    return even

