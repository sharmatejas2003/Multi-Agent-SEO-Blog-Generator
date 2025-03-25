from langchain_community.llms import GPT4All
import os

# Ensure the correct model name is used and downloaded
llm = GPT4All(model="mistral-7b-openorca.Q4_0.gguf", temperature=0.5)

def generate_outline(topic):
    prompt = f"Generate a detailed blog outline for an article on '{topic}' following SEO best practices."
    return llm.invoke(prompt)

if __name__ == "__main__":
    topic = "Remote Work Trends in 2025"
    print(generate_outline(topic))
