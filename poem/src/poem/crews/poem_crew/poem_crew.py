from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from utils import get_api_key

gemini_api_key = get_api_key('GEMINI_API_KEY')

llm = LLM(
    api_key=gemini_api_key,
    model='gemini/gemini-1.5-flash'
)

@CrewBase
class PoemCrew():
	
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def poem_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['poem_writer'],
			llm=llm
		)

	@task
	def write_poem(self) -> Task:
		return Task(
			config=self.tasks_config['write_poem'],
		)

	@crew
	def crew(self) -> Crew:
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
		)