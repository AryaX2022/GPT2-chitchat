import gradio as gr
from interact2 import execute

def greet(name):
    ret = execute(name)
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")

demo.launch() 