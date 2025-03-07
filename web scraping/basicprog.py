import pandas as pd

provinces = ["Bagmati","Gandaki","koshi","Lumbini"]
population = [3000000, 2000000, 1500000, 2500000]

#  here i am creating a dictionary called dict_prvince
dict_prvince = {
    'Province': provinces,
    'population': population
}

# now i am creating a data frame...
df_prvince = pd.DataFrame.from_dict(dict_prvince)
print(df_prvince)

# now i am gonna export this output of this df_prvince to the csv file check the below code 

# these to_excel and to_csv are two different function that need two diff parameter ie filename, and engine while others require filename and index

df_prvince.to_excel('Prvince.xlsx' , engine='openpyxl') 
df_prvince.to_csv('Prvince.csv' , index=False) 


# print(provinces[0])

# # loop eg.
# for province in provinces:
#     # if stmt eg.
#     if province == "Lumbini":
#         print(f"It's my home...{province}")
        
#     print(province)

# # one of the simplest way to export the data in python is 
# with open('test.txt','w') as file:   # and this is a simple built in keywords inside the python
#     file.write("Data successfully written and scraped...!!")

