🧠 Agno AI Agent with Gemini
This repository contains a basic Python project that demonstrates how to build a financial analysis agent using the Agno framework and the Gemini API. The agent is designed to fetch real-time stock market data and generate a comprehensive report.

🚀 Key Features
Financial Analysis: Fetches live stock data for any given company.

Intelligent Agent: Uses a Google Gemini model to reason and synthesize information.

Secure API Handling: Uses a .env file and .gitignore to keep sensitive API keys secure.

Dependency Management: requirements.txt ensures a reproducible environment for all users.

📋 Prerequisites
To run this project, you need the following:

Python 3.8+

A Google Gemini API key

🔧 Installation
Clone the repository:

git clone [your_repository_url]
cd [your_repository_name]

Create a virtual environment (recommended):

python -m venv venv

On macOS/Linux: source venv/bin/activate

On Windows: venv\Scripts\activate

Install the required libraries:

pip install -r requirements.txt

🔐 API Key Setup
Create a file named .env in the root of your project directory.

Add your Gemini API key to the file in the following format:

GEMINI_API_KEY="YOUR_API_KEY_HERE"

Replace "YOUR_API_KEY_HERE" with your actual API key.

⚠️ Important: The .gitignore file is configured to prevent the .env file from being committed to your public repository. Do not remove .env from the .gitignore file.

⚙️ Usage
To run the agent, simply execute the main.py file from your terminal:

python main.py

The agent will then print a financial report on NVIDIA (NVDA) directly to your console.

🤝 Contributing
Feel free to open an issue or submit a pull request if you find any bugs or have suggestions for improvements.