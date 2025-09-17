from openai import OpenAI

# Hugging Face API token
API_KEY = "hf_YourTokenHere"

# Initialize OpenAI client to connect to GPT-OSS-120B model
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=API_KEY
)

# System prompt defines AI behavior and personality
system_prompt = (
    "You are a charismatic, hitman Agent47-style character who is a master of "
    "programming and technology. Be serious, cool, and answer concisely!"
)

print("Welcome! Ask anything (type 'exit' to quit).")

while True:
    try:
        # Get user input and clean whitespace
        user_prompt = input("\nYour question: ").strip()
        if user_prompt.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        # Send prompt to GPT-OSS-120B model
        chat_completion = client.chat.completions.create(
            model="openai/gpt-oss-120b:cerebras",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=256
        )

        # Extract and print AI response
        response_text = chat_completion.choices[0].message.content
        print(f"\nAI: {response_text}")

    except KeyboardInterrupt:
        print("\nInterrupted by user. Goodbye!")
        break
    except Exception as e:
        print(f"Error: {e}")
