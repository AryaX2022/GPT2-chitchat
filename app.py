import gradio as gr
from interact2 import execute

def greet(name):
    ret = execute(name)
    return ret

demo = gr.Interface(fn=greet, inputs="text", outputs="text")

demo.launch(share=True) 
