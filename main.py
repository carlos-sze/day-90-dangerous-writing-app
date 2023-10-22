import tkinter as tk


class DangerousWritingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dangerous Writing App")
        self.geometry("600x400")

        self.text_area = tk.Text(self, height=10)
        self.text_area.pack(fill=tk.BOTH, expand=True)
        self.text_area.bind("<Key>", self.reset_timer)

        self.word_counter = tk.Label(self, text="Words: 0")
        self.word_counter.pack(side=tk.BOTTOM)

        self.timer_id = None
        self.word_count = 0

    def reset_timer(self, event):
        if self.timer_id:
            self.after_cancel(self.timer_id)
        self.timer_id = self.after(10000, self.clear_text)

        # Update word count
        text = self.text_area.get("1.0", tk.END)
        self.word_count = len(text.split())
        self.word_counter.configure(text=f"Words: {self.word_count}")

    def clear_text(self):
        self.text_area.delete("1.0", tk.END)
        self.word_count = 0
        self.word_counter.configure(text="Words: 0")


app = DangerousWritingApp()
app.mainloop()