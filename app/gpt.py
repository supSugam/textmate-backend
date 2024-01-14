# import openai
# from .preprocessing import preprocess_text
# from .analysis import perform_sentiment_analysis

# # Set your OpenAI API key
# openai.api_key = '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'


# def generate_response(file_content, user_query):
#     try:
#         # Step 1: Preprocess the text
#         summarized_text = preprocess_text(file_content)

#         # Step 2: Perform sentiment analysis
#         sentiment_result = perform_sentiment_analysis(summarized_text)

#         # Step 3: Generate response using GPT-3.5 based on user query and combined features
#         gpt_prompt = f"File Summary: {summarized_text}\n\nUser Query: {user_query}\n\nSentiment: {sentiment_result}\n\nNow, provide a response:"
#         response = openai.Completion.create(
#             engine="text-davinci-002",  # You can choose a different engine if needed
#             prompt=gpt_prompt,
#             max_tokens=100,
#             temperature=0.7,
#         )

#         generated_response = response['choices'][0]['text'].strip()

#         return generated_response

#     except Exception as e:
#         raise RuntimeError(f"Error generating response: {str(e)}")
import openai
from .preprocessing import preprocess_text
from .analysis import perform_sentiment_analysis

# Set your OpenAI API key
openai.api_key = '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'

def generate_response(file_content, user_query=None):  # Add user_query as an optional argument
    try:
        # Step 1: Preprocess the text
        summarized_text = preprocess_text(file_content)

        # Step 2: Perform sentiment analysis
        sentiment_result = perform_sentiment_analysis(summarized_text)

        # Step 3: Generate response using GPT-3.5 based on user query and combined features
        gpt_prompt = f"File Summary: {summarized_text}"
        if user_query:
            gpt_prompt += f"\n\nUser Query: {user_query}\n\nSentiment: {sentiment_result}\n\nNow, provide a response:"

        response = openai.Completion.create(
            engine="text-davinci-002",  # You can choose a different engine if needed
            prompt=gpt_prompt,
            max_tokens=100,
            temperature=0.7,
        )

        generated_response = response['choices'][0]['text'].strip()

        return generated_response

    except Exception as e:
        raise RuntimeError(f"Error generating response: {str(e)}")

