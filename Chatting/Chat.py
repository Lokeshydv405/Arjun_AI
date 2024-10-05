from groq import Groq
from config import apikey2

chatStr = ''

def chat(query):
    query = query.lower()
    global chatStr
    newChat = f"Master : {query} \nArjun:"
    text = ""  # Initialize text as an empty string

    client = Groq(api_key=apikey2)
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "user",
                "content": f"{newChat}"
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    for chunk in completion:
        if chunk.choices[0].delta.content:  # Check if content is not None
            print(chunk.choices[0].delta.content, end="")
            text += chunk.choices[0].delta.content  # Concatenate the text

    # Remove "Jarvis:" from the response
    response_text = text.replace("Arjun:", "").strip()
    
    newChat += response_text + "\n"  # Append the cleaned response to chatStr
    chatStr += newChat
    
    return response_text  # Return the cleaned response text
