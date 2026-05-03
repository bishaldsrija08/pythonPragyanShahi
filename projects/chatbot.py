responses = {
    "hello": "Hello! How can I assist you today?",
    "how are you?": "I'm just a chatbot, but I'm here to help you!",
    "what is your name?": "I am a simple chatbot created to assist you.",
    "what can you do?": "I can answer your questions and have a conversation with you.",
    "thank you": "You're welcome! If you have any more questions, feel free to ask.",
    "what is the weather like?": "I'm sorry, I don't have access to real-time weather information. You can check a weather website or app for the latest updates.",
    "help": "Sure! You can ask me anything or just have a chat with me.",
    "bye": "Goodbye! Have a great day!"
}

while True:
    user_input = input("You: ").lower()
    if user_input == "bye":
        print("Chatbot: " + responses["bye"])
        break
    elif user_input in responses:
        print("Chatbot: " + responses[user_input])
    else:
        print("Chatbot: I'm sorry, I don't understand that. Can you please rephrase?")