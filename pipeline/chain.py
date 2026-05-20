from langchain_anthropic import ChatAnthropic
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(model="claude-haiku-4-5-20251001")

prompt = ChatPromptTemplate.from_template("""
    PLACEHOLDER
""")

chain = prompt | llm

def generate_report(player : dict) -> str:
    report = chain.invoke({
        # placeholder
    })

    return report.content