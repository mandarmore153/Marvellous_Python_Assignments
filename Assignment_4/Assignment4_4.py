from functools import reduce
# def Add(No1, No2):
#     return No1 + No2

# def SquareNo(No):
#     return No ** 2

# def EvenNo(No):
#     if No % 2 == 0:
#         return No
  
EvenNo = lambda No : (No % 2 == 0)
SquareNo = lambda No : No ** 2  
Add = lambda No1, No2 : No1 + No2    

def main():
    number = int(input("Enter a number: "))
    Input_list = [] 
    for i in range(number):
        Input_list.append(int(input()))
    
    print("Input Data :", Input_list)
    filter_data = list(filter(EvenNo, Input_list))
    print("Filter Output :", filter_data)
        
    map_data = list(map(SquareNo, filter_data))   
    print("Map output : ", map_data) 

    red_data = reduce(Add, map_data)
    print("Reduce output : ", red_data)

if __name__ == "__main__":
    main()    
