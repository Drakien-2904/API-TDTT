from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load model (chỉ load 1 lần khi server start)
model_name = "facebook/bart-large-cnn"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Khởi tạo FastAPI
app = FastAPI(
    title="Text Summarization API",
    description="API sử dụng Hugging Face model để tóm tắt văn bản",
    version="1.0"
)

# Input schema
class TextInput(BaseModel):
    text: str


# Trang giới thiệu
@app.get("/")
def root():
    return {
        "message": "Welcome to the Text Summarization API",
        "endpoints": {
            "health": "/health",
            "generate": "/generate"
        }
    }


# Kiểm tra trạng thái API
@app.get("/health")
def health():
    return {"status": "API is running"}


# Hàm tóm tắt
def summarize(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True)

    summary_ids = model.generate(
        inputs["input_ids"],
        max_length=200,
        min_length=10,
        num_beams=4,
        forced_bos_token_id=0
    )

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary


# Endpoint tạo summary
@app.post("/generate")
def generate(data: TextInput):

    if not data.text or len(data.text.strip()) == 0:
        raise HTTPException(status_code=400, detail="Input text is empty")

    if len(data.text) < 20:
        raise HTTPException(status_code=400, detail="Text too short to summarize")

    try:
        result = summarize(data.text)

        return {
            "input_text": data.text,
            "summary": result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))