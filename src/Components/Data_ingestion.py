# Reading the data for database, path any source in a way seperated by the notebook

from abc import ABC, abstractmethod
import zipfile
from src.exception import CustomizeExcep
from src.logger import logging
import pandas as pd
import os

class DataIngestion(ABC):
    
    @abstractmethod
    
    def Ingest(self, file_path: str) -> pd.DataFrame :
        
        '''
        Take the file path and extract the data 
        
        retun: List of files
        
        '''
        
        pass

class ZipFileReader(DataIngestion):
    
    def Ingest(self, file_path: str) -> pd.DataFrame :
        
        '''
        Take the file path and extract the data 
        
        retun: List of files
        
        '''
        
        logging.info('Reading the zip file')
        
        with zipfile.ZipFile(file_path, 'r') as F:
            
            csv_files = F.extractall('Extracted_zipdata')
        
        extract_file = os.listdir('Extracted_zipdata')
        
        out = [c for c in extract_file if c.endswith('.csv')]
        
        if len(out) == 0:
        
            return CustomizeExcep(ValueError('No csv file in the zip file'))
        
        elif len(out) > 1 :
            
            return csvFileReader().Ingest(os.path.join("Extracted_zipdata", out[0]))    
        
        else: return csvFileReader().Ingest(os.path.join("Extracted_zipdata", out[0]))

class csvFileReader(DataIngestion):
    
    def Ingest(self, file_path: str) -> pd.DataFrame :
        
        '''
        Take the file path and extract the data 
        
        retun: List of files
        
        '''
        logging.info('Create the Data Frame')
        
        df = pd.read_csv(file_path)
        
        return df

class TypeFile:
    
    def Ingest(self, file_path: str) -> pd.DataFrame :
        
        '''
        Take the file path and extract the data 
        
        retun: List of files
        
        '''
        
        logging.info('Reading the extention of the file')
        
        file_ext = os.path.splitext(file_path)[1]
  
        if file_ext.endswith('.zip'):
            
            return ZipFileReader().Ingest(file_path=file_path)
        
        elif file_ext.endswith('.csv'):

            return csvFileReader().Ingest(file_path=file_path)

