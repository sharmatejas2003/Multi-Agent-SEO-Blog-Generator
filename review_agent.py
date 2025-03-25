# agents/review_agent.py
import nltk
from nltk.tokenize import sent_tokenize
from textstat import flesch_reading_ease

nltk.download('punkt')

def review_content(content):
    sentences = sent_tokenize(content)
    reading_score = flesch_reading_ease(content)
    
    summary = f"Total Sentences: {len(sentences)}\nReadability Score: {reading_score}"
    return summary + "\n\n" + content

if __name__ == "__main__":
    blog = "Remote work is a new trend. Employees enjoy flexibility but face challenges."
    print(review_content(blog))
