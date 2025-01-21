# Pybot: A Conversational AI Chatbot

Pybot is a conversational AI chatbot built using the LangChain library and the OllamaLLM language model. It provides a simple and intuitive interface for users to interact with the AI assistant.

## Installation

To use Pybot, you'll need to have Python 3.x installed on your system. You can then follow these steps to set up the project:

1. Clone the repository:
```
git clone https://github.com/your-username/pybot.git
```

2. Navigate to the project directory:
```
cd pybot
```

3. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

4. Install the required dependencies:
```
pip install -r requirements.txt
```

## Usage

To start the Pybot application, run the following command:

```
python main.py
```

This will launch the Pybot GUI, where you can interact with the AI assistant by typing your questions or comments in the input field and pressing the "Send" button.

The chatbot will display the conversation history and the AI's responses in the chat display area.

## API

Pybot uses the following APIs and libraries:

- [LangChain](https://github.com/hwchase17/langchain): A framework for building applications with large language models (LLMs).
- [OllamaLLM](https://github.com/Anthropic/langchain-ollama): A LangChain adapter for the Ollama language model.

The main functionality of the chatbot is implemented in the `get_ai_response()` method, which takes the user's input, passes it through the LangChain prompt and model, and returns the AI's response.

## Contributing

If you'd like to contribute to the Pybot project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch to your forked repository.
5. Submit a pull request to the main repository.

## License

This project is licensed under the [MIT License](LICENSE).

## Testing

To run the tests for Pybot, use the following command:

```
python -m unittest discover tests
```

This will run all the test cases defined in the `tests` directory.