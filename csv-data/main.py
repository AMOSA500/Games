import csv
import pandas

# # with open('weather.data.csv', mode='r') as data_file:
# #     file = csv.reader(data_file)
# #     for data in file:
# #         print(data[1])
#
# data = pandas.read_csv('weather.data.csv')
# print('-'*30)
# # Pandas can be converted to dict or other format data_dict = data.to_dict()
# # Read the documentation for more options
#
# # Find the mean temperature of the weather
# print(data['data'].mean(), 'Mean')
# print(data['data'].median(), 'Median')
#
#
# # Getting row with pandas
# print('-'*30)
# max_temp = data.data.max()
# max_data = data[data.data == max_temp]
# print(max_data)
# print('='*30)
# print('Convert to Fahrenheit', max_data.data)
# fahr = (max_data.data * 9 / 5) + 32
# print(fahr)
# print(f'Fahrenheit = {fahr}')
# print('-'*30)
#
# # Get the average
# len_data_li = data['data'].to_list()
# len_data = len(len_data_li)
# sum_data = sum(data['data'])
# avg_data = round((sum_data/len_data),2)
# print(f'Length: {len_data} and Sum: {sum_data} - Avg Data: {avg_data}')
#
# # Alternative way of working with data
# print(f'Alternative way to sum: {sum(data.data)}')

# Creating a DataFrame from Squirrel dataset
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
grey_squirrel = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_squirrel = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrel = len(data[data['Primary Fur Color'] == 'Black'])

# DataFrame
new_data_dict = {
    'Squirrel Color': ['Gray', 'Cinnamon', 'Black'],
    'Squirrel Count': [grey_squirrel, cinnamon_squirrel, black_squirrel]
}

sq_dataframe = pandas.DataFrame(new_data_dict)
sq_dataframe.to_csv('CP_Squirrel_census.csv', index=True, index_label='SN')
