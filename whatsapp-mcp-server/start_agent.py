from praisonaiagents import Agent

agent = Agent(
    instructions="Eres un asistente que envía mensajes por WhatsApp generados con Ollama.",
    llm="ollama/llama3.2",
    mcp="generate_and_send C:/Proyectos-Marlenne/WhatsApp-server/whatsapp-mcp/whatsapp-mcp-server/main.py"
)

agent.start("Envía un mensaje motivacional para el equipo de ventas.")