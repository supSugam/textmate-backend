from openai import OpenAI
from .preprocessing import preprocess_text
from .analysis import perform_sentiment_analysis
import os

api_keys = [
    os.getenv("OPENAI_API_KEY_1"),
    os.getenv("OPENAI_API_KEY_2"),
    os.getenv("OPENAI_API_KEY_3"),
]

def generate_summary(file_content):
    # Step 1: Preprocess the text
    result = preprocess_text(file_content)
    # Access the results
    entity_relations = result['entity_relations']
    categories = result['categories']
    summarized_text = result['summarized_text']
    for api_key in api_keys:
        try:
            client = OpenAI(api_key=api_key)
            
            # Step 2: Perform sentiment analysis
            sentiment_result = perform_sentiment_analysis(summarized_text)

            # Step 3: Generate response using GPT-3.5 based on user query and combined features
            gpt_prompt = f"Key Contents of File: {', '.join([f'{key}: {value}' for key, value_set in entity_relations.items() for value in value_set])} \nSentiment: {sentiment_result} \nCategories:{', '.join(categories)} \nNow Summarize the provided content in sense of specified sentiment in one paragraph, in nice readable sentences, not more than 600 characters."

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "user",
                        "content": gpt_prompt
                    }
                ],
                temperature=0.7,
                max_tokens=200,
                top_p=0.9,
                frequency_penalty=0.2,
                presence_penalty=0.4,
                stop=["\n"]
            )

            generated_response = response.choices[0].message.content

            # Return a tuple containing both the generated response and the summarized text
            return {
                'summarized_text': generated_response,
                'categories': categories,
                'sentiment': sentiment_result,
            }
        
        except Exception as e:
            print(f"API Key {api_key} failed with error: {str(e)}")

    return {
    'summarized_text': f"{summarized_text}\n\n",
    'categories': categories,
    'sentiment': sentiment_result,
    }




def respond_user_query(file_content, question):
    # Step 1: Preprocess the text
    result = preprocess_text(file_content)
    entity_relations = result['entity_relations']
    summarized_text = result['summarized_text']
    for api_key in api_keys:
        try:
            client = OpenAI(api_key=api_key)
            
            # Step 2: Perform sentiment analysis
            sentiment_result = perform_sentiment_analysis(summarized_text)

            # Step 3: Generate response using GPT-3.5 based on user query and combined features
            gpt_prompt = f"Content: {summarized_text}\n \nEntity Relations: {', '.join([f'{key}: {value}' for key, value_set in entity_relations.items() for value in value_set])}\n\nSentiment: {sentiment_result}\nQuestion: {question}\n Now Answer based on the information provided in a nice way, but nothing irrelevant, keep response under 200 characters long."

            response = client.chat.completions.create(
                model="text-embedding-ada-002",
                messages=[{
                    "role": "user",
                    "content": gpt_prompt
                },
                ],
                temperature=0.7,
                max_tokens=100,
                top_p=0.9,
                frequency_penalty=0.2,
                presence_penalty=0.4,
                stop=["\n"]
            )

            generated_response = response.choices[0].message.content
            # Return a tuple containing both the generated response and the summarized text
            return generated_response

        except Exception as e:
            print(f"API Key {api_key} failed with error: {str(e)}")
    
    return f"Quota Exceeded. Please try again later, or update the API Keys."