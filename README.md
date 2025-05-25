# Vision - AI-Powered Health & Safety Risk Assessor

A Python application that uses OpenAI's GPT-4o Vision model to analyze workplace photos and generate comprehensive Health & Safety risk assessments. The application provides instant analysis of workplace conditions, identifying potential hazards and providing recommendations based on UK Health & Safety regulations.

## Features

- **AI-Powered Image Analysis**: Uses OpenAI's GPT-4o Vision model to analyze workplace photos
- **Comprehensive Risk Assessment**: Provides detailed analysis following UK HSE guidelines
- **Multiple Image Support**: Upload and analyze multiple workplace photos in one session
- **PDF Report Generation**: Creates professional PDF reports with images and analysis
- **Interactive Web Interface**: User-friendly Gradio interface for easy photo upload and analysis
- **Public Sharing**: Share your analysis sessions via public Gradio links

## AI Technology

The application leverages OpenAI's GPT-4o Vision model, which combines:
- Advanced computer vision capabilities to understand workplace scenes
- Natural language processing to generate detailed analysis
- Knowledge of UK Health & Safety regulations and best practices
- Contextual understanding of workplace environments

The AI model is specifically prompted to:
1. Describe the workplace scene in detail
2. Identify potential health and safety hazards
3. Provide risk assessments based on UK regulations (HSW Act 1974, PUWER, PPE 2022)
4. Offer practical recommendations for improvement

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

3. Access the application:
- Local URL: http://localhost:7860 (or similar port)
- Public URL: A Gradio link will be provided in the terminal

## Usage

1. **Upload Photos**: Click the upload button to select workplace photos
2. **View Images**: Uploaded photos will appear in the gallery
3. **Analyze**: Click "Analyze Images" to process the photos
4. **Review Analysis**: View the detailed analysis in the text box
5. **Download Report**: Get a PDF report with images and analysis
6. **Share**: Use the public Gradio link to share your analysis session

## Requirements
- Python 3.11
- OpenAI API key with access to GPT-4o Vision
- Virtual environment (recommended)
- Internet connection for AI processing

## Dependencies
- openai==1.82.0
- gradio==5.31.0
- python-dotenv==1.0.1
- Pillow==10.2.0
- reportlab==4.1.0

## Security Notes
- Keep your OpenAI API key secure
- The `.env` file is excluded from version control
- Public Gradio links are temporary and expire after inactivity
- No data is stored permanently on the server

## Limitations
- Requires clear, well-lit photos for best results
- Analysis is based on visible elements in the photos
- Processing time depends on image size and number of images
- Public Gradio links expire after periods of inactivity

## Contributing
Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License
This project is licensed under the MIT License - see the LICENSE file for details. 