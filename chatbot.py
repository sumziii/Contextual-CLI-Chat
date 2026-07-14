import os
import time
from dotenv import load_dotenv
import requests

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

headers = {
    "Authorization":f"Bearer {api_key}",
    "Content-Type":"application/json"
}

convo_history = []

def log_call(prompt,response_text, latency, tokens_used):
    timestamp =time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    line =(f"[{timestamp}] latency ={latency:.2f}s, tokens= {tokens_used} |" f"prompt = {prompt!r}, response = {response_text!r}\n")
    with open("chat_log.txt", "a", encoding="utf-8") as f:
        f.write(line)

def get_reply(messages):
    payload= {
        "model": "openai/gpt-oss-20b",
        "messages": messages
    }

    start_time = time.time()

    try:
        response= requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers=headers,
        json=payload,
        timeout=15
    )
        if response.status_code==429:
            print("Rate limited. Try again in a moment. ")
            return None
        if response.status_code == 401:
            print("Invalid API key. Please check your .env file.")
            return None
        try:
            data = response.json()
        except ValueError:
            print("Error: Invalid JSON response from the API.")
            return None
        
        latency = time.time() - start_time
        reply= data['choices'][0]['message']['content']
        tokens_used = data.get('usage', {}).get('total_tokens', "unknown")
        
        log_call(messages[-1]['content'], reply, latency, tokens_used)
        return reply

    except requests.exceptions.Timeout:      # outer except
        print("Request timed out...")
        return None
    except requests.exceptions.RequestException as e:  # outer except
        print(f"Something went wrong: {e}")
        return None

def main():
    print("Welcome to the chatbot! Type 'exit' to quit. \n") 
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        convo_history.append({"role": "user", "content": user_input})
        reply = get_reply(convo_history)

        print(f"Chatbot: {reply}\n")
        convo_history.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    main()