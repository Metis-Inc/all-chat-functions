import requests

# Base URL and headers
base_url = "https://api.metisai.ir/api/v1/chat"
api_key = "YOUR_API_KEY"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Function to create a chat session
def create_chat_session(bot_id, user=None, initial_messages=None):
    """
    Create a new chat session.
    """
    url = f"{base_url}/session"
    data = {
        "botId": bot_id,
        "user": user,
        "initialMessages": initial_messages or []
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

# Function to send a message in a chat session
def send_message(session_id, content, message_type="USER"):
    """
    Send a message in a chat session.
    """
    url = f"{base_url}/session/{session_id}/message"
    data = {
        "message": {
            "content": content,
            "type": message_type
        }
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()


# Function to get chat session information
def get_chat_session_info(session_id):
    """
    Get information about a chat session.
    """
    url = f"{base_url}/session/{session_id}"
    response = requests.get(url, headers=headers)
    return response.json()

# Function to get list of chat sessions for a bot
def get_chat_sessions_for_bot(bot_id, page=0, size=10):
    """
    Get a list of chat sessions for a bot.
    """
    url = f"{base_url}/session?botId={bot_id}&page={page}&size={size}"
    response = requests.get(url, headers=headers)
    return response.json()

# Function to get list of chat sessions for a user
def get_chat_sessions_for_user(user_id, page=0, size=10):
    """
    Get a list of chat sessions for a user.
    """
    url = f"{base_url}/session?userId={user_id}&page={page}&size={size}"
    response = requests.get(url, headers=headers)
    return response.json()

# Function to delete a chat session
def delete_chat_session(session_id):
    """
    Delete a chat session.
    """
    url = f"{base_url}/session/{session_id}"
    requests.delete(url, headers=headers)
    

# Main section to test all functions
if __name__ == "__main__":
    bot_id = "BOT_ID"
    user_id = {"name":"Metis", "id":"metis_ai"}
    session_id = None

    # Create a chat session
    print("Creating chat session...")
    session = create_chat_session(bot_id)
    print(session)
    session_id = session.get("id")

    # Send a message in the chat session
    if session_id:
        print("Sending message...")
        message_response = send_message(session_id, "Hello!")
        print(message_response)

        # Get chat session information
        print("Getting chat session information...")
        session_info = get_chat_session_info(session_id)
        print(session_info)

        # Get list of chat sessions for the bot
        print("Getting list of chat sessions for the bot...")
        bot_sessions = get_chat_sessions_for_bot(bot_id)
        print(bot_sessions)

        # Get list of chat sessions for the user
        print("Getting list of chat sessions for the user...")
        user_sessions = get_chat_sessions_for_user(user_id)
        print(user_sessions)

        # Delete the chat session
        print("Deleting chat session...")
        delete_response = delete_chat_session(session_id)
        print("Session deleted successfully!")
    else:
        print("Failed to create chat session.")
