from functools import reduce
def Product(No1, No2):
    return No1 * No2

def AddOne(No):
    return No + 10

def NumberGtrOrle(No):
    if No >=70 and No <= 90:
        return No
    

def main():
    number = int(input("Enter a number: "))
    Input_list = [] 
    for i in range(number):
        Input_list.append(int(input()))
    
    print("Input Data :", Input_list)
    filter_data = list(filter(NumberGtrOrle, Input_list))
    print("Filter Output :", filter_data)
        
    map_data = list(map(AddOne, filter_data))   
    print("Map output : ", map_data) 

    red_data = reduce(Product, map_data)
    print("Reduce output : ", red_data)

if __name__ == "__main__":
    main()    
