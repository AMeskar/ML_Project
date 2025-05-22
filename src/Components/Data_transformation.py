# After getting the ingestion you can then apply transformaton to the data 
# I need To take the data split it, transform it

from abc import ABC, abstractmethod
import sys
from src.logger import logging
from src.Components.Data_ingestion import TypeFile
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer, SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split

class DataTransformation(ABC):
    
    @abstractmethod
    def DataTra(self, file_path:str) -> pd.DataFrame:
        """
        
        """
        pass


class DataMissingValues(DataTransformation):
    
    def DataTra(self, file_path, df:pd.DataFrame) -> pd.DataFrame:
        
        """
        
        """
        
        df = TypeFile().Ingest(file_path=file_path)
        
        target = 'math_score'
        
        y = df[target]
        
        x = df.drop(columns=[target], axis=1)
        
        num_df = x.select_dtypes(exclude='object').columns
        
        cat_df = x.select_dtypes(include='object').columns
        
        if df.isnull().sum().all() > 0:
            
            num_pipeline = Pipeline(
                
                steps= [
                    
                    ('Impute', IterativeImputer()),
                    ('Scaling', StandardScaler())
                ] 
            )
            
            cat_pipeline = Pipeline(
                
                steps= [
                    
                    ('Impute', SimpleImputer(strategy= 'most_frequent')),
                    ('one hot encoding', OneHotEncoder())
                ] 
            )
           
        else: 
            
            num_pipeline = Pipeline(
                
                steps= [
                    
                    ('Scaling', StandardScaler())
                ] 
            )
            
            cat_pipeline = Pipeline(
                
                steps= [
                    
                    ('one hot encoding', OneHotEncoder())
                ] 
            )
            
        preprocessor = ColumnTransformer(
            [
                ("numerical pipline", num_pipeline, num_df),
                
                ('categorical pipline', cat_pipeline, cat_df)
            ]
        )
        
        x = preprocessor.fit_transform(x)
        
        return x, y

class traintestsplit(DataTransformation):
    
    def DataTra(self, file_path:str) -> pd.DataFrame:
        
        """
        
        """
        
        df = TypeFile().Ingest(file_path=file_path)
                    
        x, y = DataMissingValues().DataTra(file_path, df)

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0, shuffle=True)
        
        return x_train, x_test, y_train, y_test