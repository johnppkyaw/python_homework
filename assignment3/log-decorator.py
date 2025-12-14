#Task 1: Writing and Testing a Decorator

import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

def logger_decorator(func):
  def wrapper(*args, **kwargs):
    logger.log(logging.INFO, f"function: {func.__name__}")
    value = func(*args, **kwargs)
    if(len(args) > 0):
      logger.log(logging.INFO, f"positional parameters: {args}")
    else:
      logger.log(logging.INFO, f"positional parameters: none")
    if(len(kwargs) > 0):
      logger.log(logging.INFO, f"keyword parameters: {kwargs}")
    else:
      logger.log(logging.INFO, f"keyword parameters: none")
    logger.log(logging.INFO, f"return: {value}")
  return wrapper
    
@logger_decorator
def hello():
  return "Hello, World!"  

@logger_decorator
def takes_args(*args):
  return True

@logger_decorator
def takes_kwargs(**kwargs):
  return logger_decorator

hello()
takes_args(1, 2, 3, 4)
takes_kwargs(key1 = "lock2", key2 = "lock3")
