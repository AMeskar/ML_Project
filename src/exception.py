# Python file handling errors and raise them in our customely message, we took the error from the class Exception and raise them in our way

import sys # This libraray interact with python, can so a lot of things but here it gives us the information about the error

def Error_message(error, error_detail= sys.exc_info()): # sys.exc_info() all the details are here
    
    _,_, exc_tbh = error_detail # exc_type, exc_value, exc_traceback, type and value no need we need just location
    
    # Condition
    
    if exc_tbh is not None:
        
        filename_excp = exc_tbh.tb_frame.f_code.co_filename # which file has the error
        
        Line_num_excp = exc_tbh.tb_lineno # the line number which have the error
    
    error_message = "The error is in the file [{0}] line number [{1}] and the error detail: [{2}]".format(filename_excp, Line_num_excp, str(error)) # our customize exception message
    
    return error_message

# Now lets call it and print it 

class CustomizeExcep(Exception):
    
    # create a class with a constructor to initialize the message 
    
    def __init__(self, error_message, error_detail = sys.exc_info()):
        super().__init__(error_message) # initilize or inhirit the __init__function from Exception class
        
        self.error_message = Error_message(error_message, error_detail= error_detail )
        # __init__ take the error message and error detail and feed them to the error message function
    
    def __str__(self):
        return super().__str__()
    
    # for excuting the class and print the message    
        