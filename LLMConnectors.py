import json
import re

from langchain_community.prompts import PromptTemplate
from langchain_ollama import Ollama

from SystemPrompts import resume_prompt


def clean_llm_json_output(raw_text: str) -> str:
    cleaned = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw_text.strip())
    return cleaned


class connect_with_llm:

    def prompt_creation(self, context="", query="", document=""):
        prompt_template = PromptTemplate(
            input_variables=["context", "query", "document"],
            template=resume_prompt
            .replace("{{CONTEXT}}", "{context}")
            .replace("{{QUERY}}", "{query}")
            .replace("{{DOCUMENT}}", "{document}")
        )
        llm = Ollama(
            model="mistral:latest",
            temperature=0.1,
            num_predict=500,
            top_p=0.95
        )
        chain = prompt_template | llm
        response = chain.invoke({
            "context": context,
            "query": query,
            "document": document
        })
        raw_output = response.content if hasattr(response, 'content') else str(response)
        cleaned_json = clean_llm_json_output(raw_output)

        try:
            parsed = json.loads(cleaned_json)
            return parsed
        except json.JSONDecodeError as e:
            print(f"JSON decoding error: {e}")
            print("LLM Raw Response:", raw_output)
            raise