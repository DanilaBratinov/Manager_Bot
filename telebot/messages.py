import web
import news

from user import get_name, get_id

def hello(message):
    hello_message = f"☘️Привет, {get_name(message)}"
    
    return hello_message