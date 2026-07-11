# LangChain Learning Journey 🚀

This repository documents my hands-on learning journey in **LangChain** and **Generative AI**. The goal is to understand the core concepts by building small, focused examples before moving on to larger applications such as RAG systems, AI agents, and production-ready LLM applications.

Rather than jumping directly into complete projects, this repository is organized concept by concept to build a strong foundation.

---

## 📚 Topics Covered

### ✅ Prompt Engineering

* Prompt Templates
* Chat Prompt Templates
* Message Placeholders
* Prompt Generation
* Conversation History

### ✅ Chat Models

* Google Gemini
* Groq (Llama 3.3 70B)
* Hugging Face Models

### ✅ Large Language Models (LLMs)

* Basic LLM interaction
* Model configuration
* Temperature and generation settings

### ✅ Embedding Models

* Google Gemini Embeddings
* Open Source Embeddings
* Document Similarity
* Multiple Embedding Examples

### ✅ Output Parsers

* String Output Parser
* JSON Output Parser
* Structured Output Parser
* Pydantic Output Parser

### ✅ Structured Output

* Pydantic Schemas
* TypedDict
* JSON Schema
* Structured Responses

### ✅ Chains

* Simple Chains
* Sequential Chains
* Parallel Chains
* Conditional Chains

---

## 📂 Repository Structure

```text
LangChain/
│
├── CHAINS/
│   ├── simplechains.py
│   ├── sequencialchain.py
│   ├── parellalchains.py
│   └── conditionalchains.py
│
├── CHATMODELS/
│
├── EMBEDDEDMODELS/
│
├── LLMS/
│
├── OUTPUT_PARSERS/
│
├── PROMPTS/
│
├── STRUCTURED_OUTPUT/
│
├── requirements.txt
├── notes.txt
└── README.md
```

---

## 🛠️ Technologies Used

* Python
* LangChain
* LangChain Core
* Groq API
* Google Gemini API
* Hugging Face
* Pydantic
* NumPy
* Scikit-learn
* python-dotenv

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/Nipun1311/GenAI.git
cd GenAI
```

### Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file in the project root and add your API keys.

Example:

```env
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_api_key
```

---

## 🎯 Learning Philosophy

My approach is simple:

> Learn one concept at a time. Build with it. Repeat.

Instead of memorizing APIs, I aim to understand how each LangChain component works and how they fit together to build real-world LLM applications.

---

## 📈 Current Progress

* ✅ Prompt Templates
* ✅ Chat Models
* ✅ LLM Integration
* ✅ Embedding Models
* ✅ Output Parsers
* ✅ Structured Outputs
* ✅ Simple Chains
* ✅ Sequential Chains
* ✅ Parallel Chains
* ✅ Conditional Chains

---

## 🔜 Next Steps

* Retrieval-Augmented Generation (RAG)
* Document Loaders
* Text Splitters
* Vector Databases
* Retrieval Chains
* Memory
* AI Agents
* Tools
* Model Context Protocol (MCP)
* LangGraph
* Evaluation
* Deployment

---

## 🤝 Contributions

This repository is primarily a personal learning resource. Suggestions, improvements, and discussions are always welcome.

---

## ⭐ Acknowledgements

Thanks to the LangChain community and the creators of the open-source tools and educational resources that make learning Generative AI accessible.
