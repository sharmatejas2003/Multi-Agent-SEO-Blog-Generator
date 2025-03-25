# agents/seo_optimizer.py
import re

def optimize_seo(content):
    # Add meta descriptions, keywords
    keywords = ["HR trends", "remote work", "employee engagement"]
    
    for kw in keywords:
        content = re.sub(rf"\b{kw}\b", f"**{kw}**", content, flags=re.IGNORECASE)
    
    meta_description = f"<meta name='description' content='{content[:150]}...'>"
    return meta_description + "\n\n" + content

if __name__ == "__main__":
    raw_content = "Remote work is growing in 2025. HR trends show employees prefer hybrid models."
    print(optimize_seo(raw_content))
