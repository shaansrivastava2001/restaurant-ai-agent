from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

from vector import retriever


model = OllamaLLM(model="llama3.2")

template = """
You are expert agent in answering questions about pizza restaurants.

Here are some relevant reviews: {reviews}

Here is the question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

result = chain.invoke({
    "reviews": [],
    "question": "What is the best pizza place in town?"
})

while True:
    print("\n\n")
    question = input("Ask a question, or enter q/exit to quit: ")
    if question == 'q' or question == 'exit':
        break
    reviews = retriever.invoke(question)
    result = chain.invoke({ "reviews": reviews, "question": question })
    print(result)