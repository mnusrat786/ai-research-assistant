## AI Research Assistant
Upload a PDF or ask a research question get structured summaries and explore related arXiv papers.
Runs fully offline using LangChain, Ollama, and Streamlit.
No API keys required. Just plug and run.

##   Getting Started

###  Repository

```bash
git clone https://github.com/mnusrat786/ai-research-assistant.git
cd ai-research-assistant
```
### Requirements

- Python 3.10 or later  
- [Ollama](https://ollama.com) (for running local AI models like `mistral`)  
- Git

---

## 1. Install Ollama + Mistral Model

1. Download Ollama: [https://ollama.com/download](https://ollama.com/download)  
2. Open a terminal and run:

```bash
ollama run mistral
```
This will automatically download the Mistral model locally. Make sure Ollama is running in the background before you run the app.

## 2. Setup Virtual Environment

```bash
python -m venv .venv

# Activate it
# On Windows:
.venv\Scripts\activate

# On Mac/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```
## 3. Run the App
```bash
streamlit run app/main.py
```
## 4. Dashboard
![image](https://github.com/user-attachments/assets/7efbaaee-f549-45b4-94a6-abfd82b9fd85)


