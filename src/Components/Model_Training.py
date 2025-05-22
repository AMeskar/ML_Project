# Model 
from abc import ABC, abstractmethod
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

from sklearn.metrics import mean_squared_error, r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression, Ridge,Lasso
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import RandomizedSearchCV
from catboost import CatBoostRegressor
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split

from src.Components.Data_transformation import traintestsplit

class Model_l(ABC):
    
    @abstractmethod
    
    def Model(self, x_train, x_test, y_train, y_test, model): 
        
        '''
        
        '''
        
        pass

class CompteLoss(Model_l):
    
    def Model(self, y_train, y_test): 
        
        '''
        
        '''
        
        r2 = r2_score(y_train, y_test)
        
        mae = mean_absolute_error(y_train, y_test)
        
        mse = mean_squared_error(y_train, y_test)
        
        return r2, mae, mse

class FitModel:
    
    def Compute(self, x_train, x_test,  y_train, y_test, model): 
        
        '''
        
        '''
        out = []
        
        for name, m in model.items():
            
            m.fit(x_train, y_train)
            
            y_pred_train = m.predict(x_train)
            y_pred = m.predict(x_test)
            
            print(f'\n Model {name} ==> ')
            print('\n Model Performance on Trainig set')
            
            r2_train, mae_train, mse_test = CompteLoss().Model(y_train, y_pred_train)
            
            print(f'\n r square: {r2_train}, mean absolute error: {mae_train}, mean square error: {mse_test}')
            print('\n Model Performance on Testing set')
            
            r2_test, mae_test, mse_test = CompteLoss().Model(y_test, y_pred)
            
            print(f'\n r square: {r2_test}, mean absolute error: {mae_test}, mean square error: {mse_test}')
            
            out.append(r2_test)
            
        return m, out

