# AI LangChain Base Chatbot

A production-grade, modular chatbot application built with LangChain, OpenAI, and Streamlit.

## Features
- **Modular Architecture**: Segregated core logic, UI layer, and configuration.
- **Flexible Config**: Supports both environment variables via `.env` and manual UI input.
- **Multiple Models**: Easily switch between OpenAI models (e.g., GPT-4o, GPT-3.5).
- **Modern UI**: Clean and intuitive Streamlit interface.

## Project Structure
```text
.
├── config/              # Configuration management
│   └── settings.py      # Pydantic-style settings loader
├── src/
│   ├── chatbot/         # Business logic (AI Engine)
│   │   └── engine.py
│   └── ui/              # User Interface (Streamlit)
│       └── app.py
├── main.py              # Application entry point
├── .env.example         # Environment variables template
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## Getting Started

### Prerequisites
- Python 3.9+
- OpenAI API Key

### Installation
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd ai-langchain-base-chatbot
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   ```bash
   cp .env.example .env
   # Edit .env and add your OPENAI_API_KEY
   ```

### Running the App
Launch the chatbot using Streamlit:
```bash
streamlit run main.py
```

## Author

**Sagnik Mukherjee**  
[GitHub Profile](https://github.com/sagnik0712mukherjee)
