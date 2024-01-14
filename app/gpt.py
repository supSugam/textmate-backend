from openai import OpenAI
from .preprocessing import preprocess_text
from .analysis import perform_sentiment_analysis
import os
import re

client = OpenAI(
    # api_key=os.getenv("OPENAI_API_KEY"),
    api_key="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",  # this is also the default, it can be omitted
)

def generate_response(file_content, user_query=None):
    try:
        # Step 1: Preprocess the text
        summarized_text = preprocess_text(file_content)

        # Step 2: Perform sentiment analysis
        sentiment_result = perform_sentiment_analysis(summarized_text)

        # Step 3: Generate response using GPT-3.5 based on user query and combined features
        gpt_prompt = f"File Summary: {summarized_text}"
        if user_query:
            gpt_prompt += f"\n\nUser Query: {user_query}\n\nSentiment: {sentiment_result}\n\nNow, provide a response:"

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "user",
                "content": gpt_prompt
            }],
            temperature=0.9,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=["\n"]
        )

        generated_response = response.choices[0].message.content
        sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', generated_response)

        # Return a tuple containing both the generated response and the summarized text
        return generated_response, sentences

    except Exception as e:
        raise RuntimeError(f"Error generating response: {str(e)}")
