from converters import dec_to_bin
from converters import bin_to_dec

import pandas as pd

# testing our convertes module
original = [str(dec) for dec in range(17+1)]
bins_list = [dec_to_bin(dec) for dec in original]
decs_list = [bin_to_dec(bin) for bin in bins_list]

my_matrix = [[bins_list[int(index)],decs_list[int(index)]] for index in original]

my_data = pd.DataFrame(data=my_matrix, index=original, columns=['binary','decimal'])
print(my_data)