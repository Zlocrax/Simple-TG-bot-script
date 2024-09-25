import requests

def get_user_ip(bot_token):
    """
    This function retrieves the IP address of the user interacting with a Telegram bot.
    
    Parameters:
    bot_token (str): The token of the Telegram bot
    
    Returns:
    str: The IP address of the user
    """
    try:
        # Make a request to the Telegram Bot API to get the user's IP address
        response = requests.get(f"https://api.telegram.org/bot{bot_token}/getMe")
        
        # Check if the request was successful
        if response.status_code == 200:
            # Extract the IP address from the response
            ip_address = response.json()["result"]["ip_address"]
            return ip_address
        else:
            raise Exception("Failed to retrieve the user's IP address")
    except Exception as e:
        # Log the error
        print(f"Error: {e}")
        return None
