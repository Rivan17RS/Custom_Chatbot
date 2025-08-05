import os
import gradio as gr
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

messages = [{"role": "system", "content": "You are a helpful assistant."}]

def CustomChatbot(user_message):
    if not user_message:
        return "", ""

    messages.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    assistant_message = response.choices[0].message.content
    messages.append({"role": "assistant", "content": assistant_message})

    chat_history = format_chat_history(messages)
    return assistant_message, chat_history

def format_chat_history(msgs):
    history = []
    for msg in msgs[1:]:
        role = "🧑" if msg["role"] == "user" else "🤖"
        history.append(f"{role}: {msg['content']}")
    return "\n\n".join(history)

def reset_chat():
    global messages
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    return "", ""

custom_css = """
#send-button {
    background-color: #32CD32 !important; /* Vivid Lime Green */
    color: white !important;
    border: none;
    font-weight: bold;
}
#send-button:hover {
    background-color: #28a428 !important;
}

#reset-button {
    background-color: #C62828 !important; /* Deep Crimson */
    color: white !important;
    border: none;
    font-weight: bold;
}
#reset-button:hover {
    background-color: #a81f1f !important;
}
"""

with gr.Blocks(css=custom_css) as demo:
    gr.Markdown("## 🤖 Rivan Custom Chatbot")

    user_input = gr.Textbox(label="Your Message", placeholder="Type your message here...", lines=2)
    
    with gr.Row():
        send_btn = gr.Button("Send", elem_id="send-button")
        reset_btn = gr.Button("Reset Conversation", elem_id="reset-button")

    response_output = gr.Textbox(label="Assistant Response", lines=3)
    chat_history = gr.Textbox(label="Chat History", lines=15, interactive=False)

    send_btn.click(fn=CustomChatbot,
                   inputs=[user_input],
                   outputs=[response_output, chat_history])

    reset_btn.click(fn=reset_chat,
                    inputs=[],
                    outputs=[response_output, chat_history])

demo.launch(share=True)
