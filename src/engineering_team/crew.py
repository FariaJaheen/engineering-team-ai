from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class EngineeringTeam:
    """Engineering team crew: design -> backend -> frontend -> tests"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def engineering_lead(self) -> Agent:
        return Agent(
            config=self.agents_config["engineering_lead"],  # type: ignore[index]
            verbose=True,
        )

    @agent
    def backend_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config["backend_engineer"],  # type: ignore[index]
            verbose=True,
            allow_code_execution=True,
            code_execution_mode="safe",
            max_execution_time=240,
            max_retry_limit=5,
        )

    @agent
    def frontend_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config["frontend_engineer"],  # type: ignore[index]
            verbose=True,
        )

    @agent
    def test_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config["test_engineer"],  # type: ignore[index]
            verbose=True,
            allow_code_execution=True,
            code_execution_mode="safe",
            max_execution_time=240,
            max_retry_limit=5,
        )

    @task
    def design_task(self) -> Task:
        return Task(
            config=self.tasks_config["design_task"],  # type: ignore[index]
        )

    @task
    def code_task(self) -> Task:
        return Task(
            config=self.tasks_config["code_task"],  # type: ignore[index]
        )

    @task
    def frontend_task(self) -> Task:
        return Task(
            config=self.tasks_config["frontend_task"],  # type: ignore[index]
        )

    @task
    def test_task(self) -> Task:
        return Task(
            config=self.tasks_config["test_task"],  # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )