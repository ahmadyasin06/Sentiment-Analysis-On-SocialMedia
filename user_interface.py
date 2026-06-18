import tkinter as tk
from tkinter import messagebox
from data.data_handler import DataHandler
from visualization.result_visualizer import ResultVisualizer


class SentimentUI:
    def __init__(self):
        self.handler = DataHandler()
        self.visualizer = ResultVisualizer()

        # Root Window
        self.root = tk.Tk()
        self.root.title("Social Media Sentiment Analyzer")
        self.root.geometry("720x450")
        self.root.configure(bg="#f4f6f8")
        self.root.resizable(False, False)

        # Title
        tk.Label(
            self.root,
            text="Social Media Sentiment Analysis",
            font=("Montserrat", 22, "bold"),
            bg="#f4f6f8",
            fg="#2c3e50"
        ).pack(pady=15)

        # Main Frame (Card Style)
        self.card = tk.Frame(self.root, bg="white", bd=0)
        self.card.pack(padx=20, pady=10, fill="both", expand=True)

        # Input Section
        tk.Label(
            self.card,
            text="Analyze a Post or Comment",
            font=("Montserrat", 14, "bold"),
            bg="white",
            fg="#34495e"
        ).pack(pady=(15, 5))

        self.text_input = tk.Text(
            self.card,
            height=3,
            width=55,
            font=("Segoe UI", 11),
            bd=1,
            relief="solid"
        )
        self.text_input.pack(pady=8)

        # Buttons Frame
        btn_frame = tk.Frame(self.card, bg="white")
        btn_frame.pack(pady=10)

        tk.Button(
            btn_frame,
            text="Analyze Sentiment",
            command=self.analyze,
            font=("Montserrat", 11, "bold"),
            bg="#3498db",
            fg="white",
            width=18,
            cursor="hand2",
            bd=0
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            btn_frame,
            text="Fetch Posts",
            command=self.fetch_posts,
            font=("Montserrat", 11, "bold"),
            bg="#2ecc71",
            fg="white",
            width=18,
            cursor="hand2",
            bd=0
        ).grid(row=0, column=1, padx=10)

        # Result Section
        self.result_label = tk.Label(
            self.card,
            text="Sentiment will appear in next window. Be patient!",
            font=("Segoe UI", 14),
            bg="white",
            fg="#2c3e50",
            justify="center"
        )
        self.result_label.pack(pady=20)

        self.root.mainloop()

    def analyze(self):
        text = self.text_input.get("1.0", tk.END).strip()

        if not text:
            messagebox.showwarning("Input Required", "Please enter some text to analyze.")
            return

        result = self.handler.process(text)
        emoji = self.visualizer.emoji(result["label"])

        # self.result_label.config(
        #     text=f"Sentiment: {result['label']} {emoji}\nConfidence: {result['confidence']}%"
        # )

        # Chart visualization
        self.visualizer.show_chart(result)

    def fetch_posts(self):
        post = self.handler.fetch_post_from_db()

        if not post:
            messagebox.showwarning(
                "No Data",
                "No posts found in the database."
            )
            return

        self.text_input.delete("1.0", tk.END)
        self.text_input.insert(tk.END, post)

        messagebox.showinfo(
            "Posts Fetched",
            "Social media post fetched from database successfully."
        )
