import streamlit as st
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.pdf_agent import extract_text_from_pdf
from agents.arxiv_agent import search_arxiv
from core.agent_runner import run_agent

# Streamlit config
st.set_page_config(page_title="AI Research Agent", layout="wide")
st.title("AI Research Assistant")

# Optional summary mode
mode = st.radio("Summary Mode", ["📝 High-Level Summary", "🔬 Deep Technical Breakdown"])

# Upload + query
query = st.text_input("Ask a question (or upload a PDF below):")
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

# Helper: split PDF into chunks
def chunk_text(text, max_len=2000):
    return [text[i:i + max_len] for i in range(0, len(text), max_len)]

# Run agent
if st.button("Run Agent"):
    with st.spinner("Processing..."):
        if uploaded_file:
            with open("temp.pdf", "wb") as f:
                f.write(uploaded_file.read())
            pdf_text = extract_text_from_pdf("temp.pdf")
            chunks = chunk_text(pdf_text)

            results = []
            for i, chunk in enumerate(chunks):
                if mode == "📝 High-Level Summary":
                    prompt = f"""
You're a research assistant. Summarize the academic paper section below in 3 key bullet points.
Avoid repetition. Make it useful for someone scanning the paper quickly.

--- START CHUNK #{i+1} ---
{chunk}
--- END CHUNK ---
"""
                else:
                    prompt = f"""
You're an AI research assistant. Analyze the academic paper section below with a deep technical lens.

Extract:
1. Any mathematical concepts, attention mechanisms, or innovations
2. Definitions of any new components (e.g., embeddings, heads, architectures)
3. Clear paraphrase of the section’s technical contribution

Use markdown. Keep it compact, no fluff.

--- START CHUNK #{i+1} ---
{chunk}
--- END CHUNK ---
"""
                result = run_agent(prompt)
                results.append(f"### 📄 Section {i+1}\n{result}")

            final_output = "\n\n".join(results)
            st.success("Agent Response Complete:")
            st.markdown(final_output)

        else:
            # Free-form query
            result = run_agent(query)
            st.success("Agent Responded:")
            st.write(result)

# Arxiv search
st.divider()
st.subheader("📚 Search Academic Papers (arXiv)")
arxiv_query = st.text_input("Enter your research topic:")
if st.button("Search ArXiv"):
    with st.spinner("Searching arXiv..."):
        result = search_arxiv(arxiv_query)
        st.success("Papers Found:")
        st.markdown(result)
