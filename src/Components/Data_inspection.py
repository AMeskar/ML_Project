from abc import ABC, abstractmethod
import pandas as pd

class DataFrameInspection(ABC):
    
    @abstractmethod
    
    def Inspect(self, df: pd.DataFrame):
        
        pass