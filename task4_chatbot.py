def get_reply(text):
    greetings = ["hello", "hi", "hey"]
    good_words = ["good", "i am good", "i'm good"]

    if text in greetings:
        return "\nHi, how's your day going!"

    if text in good_words:
        return "\n Glad to hear that! so what's the agenda today?"

    keyword_replies = [
        ("how are you", "\nI am fine thanks for asking! what about you? "),
        ("good morning", "\nGood morning! Hope you have a great day!"),
        ("good night", "\nGood night! Sleep well"),
        ("who are you", "\n I'm a simple Python chatbot designed to answer your questions."),
        ("what is your name", "\n My name is Alexa AI Chatbot"),
        ("what can you do", "\nI can answer basic questions, tell jokes, and have simple conversations."),
        ("what is python", "\nPython is a popular programming language known for its simple and readable syntax."),
        ("who created you", "\nI am created using Python"),
        ("tell me a joke", "\nWhy do programmers prefer dark mode? Because light attracts bugs! "),
        ("tell me another joke", "\nWhy was the computer cold? Because it left its Windows open! "),
        ("thanks", "\nYou're welcome!"),
        ("bye", "\nGoodbye! Have a great day! ")
    ]

    for word, reply in keyword_replies:
        if word in text:
            return reply

    return "\nSorry, I don't understand that yet."


print("Hey there! I am Alexa your AI Assistant\n")
print("How can I help you today?")

while True:
    user_response = input("\nAsk anything... (type exit to exit)").lower()

    if user_response == "exit":
        break

    print(get_reply(user_response))
