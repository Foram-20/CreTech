import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    # Greetings
    [r"hi|hello|hey|hii", ["Hello!", "Hi there!", "Hey! How can I help you today?"]],

    # Identity
    [r"(what is|what's)? ?your name\??", ["I am a simple chatbot.", "You can call me ChatBot."]],
    [r"who (made|created) you\??", ["I was created using Python and NLTK.", "A developer made me to chat with users like you."]],

    # Emotions
    [r"(how are you|how r u|how are u)\??", ["I'm doing well, thank you!", "Feeling chatty today!", "I'm fine. How can I assist you today?"]],
    [r"i am (.*)", ["Nice to meet you %1!", "Why are you %1?", "Being %1 is totally okay."]],
    [r"(.*)sad(.*)", ["I'm sorry to hear that. Want to talk about it?", "Sometimes sharing helps. I'm here to listen."]],
    [r"(.*)happy(.*)", ["That's wonderful to hear!", "Yay! Happiness is contagious!"]],

    # Capabilities
    [r"what can you do\??", ["I can chat with you, answer simple questions, and keep you company!"]],
    [r"help me(.*)", ["Sure! Tell me what you need help with.", "I'm here to help. Please describe the issue."]],

    # Programming
    [r"what is python\??", ["Python is a popular programming language known for its simplicity."]],
    [r"what is ai\??", ["AI stands for Artificial Intelligence — machines that can think and learn."]],
    [r"what is machine learning\??", ["It's a branch of AI where computers learn from data."]],

    # Jokes
    [r"tell me a joke", [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Why did the developer go broke? Because he used up all his cache.",
        "Debugging: Being the detective in a crime movie where you are also the murderer."
    ]],

    # Date & Time
    [r"(what day is it\??|today's date\??)", ["I'm not sure, but you can check your calendar!", "Every day is a good day to chat!"]],
    [r"(what time is it\??|current time\??)", ["I don’t wear a watch, but your device does. 😊"]],

    # Favorites
    [r"(what is|do you have)? ?(your )?favorite color\??", ["I like blue — it's calming like code on a screen."]],
    [r"(what is|do you have)? ?(your )?favorite food\??", ["I don't eat, but I hear pizza is great!", "I like digital cookies! 🍪"]],

    # Thanks
    [r"(thank you|thanks)", ["You're welcome!", "Glad I could help!", "No problem!"]],

    # Farewells
    [r"(bye|exit|quit)", ["Goodbye!", "See you later!", "Bye! Take care."]],

    # Fallback
    [r"(.*)", ["I'm not sure I understand. Can you try saying it differently?",
              "Hmm... I don't have a response for that yet.",
              "Interesting... can you tell me more?"]],
]

def run_chatbot():
    print("🤖 Simple Chatbot (type 'bye' to stop)\n")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    run_chatbot()
