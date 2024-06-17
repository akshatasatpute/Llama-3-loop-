from flask import Flask, request, jsonify
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer



app = Flask(__name__)

# Define a placeholder function for LLaMA-3 response generation

# Replace 'meta-llama/LLaMA-3' with the actual model name when available
model_name = 'meta-llama/LLaMA-3'

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

    
    # Replace this placeholder with actual LLaMA-3 model code
    # For demonstration, just echo back the input


def generate_response(prompt, model, tokenizer, max_length=100):
    inputs = tokenizer(prompt, return_tensors='pt')
    outputs = model.generate(inputs.input_ids, max_length=max_length, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

def generate_llama_response(user_input):
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye!")
            break
        response = generate_response(user_input, model, tokenizer)
        print(f"Chatbot: {response}")



@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    response = generate_llama_response(user_input)
    return jsonify({'message': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

