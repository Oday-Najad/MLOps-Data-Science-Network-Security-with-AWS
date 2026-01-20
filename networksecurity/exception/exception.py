import sys
from networksecurity.logging.logger import logging


class NetworkSecurityException(Exception):
    def __init__(self, error_message: Exception, error_detail: sys):
        self.error_message = error_message
        __, _, exc_tb = error_detail.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.filename = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error occurred in script: {self.filename} at line number: {self.lineno} with message: {self.error_message}"


# if __name__ == "__main__":

#     try:
#         logging.info("Starting main execution")
#         a = 1 / 0
#         print("This will not be printed")
#     except Exception as e:
#         logging.info("An exception occurred")
#         raise NetworkSecurityException(e, sys)
#         logging.info("Exception details logged")
