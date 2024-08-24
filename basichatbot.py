import nltk # type: ignore
from nltk.chat.util import Chat, reflections # type: ignore

# Ensure NLTK packages are downloaded
nltk.download('punkt')

# Define a set of pairs (input patterns and responses)
pairs = [
    [
        r"(hi|hello|hey|hola|howdy)",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created by you.", "You can call me Chatbot.", "I'm your assistant."]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm great! How about you?", "Feeling chatty!"]
    ],
    [
        r"what can you do ?",
        ["I can chat with you and help you with basic tasks.", "I'm here to assist you with anything I can."]
    ],
    [
        r"(.*) your name ?",
        ["My name is Chatbot.", "I'm called Chatbot."]
    ],
    [
        r"(.*) created you ?",
        ["I was created by Labhansh Goyal.", "Labhansh Goyal built me using Python."]
    ],
    [
        r"sorry (.*)",
        ["It's okay.", "No problem!", "Don't worry about it."]
    ],
    [
        r"thank you(.*)",
        ["You're welcome!", "Anytime!", "No problem!"]
    ],
    [
        r"quit",
        ["Goodbye! Have a nice day.", "Bye! Take care.", "See you soon!"]
    ],
    [
        r"(.*)",
        ["I'm not sure how to respond to that.", "Can you tell me more?", "Interesting, tell me more!"]
    ]
]

# Create a chatbot instance with the pairs and reflections
chatbot = Chat(pairs, reflections)

# Start the conversation
def chatbot_conversation():
    print("Chatbot: Hi there! I am your friendly chatbot. Type 'quit' to end the conversation.")
    while True:
        user_input = input("You: ").lower()
        if user_input.strip() == "quit":
            print("Chatbot: Goodbye! Have a nice day.")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot_conversation()