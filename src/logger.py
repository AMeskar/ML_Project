# logger python file to track our appilcation, anything happen will be tracked by this file

import logging
import os
from datetime import datetime

Log_F = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # create a .log file contain date.log

path_logf = os.path.join(os.getcwd(), 'log') # create a path /current directory/log

os.makedirs(path_logf, exist_ok= True) # Create the repository of all the directory and interlidiate directory

path_log_file = os.path.join(path_logf, Log_F) # create the whole path with the .log file in it

logging.basicConfig(
    
    filename= path_logf, # Take the path of the filename created
    
    format= "{asctime} - {levelname} - {message}", # the format base of the message
    
    level = logging.INFO(), # level mean which info the log will give u, .INFO, .DEBUG, .ERROR
    
)