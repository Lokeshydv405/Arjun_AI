from groq import Groq
from config import apikey2
import os
from Basic_Utilization.Say import say

def ai(prompt):
    text = f'Questions for AI: {prompt} \n' + "-" * 20
    client = Groq(api_key=apikey2)
    
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )
    
    response = ""
    for chunk in completion:
        chunk_content = chunk.choices[0].delta.content or ""
        response += chunk_content
        # print(chunk_content, end="")

    text += response

    # Ensure the 'Answers' directory exists
    if not os.path.exists('Answers'):
        os.mkdir('Answers')

    # Sanitize and truncate the file name
    sanitized_prompt = ''.join(prompt.split('write')[1:]).strip()[:20].replace('/', '_').replace('\\', '_')  # Adjust sanitization as needed
    file_name = f'Answers/{sanitized_prompt}.txt'

    # Write the response to the file
    with open(file_name, 'w') as f:
        f.write(text)
        print(" Done , Check for the File in Answers Folder")
        say(" Done , Check for the File in Answers Folder")

    return True
