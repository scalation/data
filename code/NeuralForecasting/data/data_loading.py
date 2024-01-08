import pandas as pd

def load_data(data_file: str, columns = None, skip: int = 0, sort: bool = False, date: str = 'date', target: str = 'target') -> pd.DataFrame:
    """
    A function used for loading the data file and selecting features for training 

    Arguments
    ----------
    data_file: str
        the name of the dataset 
    columns: list[str]
        columns used for training in the multivariate setting
    skip: int
        ignore the first skip rows
    date: str
        the name of the date/time column 
    target: str
        the name of the main target column for evaluation e.g. new_deaths for the COVID dataset
           
    Returned Values
    ----------
    data : pd.DataFrame

    """
    data = pd.read_csv(data_file)
    data[date] = pd.to_datetime(data[date])           #convert string to datetime
    data[date] = [d.date() for d in data[date]]       #convert datetime to date
    data = data.iloc[skip:]                           #keep index location skip to end
    data.reset_index(inplace = True, drop = True) 
    if sort:
        data = data.sort_values(by = date)            #sort by date just to make sure
    if columns is None:
        columns = data.columns
    data = data[columns]                              #keep the column you want
    observed = data[[date, target]]
    return data, observed

def plot_data(data: pd.DataFrame):
    """
    A function used for plotting the data

    Arguments
    ----------
    data: DataFrame
        the name of the dataset 
        
    Returned Values
    ----------
    
    """
    return data.plot(subplots = True, figsize = (10, 12))
