# YouTube Trend Analysis Tool 🎥

## Overview
This tool is part of the AI Engineering Hub initiative, providing powerful YouTube channel analysis using AI agents and data scraping capabilities. Built with CrewAI, Bright Data, and Streamlit, it offers deep insights into YouTube content trends and patterns.

## Features
- 🤖 AI-powered content analysis using CrewAI agents
- 📊 YouTube channel data scraping with Bright Data
- 📈 Trend analysis and insights generation
- 🎯 Custom date range selection
- 💻 User-friendly Streamlit interface
- 🤖 Ability to swap between API calls and local models (I used Deepseek-r1:7b with Ollama for this)

## Installation
1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Set up environment variables in `.env`:
```
BRIGHT_DATA_API_KEY=your_key
OPENAI_API_KEY=your_key
CLAUDE_API_KEY=your_key
```

## Usage
Run the application using:
```bash
streamlit run app.py
```

## Technology Stack
- **Frontend**: Streamlit
- **AI Processing**: CrewAI, Ollama
- **Data Collection**: Bright Data API
- **Language Models**: Deepseek-r1:7b

## Attribution
This project is a fork of [AI Engineering Hub](https://github.com/patchy631/ai-engineering-hub), which provides in-depth tutorials on LLMs, RAGs, and real-world AI agent applications.  I just had to make a couple of changes to get it working.

## Author
Sean A. Harrington  
Director of Technology Innovation  
University of Oklahoma College of Law

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
