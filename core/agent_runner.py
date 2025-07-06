from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_community.llms import Ollama

llm = Ollama(model="llama2")
memory = ConversationBufferMemory()
chain = ConversationChain(llm=llm, memory=memory, verbose=True)

def run_agent(prompt):
    return chain.run(prompt)
