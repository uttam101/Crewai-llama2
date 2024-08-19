from crewai import Agent
from langchain_community.llms import Ollama
from dotenv import load_dotenv
import os

load_dotenv()

llm = Ollama(
    model=os.getenv("LLM_MODEL_NAME"), # model name
    base_url=os.getenv("OLLAMA_API_BASE") # ollama api url
)

class RecruitmentAgent():

    def Jd_creation_agent():
        return Agent(
            role="Job Description Creator",
            goal="create best job description as per the job role and skills",
            backstory="An expert in creating professional job descriptions for a job role is required with extensive information",
            llm=llm,
            memory=True,
            allow_delegation=False,
            verbose = True
        )

    def market_research_agent():
        return Agent(
            role="Market Research Expert",
            goal="research market trends and opportunities based on the job role, skills and current market standard",
            backstory="An expert in market research is known about the market trends and opportunities based on the job role, skills and current market standard",
            llm=llm,
            memory=True,
            allow_delegation=False,
            verbose = True
        )
