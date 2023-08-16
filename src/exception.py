import sys

def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    
    filename = exc_tb.tb_frame.f_code.co_filename
    error_msg = "Error occured in file [{0}] line number [{1}] error mesage [{2}]".format(filename, exc_tb.lineno, str(error))
    return error_msg
    
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super.__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        
    def __str__(self):
        return self.error_message