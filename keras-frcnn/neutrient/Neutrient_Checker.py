import pandas as pd

input_tag = ["bulgogi", "gim", "rice"]

Category_list_male = pd.read_csv("category_male.csv")

input_neutrient_list = Category_list_male[Category_list_male['Tag'].isin(input_tag)]

input_neutrient_sum = input_neutrient_list.sum()

print(input_neutrient_sum)

input_neutrient_sum


Food_list = pd.read_csv('nutrients.csv')

print(Food_list)