from agno.agent import Agent, RunResponse
from agno.models.ollama import Ollama

from ollama import Client


agent = Agent(
    model=Ollama(id="deepseek-r1", host="http://ai:11434"),
    markdown=True,
    tools=[
        BitbucketClient(base_url="https://api.bitbucket.org/2.0", workspace="stoneridgetechnology")
    ]
)

# Print the response in the terminal
agent.print_response("Summarize the changes in the pull request 4300 in the echelon repository.")
