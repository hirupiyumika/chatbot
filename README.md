# Simple Python Chatbot with OpenAI API

This is a simple chatbot application built with Python that interacts with OpenAI's GPT-3.5 Turbo model. The chatbot allows users to input queries and receive AI-generated responses in a conversational format. The app runs in a loop until the user types "bye" to exit.

## Features

- Interactive chatbot using OpenAI's GPT-3.5 Turbo model.
- Command-line interface (CLI) for easy interaction.
- Supports environment variable configuration for secure API key storage.
- User-friendly experience with a simple input/output mechanism.

## Requirements

- Python 3.x
- OpenAI Python package
- dotenv for environment variable management

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/hirupiyumika/chatbot.git
   cd chatbot
   ```

2. **Install dependencies:**

   Install required packages using pip:

   ```bash
   pip install openai python-dotenv
   ```

3. **Set up the API key:**

   Create a `.env` file in the project directory and add your OpenAI API key:

   ```
   OPENAI_API_KEY=your-api-key-here
   ```

## Usage

1. **Run the chatbot script:**

   ```bash
   python chatbot.py
   ```

2. **Interact with the chatbot:**

   - Type your questions and press `Enter`.
   - Type `bye` to exit the chatbot.

   Example interaction:

   ```
   User: Hello
   AI: Hello! How can I assist you today?
   User: What's the weather like?
   AI: I'm sorry, but I can't provide real-time weather updates.
   User: bye
   AI: Goodbye!
   ```

## Configuration

- The chatbot script uses the OpenAI API key stored in a `.env` file for security.
- Modify the `max_tokens`, `temperature`, and `model` parameters in the script to customize chatbot behavior.

## Troubleshooting

- Ensure that your `.env` file is correctly configured with your OpenAI API key.
- If you encounter errors related to the API, check your API key usage limits on the [OpenAI dashboard](https://platform.openai.com/account/usage).

---

Let me know if you need further modifications!
