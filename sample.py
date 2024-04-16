from barracudas import fysh

#Initialize the variables
port = ’?’ # Mostly, it would be this '/dev/ttyACM0'
g_limit = ’?’# 0 to 1
token = ’?’ # your_api_token'
chat_id = ’?’ # your_chat_id'
delay = ’?’ # Seconds

#Call the function with variables
fysh.fysh(port, g_limit, token, chat_id, delay)
