# Contextual-CLI-Chat
A command-line chatbot with conversation memory, structured logging, and graceful API error handling

## Features
 
- **Conversation memory** — the full message history is resent with each request, so the bot can correctly follow up on earlier turns instead of treating every message as a new conversation.
- **Graceful error handling** — timeouts, rate limits (`429`), invalid credentials (`401`), and malformed/non-JSON responses are all caught explicitly, so the program fails with a clear message instead of crashing.
- **Structured logging** — every call logs a timestamp, latency, real token usage (from the API's own `usage` field), and the prompt/response pair to `chat_log.txt`.
- **Environment-based configuration** — the API key is loaded from a local `.env` file, kept out of source control.
## Setup
 
1. Clone the repo:
```bash
   git clone https://github.com/sumziii/Contextual-CLI-Chat.git
   cd Contextual-CLI-Chat
```
2. Install dependencies:
```bash
   pip install requests python-dotenv
```
3. Copy the example environment file and add your real key:
```bash
   cp .env.example .env
```
   Then open `.env` and replace the placeholder with your actual [Groq API key](https://console.groq.com/keys).
 
## Usage
 
```bash
python chatbot.py
```
 
Type a message and press Enter. Type `exit` to end the session.
 
Example:
```
You: what are the primary colours
Chatbot: [explains RGB, CMY, and RYB systems]
 
You: for painting
Chatbot: [correctly follows up, describing RYB specifically for painting —
          conversation memory in action]
```
 
## Project structure
 
```
.
├── chatbot.py        # Main chat loop: memory, logging, error handling
├── test_key.py        # Minimal script to verify an API key works
├── .env.example        # Template for required environment variables
├── .gitignore
└── README.md
```
## Known limitations
 
- No retry/backoff logic on rate-limit errors — a `429` currently just stops that turn rather than automatically retrying.
- No streaming support yet — responses are returned in full rather than printed incrementally.
## License
 
MIT
 
