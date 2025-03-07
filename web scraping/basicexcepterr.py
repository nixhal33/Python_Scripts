rand_list=[2,3,4,5,6, 'California']

for element in rand_list:
    try:
        print(element/2)
    except:
        print("Please enter a valid number...!!!")


# while break statement uses
n=10
while n>0:
    print(f'Yes n ie. {n} is greater.')
    n=n-1
    print(f"But i am deducting the n until it becomes {n} or dissatisfies the condition")
    
    #  here if n==5 then break means if the condition reaches the 5 then then this block exits the code execution
    # if n==5:
    #     break

print("finally 0 came huh!!!")