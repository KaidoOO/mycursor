import os
import sys
from dotenv import load_dotenv
from google import genai

def main():
    print("Hello from mycursor!")
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    
    client = genai.Client(api_key=api_key)
    if(len(sys.argv) > 1):
        print(f"cli arguments {len(sys.argv)}")
        first_prompt = sys.argv[1]
    else:
        print("Please provide a prompt as a command line argument.")
        sys.exit(1)
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=first_prompt)
    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
