import numpy as np
import pandas as pd

# 1. Create a Series
data = np.array([10, 20, 30, 40, 50])
series = pd.Series(data)

# 2. Assign index labels
index = ['a', 'b', 'c', 'd', 'e']
series.index = index

# 3. Select values for 'b' and 'e'
values_b_e = series[['b', 'e']]
print(values_b_e)

# 4. Check if the Series contains the value 20
contains_20 = 20 in series.values
print(contains_20)

# 5. Check if the Series contains the values 15 and 20
contains_15_20 = np.isin(series, [15, 20])
print(contains_15_20)

# 6. Add 5 to each element
series = series + 5
print(series)

# 7. Convert Series to dictionary
series_dict = dict(zip(series.index, series.values))
print(series_dict)

# 8. Create Series from a dictionary
dictionary = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50, 'f': 60}
series_new = pd.Series(dictionary)
print(series_new)

# 9. Check for null values
is_null = series.isnull()
not_null = series.notnull()
print(is_null)
print(not_null)

# 10. Create another Series
data2 = np.array([20, 30, 40, 50, 60])
series2 = pd.Series(data2)

# 11. Assign index labels to the second Series
index2 = ['b', 'c', 'd', 'e', 'f']
series2.index = index2

# 12. Add the two Series together
sum_series = series + series2
print(sum_series)

# 13. Find unique values in the Series
unique_values = np.unique(series)
print(unique_values)

# 14. Sort the Series in ascending order
sorted_series = pd.Series(np.sort(series.values))
print(sorted_series)

# 15. Save the Series to a text file
np.savetxt('series_data.txt', series.values, delimiter='\t')
