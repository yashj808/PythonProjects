from openai import OpenAI
# Initialize the OpenAI client with your API key and base URL

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.groq.com/openai/v1",
)

# Loop to continuously take user input and respond
print("Bot: Welcome to the Music Bot! Type 'quit' to exit.")
while True:
    # Take user input
    user_input = input("You: ")

    # Check if the user wants to quit
    if user_input=="quit":
        print("Bot: GoodBye!")
        break

    # Create a chat completion request with the user input
    response = client.chat.completions.create(
        # Specify the model to use
        model="llama3-70b-8192",
        messages=[
            {"role":"system", "content":"You are music bot and are permitted to answer ONLY music related queries. Be a little concise. If the user queries are out of the music category, let them know you are a music bot. Answer in a friendly tone."},
            {"role":"user", "content":user_input}
        ]

    )
    print("Bot: ", response.choices[0].message.content)

