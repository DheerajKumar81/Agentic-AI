from dotenv import load_dotenv
import os
from crewai import Agent, Task, Crew, LLM

load_dotenv()

#Use local LLM from Ollama
llm = LLM(
    model='ollama/tinylamma',
    base_url='http://localhost:11434'
)

#Creating Agent 
email_writer =  Agent(
    role='Professional Email Writer',
    goal='Write clear professional emails',
    backstory='You are an expert corporate communication specialist.',
    llm=llm,
    verbose=True
)

#Define task
write_email = Task(
    description='Write a professional email requesting leave tomorrow due to personal reasons.',
    expected_output='A well formatted professional email with subject line.',
    agent=email_writer
)

#Crew crew
crew = Crew(
    agents=[email_writer],
    tasks=[write_email],
    verbose=True
)

#Run agent
result = crew.kickoff()
