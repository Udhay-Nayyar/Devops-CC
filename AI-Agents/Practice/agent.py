from strands import Agent
from strands.models.ollama import OllamaModel
from strands_tools import http_request


ollama_model = OllamaModel(
    host="http://localhost:11434",  # Ollama server address
    model_id="llama3.2:3b"             # Specify which model to use
)

system_prompt = """
You are a helpful and friendly AI agent.

Answer the user's questions in a natural, normal, and conversational way.
Keep your answers clear and easy to understand.

When you need current or real-time information, use the available tools
and free public APIs instead of guessing.

For example:
- For today's date or current time, use an appropriate API/tool.
- For weather, use a weather API if available.
- For current information, use an available API when appropriate.
- For general knowledge and simple questions, answer normally without
  using a tool.

Do not make up information or API results.
If you cannot find the required information, simply say so.

Be helpful, concise, and friendly.
Talk like a normal assistant, not like a robot.
"""



agent = Agent(model=ollama_model,system_prompt=system_prompt,tools = [http_request])



question = input("Enter the question you wanat to asks : ")
agent(question)

# using locally installed agents use 
# ollama 

    