import openai

openai.api_type = "azure"
openai.api_base = "YOUR_AZURE_OPENAI_ENDPOINT"
openai.api_version = "2023-05-15"
openai.api_key = "YOUR_OPENAI_KEY"

def answer_question(user_question, docs_text):
    prompt = f"Use the following information to answer the question:\n{docs_text}\n\nQuestion: {user_question}\nAnswer:"
    response = openai.Completion.create(
        engine="gpt-35-turbo",
        prompt=prompt,
        max_tokens=256,
        temperature=0.2
    )
    return response.choices[0].text.strip()

# Usage example
docs_text = get_all_texts()
user_question = "What is insurance?"
answer = answer_question(user_question, docs_text)
print(answer)
