# import libraries
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent

# Our Function to take texst

def Legal_Researcher(input_variable,language):
  input_variable = input_variable+" . " +language
  # create a new openai api key
  os.environ["OPENAI_API_KEY"] = "...."
  # set up openai api key
  openai_api_key = os.environ.get('OPENAI_API_KEY')

  # Load in some tools to use
  os.environ["SERPAPI_API_KEY"] = "...."

  # set up openai api key
  openai_api_key = os.environ.get('SERPAPI_API_KEY')
 
  # create a model
  llm = OpenAI(temperature = 0.9)

  tools = load_tools(["serpapi", "llm-math"], llm=llm)

  agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
  Output_For_Function =agent.run(input_variable) 
 

  return Output_For_Function
