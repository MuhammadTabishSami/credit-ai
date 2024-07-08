import sys
import logging
from src.logger import logging

def error_message_detail(error,error_detail):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error Occurred in Python Script[{0}] line number[{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)) 
    
    return error_message
    

class CustomException(Exception):
    def __init__(self,error_message,error_detail): #:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
if __name__ == '__main__':
    try:
        raise ValueError("Example Error")
    except ValueError as e:
            error_detail=sys.exc_info()
            custom_exception= CustomException(str(e),error_detail)
            logging.error(str(custom_exception))
            
    
        