# this file is basically meant to convert a .csv file into a format that is able to be 
# represented in the markdown README. This has nothing to do with the mapping itself.

import pandas as pd
base_md = pd.read_csv("../data_tables/csv/all_bases.csv")
space_md = pd.read_csv("../data_tables/csv/all_spaces.csv")
print(base_md.to_markdown(index=False))
print("\n\n")
print(space_md.to_markdown(index=False))