import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import gradio as gr

def load_model():
    model_name = "bitext/Mistral-7B-Travel"
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)  # Use slow tokenizer for SentencePiece
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",
        load_in_4bit=True,
        low_cpu_mem_usage=True
    )
    return tokenizer, model

def generate_response(user_input):
    tokenizer, model = load_model()
    inputs = tokenizer(user_input, return_tensors="pt").to("cuda")
    outputs = model.generate(**inputs, max_new_tokens=200)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

iface = gr.Interface(
    fn=generate_response,
    inputs="text",
    outputs="text",
    title="AI-Powered Tour Planning Chatbot",
    description="Ask me anything about your travel plans!"
)

if __name__ == "__main__":
    iface.launch()
