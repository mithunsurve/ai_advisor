# AI Course Advisor

This application helps students get AI-powered course recommendations and advice for their academic journey.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- OpenAI API key

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd ai_advisor
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Running the Application

1. Make sure your virtual environment is activated (if you created one)

2. Start the application by running both files in separate terminal windows:

   In the first terminal:
   ```bash
   python advisor.py
   ```

   In the second terminal:
   ```bash
   python app.py
   ```

3. The application will run in the command-line interface (CLI). Follow the prompts in the terminal to interact with the AI Course Advisor.

## Features

- Course recommendations based on your interests and goals
- AI-powered academic advice
- Interactive chat interface
- Personalized learning path suggestions

## Troubleshooting

If you encounter any issues:

1. Ensure all dependencies are installed correctly
2. Verify your OpenAI API key is valid and properly set in the `.env` file
3. Check that you're using a compatible Python version
4. Make sure both advisor.py and app.py are running in separate terminal windows

## Support

For any issues or questions, please open an issue in the repository.