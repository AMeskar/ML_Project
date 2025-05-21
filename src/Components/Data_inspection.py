from abc import ABC, abstractmethod
import pandas as pd

class DataFrameInspection(ABC):
    
    @abstractmethod
    
    def Inspect(self, df: pd.DataFrame):
        '''
        Function to inspect data
        
        return: general describtion or statistical describtion
        
        '''
        pass

class GeneralInspect(DataFrameInspection):
    
    def Inspect(self, df: pd.DataFrame):
        '''
        Function to inspect data
        
        return: general describtion or statistical describtion
        
        '''
        print("=== General description to the data ===")
        
        print(df.info())

class SatatisticalInspect(DataFrameInspection):
    
    def Inspect(self, df: pd.DataFrame):
        '''
        Function to inspect data
        
        return: general describtion or statistical describtion
        
        '''
        
        print("=== Statistical description to the data ===")
        
        print('numerical stat ==>')
        
        print('\n', df.describe())
        
        print('Categorical stat ==>')
        
        print(df.describe(include=["O"]))
                
class SetDataDescription:
    
    def __init__(self, description_method: DataFrameInspection):
        
        self._description_method = description_method
    
    def changeDataDescription(self, description_method: DataFrameInspection):
        
        self._description_method = description_method
    
    def execute(self, df: pd.DataFrame):
        
        self._description_method.Inspect(df)
        
        