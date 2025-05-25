# Vision - ChatGPT-4 Powered Gradio App

A Python application built with Gradio that interfaces with OpenAI's GPT-4 API.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
.\venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Running the Application

1. Ensure your virtual environment is activated
2. Run the application:
```bash
python app.py
```

3. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:7860)

## Requirements
- Python 3.11
- OpenAI API key
- Virtual environment (recommended) 