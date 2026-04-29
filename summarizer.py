from transformers import pipeline

# Load pre-trained model (runs first time slowly)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    max_len = 130
    min_len = 30

    result = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
    
    return result[0]['summary_text']
