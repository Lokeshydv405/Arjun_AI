from groq import Groq
import os

def ai(user_profile):
    # Construct the prompt based on user profile details
    prompt = f"""Create a detailed, personalized 7-day diet plan based on the following user profile and preferences:

### User Profile:
- **Age**: {user_profile['age']}
- **Gender**: {user_profile['gender']}
- **Weight**: {user_profile['weight']} kg
- **Height**: {user_profile['height']} cm
- **Fitness Goal**: {user_profile['fitness_goal']}
- **Medical Conditions**: {user_profile['medical_conditions']}
- **Dietary Restrictions**: {user_profile['dietary_restrictions']}
- **Budget**: {user_profile['budget']}

### Diet Preferences:
- **Preferred Food Category**: {user_profile['preferred_food_category']}
- **Preferred Cuisine**: {user_profile['preferred_cuisine']}
- **Foods to Include**: {', '.join(user_profile['foods_to_include'])}
- **Foods to Avoid**: {', '.join(user_profile['foods_to_avoid'])}
- **Number of Meals**: {user_profile['number_of_meals']}
- **Specific Ingredients**: Likes: {', '.join(user_profile['likes'])}, Dislikes: {', '.join(user_profile['dislikes'])}

### Other Preferences:
- **Cooking Time**: {user_profile['cooking_time']}
- **Activity Level**: {user_profile['activity_level']}

### Output Instructions:
- Provide a day-by-day breakdown for 7 days, including breakfast, lunch, dinner, and snacks.
- Each meal should include a dish with its Hindi name in brackets.
- List estimated calorie counts for each meal.
- Suggest ingredient substitutions if needed to align with dietary restrictions and budget constraints.
- Summarize the overall calorie count and highlight any nutritional notes relevant to diabetes.

"""

    text = f'Questions for AI: {prompt} \n' + "-" * 20
    client = Groq(api_key="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")
    
    try:
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=2000,
            top_p=1,
            stream=True,
            stop=None,
        )
        
        response = ""
        for chunk in completion:
            chunk_content = chunk.choices[0].delta.content or ""
            response += chunk_content
            print(chunk_content, end="")  # Real-time output
        
        text += response

        # Ensure the 'Answers' directory exists
        if not os.path.exists('Answers'):
            os.mkdir('Answers')

        # Sanitize and create a descriptive file name
        file_name = f"Answers/diet_plan_{user_profile['fitness_goal'].replace(' ', '_')}.txt"

        # Write the response to the file
        # Write the response to the file with UTF-8 encoding
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(text)
            print("\nDone, Check for the File in Answers Folder")
            # say("Done, Check for the File in Answers Folder")  # Uncomment for audio feedback


    except Exception as e:
        print(f"An error occurred: {e}")

    return True

# Example to run the AI function
if __name__ == "__main__":
    # Sample user profile input for diet planning
    user_profile = {
        "age": 20,
        "gender": "Male",
        "weight": 65,
        "height": 175,
        "fitness_goal": "Weight gain",
        "medical_conditions": "High Blood Pressure",
        "dietary_restrictions": "Low sugar",
        "budget": "Medium",
        "preferred_food_category": "Vegetarian",
        "preferred_cuisine": "North Indian",
        "foods_to_include": [],
        "foods_to_avoid": ["Sugary snacks", "Processed foods", "Oily snacks"],
        "number_of_meals": "3 meals and 2 snacks per day",
        "likes": ["Soya beans"],
        "dislikes": ["Coriander"],
        "cooking_time": "Quick meals",
        "activity_level": "Moderate, exercises 3 times a week"
    }

    # Call the AI function
    ai(user_profile)
