import pyttsx3
import os
import google.genai as genai
import types
from dotenv import load_dotenv, find_dotenv

def main():
    # hello_world()
    # speak("Leo is an idiot")
    # get_int()
    # agree()
    # test_range()
    # find_name()
    # phone_book()
    talk_to_gemini()


def talk_to_gemini():
    _ = load_dotenv(find_dotenv())
    gemini_api_key = os.environ["GEMINI_API_KEY"]
    client = genai.Client(api_key=gemini_api_key)
    system_prompt = "You are a friendly and supportive lecturer at Dundalk Institute of Technology. You are also succint. Use no markdown as you are in the terminal."
    user_prompt = input("What do you want to know?: ")
    llm_model = "gemini-3.5-flash"
    chat = client.chats.create(model=llm_model)
    response = chat.send_message(system_prompt+user_prompt)
    print(response.text)


def hello_world():
    print("Hello, world")


def speak(to_say:str):
    engine = pyttsx3.init()
    engine.say(to_say)
    engine.runAndWait()


def get_int():
    while True:
        try:
            number = int(input("Please enter an integer: "))
            print (number)
            return
        except ValueError:
            print("This is not an integer >:(")


def agree():
    while True:
            response = input("Do you agree: ").lower()
            if response in ["yes", "no", "y", "n", "agree", "disagree"]:
                return
            else:
                print("Answer is not agreeing or disagreeing!")


def test_range():
    numbers = list(range(1,101))
    print(numbers)
    for i in numbers:
        if (i%2 == 0):
            print(i)
            break


def find_name():
    names = ["Pijus", "Leo", "Raivis", "Anastasija", "Kornel"]
    name_to_search = input("Who are you looking for?: ").lower()
    for i in names:
        if i.lower() == name_to_search:
            print("Found " + i + "!")


def phone_book():
    people = {"Pijus": "+353123456789", "Leonas": "+353123456789"}
    name = input("Please enter name:")
    if name in people:
        print(f"Number: {people[name]}")


if __name__ == "__main__":
    main()