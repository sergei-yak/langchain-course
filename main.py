import os

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


def main():
    print("Hello from langchain-course!")
    print("Your OPENAI_API_KEY is:", os.getenv("OPENAI_API_KEY"))


if __name__ == "__main__":
    main()
