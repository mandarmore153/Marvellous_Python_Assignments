def ChkPrime(input_elements):
    
    prime_number_list = []
    for i in input_elements:
        
        if i < 2:
            continue
        
        prime_number = True
        for j in range(2,i):        
            if (i % j) == 0:
                prime_number = False
                break
            
        if prime_number == True:   
            prime_number_list.append(i)
                 
    print("Prime number list is : ", prime_number_list)            
    return sum(prime_number_list)         