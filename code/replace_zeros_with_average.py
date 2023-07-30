import pandas as pd

def replace_zeros_with_average(filename: str, columns: list[str])-> pd.DataFrame:
    """
    This function checks for zero values in the 'columns' of the csv file and replaces them with the average of rows above and below them.

    Arguments
    ----------
    filename: str
    the name of the CSV file 
    columns: list[str]
    the name of the columns

    Returned Values
    ----------
    data : pd.DataFrame
    the final DataFrame with nonzero values

    """
    data = pd.read_csv(filename)
    for i in columns:
        for ind in data.index:
            if data[i][ind]==0:
                data[i][ind] = (data[i][ind-1]+data[i][ind+1])/2
    data.to_csv(f"{filename}_updated.csv", index=False)
    
    return data
