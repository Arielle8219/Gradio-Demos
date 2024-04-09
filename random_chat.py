import time
import gradio as gr
from datetime import datetime
import pandas as pd


initial_data = {
    'user': ["Anonymous user"],
    'date': [datetime.now().date()],
    'identifier': ["ID: A123910928"],
    'config': ['config']
}

pandDF = pd.DataFrame(initial_data)

json_configs = {
  "lilly-openai-v1": {
    "model_class": "lilly-openai",
    "model_class_index_alias": "null",
    "model_iteration": 1,
    "embedding": {
      "model": "text-embedding-ada-002",
      "chunk_size": 16,
      "iteration": 1,
      "compute_type": "external",
      "open_api_type": "azure"
    },
    "llm": {
      "model_name": "text-davinci-003",
      "deployment_name": "text-davinci-003",
      "token_limit": 4097,
      "max_response_token_size": 1000
    }
  },
  "lilly-openai-v2": {
    "model_class": "lilly-openai",
    "model_class_index_alias": "null",
    "model_iteration": 2,
    "embedding": {
      "model": "text-embedding-ada-002",
      "chunk_size": 16,
      "iteration": 1,
      "compute_type": "external",
      "open_api_type": "azure"
    },
    "llm": {
      "model_name": "gpt-4",
      "deployment_name": "gpt-4",
      "token_limit": 8000,
      "max_response_token_size": 1000
    }
  },
  "lilly-openai-v3": {
    "model_class": "lilly-openai",
    "model_class_index_alias": "null",
    "model_iteration": 3,
    "embedding": {
      "model": "text-embedding-ada-002",
      "chunk_size": 16,
      "iteration": 1,
      "compute_type": "external",
      "open_api_type": "azure"
    },
    "llm": {
      "model_name": "gpt-4-32k",
      "deployment_name": "gpt-4-32k",
      "token_limit": 32768,
      "max_response_token_size": 5000
    }
  },
  "lilly-openai-v4": {
    "model_class": "lilly-openai",
    "model_class_index_alias": "null",
    "model_iteration": 4,
    "embedding": {
      "model": "text-embedding-ada-002",
      "chunk_size": 16,
      "iteration": 1,
      "compute_type": "external",
      "open_api_type": "azure"
    },
    "llm": {
      "model_name": "gpt-4-1106-preview",
      "deployment_name": "gpt-4-1106-preview",
      "token_limit": 128000,
      "max_response_token_size": 20000
    }
  }
}

def random_response(message, history):
    for i in range(len(message)):
        time.sleep(0.3)
        yield "You typed: " + message[: i+1]



def message_config(message, history, config):

    global pandDF
    current_date = datetime.now().date()
    user = "Anonymous user"
    identifier = "ID: 109203123018"
    if config == "":
        config = "lilly-openai-v1"
    config = json_configs[config]

    #data = {'user': user, 'date': [current_date], 'identifier': [identifier], 'config': [config]}
    data = {'user': user, 'date': current_date, 'identifier': identifier, 'config': config}
    pandDF = pandDF.append(data, ignore_index = True)

    print(pandDF)
    #df.update(df)


    response = f"You chose {config}."
    yield response

with gr.Blocks() as chat:

    #textbox=gr.Textbox(placeholder="Add additional Prompt", label="System Prompt")
    dataframe = gr.Dataframe(
        headers=["user", "date", "identifer", "config"],
        datatype=["str", "date", "str", "str"],
        row_count=5,
        col_count=(4, "fixed"),
        type = "pandas",
        value=pandDF
        #data = initial_data
    ) 
    
    #df = df_block.get_data()
    config = gr.Dropdown(
            ["lilly-openai-v1", "lilly-openai-v2", "lilly-openai-v4", 
             "lrl-md3-openai-v1"], 
            #default = "lilly-openai-v1", 
            label= "Config", 
            info="Will add more configs later!"
    )
    system_prompt = gr.Textbox("You are helpful AI.", label="System Prompt")
    gr.ChatInterface(
        message_config, additional_inputs=[config]
    )



chat.launch(share = True)

