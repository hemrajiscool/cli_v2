from ai_client import APIclient
from agent import Agent

ai_client = APIclient()
agent = Agent(ai_client)


while True:
    user_input = input("User: ")
    if user_input == "exit":
        break
    response = agent.chat(user_input)
    print(f"AI: {response}")