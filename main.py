import tkinter as tk
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below

Here is the conversation history: {context}

Question: {question}

Answer:
"""
model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pybot")
        self.root.geometry("500x600")
        self.root.configure(bg='#2E2E2E')

        self.title_label = tk.Label(self.root, text="Pybot", font=("Times New Roman", 24), fg="#FFFADA", bg='#2E2E2E')
        self.title_label.pack(pady=5)

        self.subtitle_label = tk.Label(self.root, text="How may I help you?", font=("Times New Roman", 12), fg="white", bg='#2E2E2E')
        self.subtitle_label.pack(pady=0)

        self.chat_display = tk.Text(self.root, wrap=tk.WORD, width=60, height=23, font=("Times New Roman", 12), bg='#1e1e1e', fg='#FFFADA', bd=0)
        self.chat_display.pack(pady=10)
        self.chat_display.config(state=tk.DISABLED)

        self.chat_display.tag_configure("user_label", foreground="#40E0D0", justify="right")
        self.chat_display.tag_configure("user_text", foreground="white", justify="right")
        self.chat_display.tag_configure("bot_label", foreground="#40E0D0", justify="left")
        self.chat_display.tag_configure("bot_text", foreground="white", justify="left")

        self.input_frame = tk.Frame(self.root, bg='#2E2E2E')
        self.input_frame.pack(fill=tk.X, pady=5)

        self.entry_message = tk.Entry(self.input_frame, font=("Times New Roman", 14), bg='#444444', fg='white', bd=2, relief="flat")
        self.entry_message.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, ipady=8)
        self.entry_message.bind("<Return>", self.send_message)

        self.send_button = tk.Button(self.input_frame, text="Send", command=self.send_message, font=("Times New Roman", 14), fg="white", bg="#40E0D0", relief="flat", width=10)
        self.send_button.pack(side=tk.RIGHT, padx=10)

        self.context = ""  

    def send_message(self, event=None):
        user_input = self.entry_message.get()
        if user_input != "":
            self.chat_display.config(state=tk.NORMAL)

            self.chat_display.insert(tk.END, "You: ", "user_label")
            self.chat_display.insert(tk.END, user_input + "\n", "user_text")

            self.chat_display.config(state=tk.DISABLED)
            self.entry_message.delete(0, tk.END)

            result = self.get_ai_response(user_input)

            self.chat_display.config(state=tk.NORMAL)

       
            self.chat_display.insert(tk.END, "Pybot: ", "bot_label")
        
            self.chat_display.insert(tk.END, result + "\n", "bot_text")

            self.chat_display.config(state=tk.DISABLED)
            self.chat_display.yview(tk.END)

    def get_ai_response(self, user_input):
        result = chain.invoke({"context": self.context, "question": user_input})
        self.context += f"\nUser: {user_input}\nAI: {result}"
        return result

root = tk.Tk()
app = ChatbotApp(root)
root.mainloop()
