# Modern 2026 import
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from models.task_model import TaskList
from utils.gemini_client import get_gemini_model

def create_schedule_agent():

    llm = get_gemini_model()

    parser = PydanticOutputParser(pydantic_object=TaskList)

    prompt = PromptTemplate(
        template="""
You are an AI scheduling assistant.

Extract tasks from the message and convert them into structured schedule items.

Return JSON with:
- task
- date
- time
- priority (if mentioned)

Message:
{message}

{format_instructions}
""",
        input_variables=["message"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )

    chain = prompt | llm | parser

    return chain