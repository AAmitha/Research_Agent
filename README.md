# 🔍 Research Agent

An AI-powered research agent that performs multi-step web research to answer complex questions comprehensively.

## 🎯 What it does

- Takes a complex question as input
- Automatically searches the web using Tavily
- Reasons step-by-step using Llama 3.2 (local LLM)
- Synthesizes findings into a comprehensive answer with sources

## 🏗️ Architecture

User Question → LangGraph Agent → Llama 3.2 thinks → Tavily searches web → Llama 3.2 synthesizes → Answer

This follows the **ReAct pattern** (Reason + Act) - the LLM reasons about what to search, acts by searching, then reasons again until it has enough information.

## 🛠️ Tech Stack

| Tool | Purpose | Cost |
|------|---------|------|
| LangGraph | Agent workflow orchestration | Free |
| Llama 3.2 (Ollama) | Local LLM — no API needed | Free |
| Tavily | Web search API | Free tier |
| Streamlit | Chat UI | Free |

## 🚀 Run Locally

### Prerequisites
- Python 3.11+
- [Ollama](https://ollama.com) installed
- [Tavily API key](https://tavily.com) (free)

### Steps

Clone the repo and navigate into it:

    git clone https://github.com/AAmitha/Research_Agent.git
    cd Research_Agent

Create and activate virtual environment:

    python -m venv venv
    venv\Scripts\activate        # Windows
    source venv/bin/activate     # Mac/Linux

Install dependencies:

    pip install -r requirements.txt

Pull Llama 3.2 model:

    ollama pull llama3.2

Add your Tavily API key — create a .env file:

    TAVILY_API_KEY=your_key_here

Run the app:

    streamlit run app.py

## 💡 Key Concepts

**ReAct Pattern** - Agent alternates between Reasoning (what do I need to find?) and Acting (search for it), looping until it has enough context to answer.

**LangGraph StateGraph** - Manages the agent's state across multiple search iterations, enabling complex multi-step reasoning.

**Local LLM** - Uses Ollama to run Llama 3.2 locally — no OpenAI API costs, complete privacy.

## 📁 Project Structure

    Research_Agent/
    ├── agent.py          # LangGraph agent logic (ReAct pattern)
    ├── tools.py          # Tavily search tool
    ├── app.py            # Streamlit chat UI
    ├── .env              # API keys (not committed)
    └── requirements.txt  # Python dependencies

## 🙋 Author
**Amitha Akepati**
[LinkedIn](https://linkedin.com/in/amithaake03) · [GitHub](https://github.com/AAmitha) · [Kaggle](https://kaggle.com/akepati)
