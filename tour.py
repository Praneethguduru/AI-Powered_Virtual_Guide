import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch

# Load model with 4-bit quantization
device = 'cuda' if torch.cuda.is_available() else 'cpu'

bnb_config = BitsAndBytesConfig(load_in_4bit=True)
model = AutoModelForCausalLM.from_pretrained(
    "bitext/Mistral-7B-Travel", 
    quantization_config=bnb_config
).to(device)

tokenizer = AutoTokenizer.from_pretrained("bitext/Mistral-7B-Travel")

def generate_response(user_input):
    prompt = f"You are an expert in customer support for Travel.\nUser: {user_input}\nAssistant:"
    model_inputs = tokenizer(prompt, return_tensors="pt").to(device)
    
    # Generate response
    generated_ids = model.generate(
        model_inputs["input_ids"],
        max_new_tokens=150,
        do_sample=True,
        temperature=0.7,
        top_p=0.9
    )
    decoded = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
    return decoded.strip()

# Gradio Interface
demo = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(label="Ask your travel question:"),
    outputs=gr.Textbox(label="Travel Assistant's Response:"),
    title="AI Travel Planning Assistant",
    description="Ask me anything about destinations, flights, accommodations, and more!"
)

demo.launch()
