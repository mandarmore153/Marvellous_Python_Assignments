from functools import reduce

def MaxNo(No1, No2):       
    return max(No1, No2)

def MultiNo(No):
    return No * 2

def PrimeNo(No):
    
    chkprime = True
    for i in range(2, No):
        if No % i == 0:
            chkprime = False
            break
    
    if chkprime == True:    
        return No
     
   

def main():
    number = int(input("Enter a number: "))
    Input_list = [] 
    for i in range(number):
        Input_list.append(int(input()))
    
    print("Input Data :", Input_list)
    filter_data = list(filter(PrimeNo, Input_list))
    print("Filter Output :", filter_data)
        
    map_data = list(map(MultiNo, filter_data))   
    print("Map output : ", map_data) 

    red_data = reduce(MaxNo, map_data)
    print("Reduce output : ", red_data)

if __name__ == "__main__":
    main()    
