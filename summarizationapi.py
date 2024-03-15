from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app =FastAPI()

class Article(BaseModel):
    text: str

class Summary(BaseModel):
    summary_text: str

summarizer = pipeline('summarization')

@app.post("/", response_model=Summary)
async def summarize_article(article: Article):
    # Summarize the article
    summary = summarizer(article.text, max_length=130, min_length=30, do_sample=False)
    return {"summary_text": summary[0]['summary_text']}
