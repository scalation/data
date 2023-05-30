def data_processing_viz(data_file:str, columns:list[str], skip:int=0, date:str='date') -> pd.DataFrame:
    """
    A function used for data processing and visualization
    
    Required Imports
    ----------
    import pandas as pd

    Arguments
    ----------
    data_file : str
        a formatted string to print out what the animal says
    columns : list[str]
        the name of the animal
    skip : int
        ignore the first skip rows
    date : str
        the sound that the animal makes
        
    Returned Values
    ----------
    data : pd.DataFrame

    """
    data = pd.read_csv(data_file)
    data[date] = pd.to_datetime(data[date])       #convert string to datetime
    data[date] = [d.date() for d in data[date]]   #convert datetime to date
    data = data.iloc[skip:]                       #keep index location skip to end
    data.reset_index(inplace = True, drop = True)  
    data = data.sort_values(by = date)            #sort by date just to make sure
    data = data[columns]                          #keep the column you want
    data.plot(subplots = True, figsize = (10, 12))
    return data
