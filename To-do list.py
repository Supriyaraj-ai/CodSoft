import customtkinter as ctk
import json
import os

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class SmartToDoApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("🧠 Smart To-Do Tracker")
        self.geometry("500x550")
        self.resizable(False, False)
        self.task_data = []

        self.task_input = ctk.CTkEntry(self, width=300, placeholder_text="Enter your task")
        self.task_input.place(x=30, y=20)

        add_btn = ctk.CTkButton(self, text="➕ Add Task", command=self.add_task)
        add_btn.place(x=350, y=20)

        clear_btn = ctk.CTkButton(self, text="🗑️ Clear All", fg_color="red", command=self.clear_all)
        clear_btn.place(x=380, y=480)

        self.task_frame = ctk.CTkScrollableFrame(self, width=440, height=420)
        self.task_frame.place(x=30, y=70)

        self.load_tasks()
        self.refresh_tasks()

    def add_task(self):
        task_text = self.task_input.get().strip()
        if task_text:
            self.task_data.append({"text": task_text, "done": False})
            self.task_input.delete(0, 'end')
            self.save_tasks()
            self.refresh_tasks()

    def toggle_status(self, index):
        self.task_data[index]["done"] = not self.task_data[index]["done"]
        self.save_tasks()
        self.refresh_tasks()

    def delete_task(self, index):
        del self.task_data[index]
        self.save_tasks()
        self.refresh_tasks()

    def clear_all(self):
        self.task_data.clear()
        self.save_tasks()
        self.refresh_tasks()

    def refresh_tasks(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        for index, task in enumerate(self.task_data):
            task_row = ctk.CTkFrame(self.task_frame)
            task_row.pack(padx=5, pady=5, fill="x")

            status_color = "#77dd77" if task["done"] else "#ff6961"
            label_text = f"✅ {task['text']}" if task["done"] else f"🔘 {task['text']}"

            task_label = ctk.CTkLabel(task_row, text=label_text, text_color=status_color, anchor="w")
            task_label.pack(side="left", padx=10, fill="x", expand=True)
            task_label.bind("<Button-1>", lambda e, i=index: self.toggle_status(i))

            del_btn = ctk.CTkButton(task_row, text="❌", width=35, fg_color="darkred", command=lambda i=index: self.delete_task(i))
            del_btn.pack(side="right", padx=5)

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.task_data, file, indent=4)

    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as file:
                self.task_data = json.load(file)


if __name__ == "__main__":
    app = SmartToDoApp()
    app.mainloop()