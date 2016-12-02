import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


data_list = []
for year in range(1924, 2013, 4):
    year = str(year)

    header = pd.read_csv(year +".csv", nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()

    df = pd.read_csv(year +".csv", index_col = 0,
              thousands = ",", skiprows = [1])

    df.rename(inplace = True, columns = d) # rename to democrat/republican
    df.dropna(inplace = True, axis = 1)    # drop empty columns
    df["Year"] = year

    data_list.append(df[["Democratic", "Republican", "Total Votes Cast", "Year"]])

    new = pd.concat(data_list)

    new["Republican Vote Share"] = new["Republican"]/new["Total Votes Cast"]

    print(new)

    graph = new[new.index=="Accomack County"].plot(x="Year", y="Republican Vote Share")
    graph.get_figure().savefig('voteshare.pdf')
    ### Aren't the instructions clear on the filename accomack.png?
    
