# AI Code Documentation Generator

Automatically generate professional docstrings, class documentation, and README files for Python projects using Google's Gemini 2.5 Flash AI model.

## Features

- Smart function and class documentation with type hints and examples
- Auto-insert docstrings directly into code files with proper formatting
- Generate comprehensive README files for entire projects
- Clean web interface with side-by-side code comparison
- Download documented files instantly
- Supports Google-style docstrings

## Installation

Clone this repository and install dependencies:
pip install google-genai python-dotenv streamlit


Create a .env file in the project root and add your Gemini API key. Get a free API key from Google AI Studio.

## Usage

Launch the Streamlit application, upload any Python file, click the generate button, and download your documented code with professional docstrings automatically inserted at the correct locations.

## Technical Stack

- AI Model: Google Gemini 2.5 Flash
- Frontend: Streamlit
- Parser: Python AST module
- Python 3.8 or higher required

## Project Structure

- parser.py: Extracts functions and classes from Python files
- generator.py: Generates docstrings using Gemini API
- readme_generator.py: Creates project README files
- app.py: Streamlit web interface

## License

MIT License. Free to use for personal and commercial projects.

## Contributing

Contributions welcome. Fork the repository and submit pull requests with improvements.
