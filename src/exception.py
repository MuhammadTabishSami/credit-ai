import sys
import logging

def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in script: [{file_name}] at line number: [{line_number}] error message: [{str(error)}]"
    return error_message
    
    # if exc_tb is not None:
    #     file_name = exc_tb.tb_frame.f_code.co_filename
    #     error_message = "Error occurred in Python Script[{0}] line number[{1}] error message[{2}]".format(
    #         file_name, exc_tb.tb_lineno, str(error))
    # else:
    #     error_message = f'Error occurred: {str(error)}'
    # return error_message

import sys

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = self.error_message_detail(error_message, error_detail)

    def error_message_detail(self, error_message, error_detail: sys):
        _, _, exc_tb = error_detail.exc_info()  # Correct way to access exception details        
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        error_message = f"Error occurred in script: [{file_name}] at line number: [{line_number}] error message: [{error_message}]"
        return error_message

    def __str__(self):
        return self.error_message


if __name__ == '__main__':
    try:
        raise ValueError("Example Error")
    except ValueError as e:
        error_detail = sys.exc_info()
        custom_exception = CustomException(str(e), error_detail)
        logging.error(str(custom_exception))
