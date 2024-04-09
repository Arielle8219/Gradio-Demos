import gradio as gr

def greet(name, intensity):
    return "Hello " * intensity + name + "!"

demo = gr.Interface(

    # fn is anything to wrap the interface around, can be any python function
    fn=greet,

    # look into components: https://www.gradio.app/docs/components 
    inputs=["text", "slider"],
    outputs=["text"],
)

demo.launch(share = True)