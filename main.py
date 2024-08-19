
from crewai import Crew, Process
# from crewai.crews.crew_output import CrewOutput
from recruitment_agent import RecruitmentAgent
from recruitment_task import RecruitmentTask
import json
import os
import spacy
# from config import Config

params = request.json

market_researcher_agent = RecruitmentAgent.market_research_agent()
jd_creation_agent = RecruitmentAgent.Jd_creation_agent()

market_research_task = RecruitmentTask.market_research(params['job_title'] , params['experience'] ,market_researcher_agent)
jd_creation_task = RecruitmentTask.jd_creation(params['job_title'] , params['experience'] , params['technical_skills'] , jd_creation_agent)

crew = Crew(
    agents=[market_researcher_agent,jd_creation_agent],
    tasks=[market_research_task,jd_creation_task],
    verbose=True,
)

result = crew.kickoff()

print(result)