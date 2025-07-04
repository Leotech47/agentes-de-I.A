# Template: Agente de IA Personalizado com seu Estilo

from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

# 1. Inicialize o modelo de linguagem (pode ser GPT-4 via OpenAI)
llm = ChatOpenAI(temperature=0.3, model_name="gpt-4")

# 2. Memória para manter contexto de conversa
memory = ConversationBufferMemory(memory_key="chat_history")

# 3. Prompt personalizado com seu estilo
prompt = PromptTemplate(
    input_variables=["input"],
    template="""
    Você é Leonardo, servidor público atuante na área de segurança institucional. 
    Seu estilo de comunicação é claro, direto, profissional e com foco em análise técnica.
    Quando responder, use linguagem objetiva e fundamente suas respostas em boas práticas de segurança, análise de risco e legislação pertinente quando aplicável.
    
    Pergunta do usuário: {input}
    """
)

# 4. Ferramentas (opcional - adicionar consultas a banco de dados, API, etc.)
tools = []  # Pode incluir futuramente

# 5. Inicializa o agente com LLM, prompt e memória
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="chat-conversational-react-description",
    memory=memory,
    verbose=True
)

# 6. Função para executar o agente com o prompt personalizado
def responder_com_estilo_leonardo(pergunta):
    entrada_formatada = prompt.format(input=pergunta)
    resposta = agent.run(entrada_formatada)
    return resposta

# 7. Teste (remova ao usar em produção)
if __name__ == "__main__":
    pergunta = "Quais são os cuidados essenciais em uma análise de risco institucional?"
    print(responder_com_estilo_leonardo(pergunta))
