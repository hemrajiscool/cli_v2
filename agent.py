from ai_client import APIclient
class Agent:
    def __init__(self, ai_client):
        self.ai_client = ai_client
        self.messages = []

    def chat(self, user_input):
        
        self.messages.append({
            "role": "user",
            "content": user_input
        })
        response = self.ai_client.generate(self.messages)
        self.messages.append({
            "role": "assistant",
            "content": response
        })
        return response
        