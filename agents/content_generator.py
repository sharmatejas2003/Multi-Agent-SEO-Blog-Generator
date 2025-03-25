# agents/content_generator.py
from langchain_community.llms import GPT4All # Corrected import
def generate_content(outline):
    llm = GPT4All(model="gpt-4", temperature=0.7)
    prompt = f"Write a 2000-word SEO-optimized blog post based on this outline:\n\n{outline}"
    return llm.invoke(prompt)

if __name__ == "__main__":
    outline = "1. Introduction\n2. Benefits of Remote Work\n3. Challenges & Solutions..."
    print(generate_content(outline))
