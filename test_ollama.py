from agno.agent import Agent, RunResponse
from agno.models.ollama import Ollama

from ollama import Client


agent = Agent(
    model=Ollama(id="deepseek-r1", host="http://ai:11434"),
    markdown=True
)

# Print the response in the terminal
agent.print_response("Share a 2 sentence horror story.")
