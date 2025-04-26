from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from pydantic import BaseModel
import os


# llms
os.environ['GROQ_API_KEY'] = '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'
llama_llm = LLM(
    model = "groq/llama-3.3-70b-versatile",
    temperature= 0.0
)

gemma_llm = LLM(
    model = "groq/gemma2-9b-it",
    temperature= 0.0
)

llama_instant_llm = LLM(
    model = "groq/llama-3.1-8b-instant",
    temperature= 0.0
)

llama_guard = LLM(
    model = "groq/llama-guard-3-8b",
    temperature= 0.0
)


# structured outputs

# Rules Agent ------------------------------
class credit_JSON(BaseModel):
  english_course: str
  current_semester: int
  registration_semester: int
  ordinary_registration_semester_credit_hours: int
  student_maximum_credit_hours: int
  reasoning: str


class Prioritisied(BaseModel):
  prioritisied_courses: list
  reasoning: str

class Selected(BaseModel):
  selected_courses: list
  reasoning: str
  total_credit_hours: int


@CrewBase
class RulesCrew():
	"""University Academic crew specializing in course registration policies."""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def rules_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['rules_agent'],
			llm = llama_llm,
			verbose=True
		)

	@task
	def rules_task(self) -> Task:
		return Task(
			config=self.tasks_config['rules_task'],
			output_json = credit_JSON,
			output_file = './outputs/credits.json',
		)


	# crews -------------------------
	@crew
	def crew(self) -> Crew:
		"""Creates the Rules crew"""

		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
		)
	


#priorities Agent --------------------------------------
@CrewBase
class PriorityCrew():
	"""University Course crew specializing in course prioritization and academic planning."""

	agents_config = 'config/agents_p.yaml'
	tasks_config = 'config/tasks_p.yaml'

	@agent
	def courses_prioritizer(self) -> Agent:
		return Agent(
			config=self.agents_config['courses_prioritizer'],
			llm = llama_llm,
			verbose=True
		)

	@task
	def rank_courses_task(self) -> Task:
		return Task(
			config=self.tasks_config['rank_courses_task'],
			output_json = Prioritisied,
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Priority crew"""

		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
		)
	


# selection Agent --------------------------------------
@CrewBase
class SelectionCrew():
	"""University Course Selection crew specializing in optimized course scheduling."""

	agents_config = 'config/agents_s.yaml'
	tasks_config = 'config/tasks_s.yaml'

	@agent
	def courses_selector(self) -> Agent:
		return Agent(
			config=self.agents_config['courses_selector'],
			llm = llama_llm,
			verbose=True
		)

	@task
	def select_courses_task(self) -> Task:
		return Task(
			config=self.tasks_config['select_courses_task'],
			output_json = Selected,
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the selection crew"""

		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
		)