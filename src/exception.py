import sys 
from src.logger import logging

def error_detail_message(error,error_message:sys):
    _,_,exc_tb = error_message.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    error_message = "error occured in python script name [{0}] line no [{1}] error detail [{2}]".format(file_name,line_no,error)

    return error_message

class HeartDiseaseError(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_detail = error_detail_message(error_message,error_detail)

    def __str__(self):
        return self.error_detail
    
