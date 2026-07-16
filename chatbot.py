import random
from datetime import datetime

print("=" * 40)
print("      Welcome to AI Chatbot")
print("Type 'bye' to exit.")
print("=" * 40)

jokes = [
    "Why did the computer get cold? Because it left its Windows open!",
    "Why do programmers prefer Python? Because it's easy to understand!",
    "Why was the computer late? It had too many tabs open!"
]

while True:
    user = input("\nYou: ").lower().strip()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    elif "how are you" in user:
        print("Bot: I'm doing great! How about you?")

    elif "name" in user:
        print("Bot: My name is CodSoft AI Chatbot.")

    elif "time" in user:
        print("Bot:", datetime.now().strftime("%I:%M %p"))

    elif "date" in user:
        print("Bot:", datetime.now().strftime("%d-%m-%Y"))

    elif "joke" in user:
        print("Bot:", random.choice(jokes))

    elif "python" in user:
        print("Bot: Python is a powerful programming language used in AI and Machine Learning.")

    elif "thank" in user:
        print("Bot: You're welcome!")

    elif user == "bye":
        print("Bot: Goodbye! Have a great day!")
        break

    else:
        print("Bot: Sorry, I don't understand that. Please try another question.")