import os
import sys
from dotenv import load_dotenv
from google.genai import types, Client
from functions.call_function import call_function
from prompts import system_prompt
from functions.available_functions import available_functions

def main():
    if len(sys.argv) < 2:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = Client(api_key=api_key)
    verbose = "--verbose" in sys.argv
    user_prompt = " ".join(sys.argv[1:])
    if verbose:
        print(f"User prompt: {user_prompt}")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    generate_content(client, messages, verbose)

def generate_content(client: Client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt,
        )
    )
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    if not response.function_calls:
        return response.text

    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if (
            not function_call_result.parts or 
            not function_call_result.parts[0].function_response
        ):
            raise Exception('Error: empty function call result')
        print(f"-> {function_call_result.parts[0].function_response.response}")

if __name__ == "__main__":
    main()
