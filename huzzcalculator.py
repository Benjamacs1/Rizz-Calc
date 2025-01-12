import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class HuzzChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("Huzz Calc (thats short for for calculator yk)")
        self.root.geometry("400x500")
        self.current_step = 1
        
        self.main_frame = tk.Frame(self.root, padx=20, pady=20)
        self.main_frame.pack(expand=True, fill='both')
        
        self.q1_frame = tk.Frame(self.main_frame)
        self.q1_frame.pack(fill='both', pady=10)
        
        self.rizz_label = tk.Label(self.q1_frame, text="Do you have rizz?", font=('Arial', 12))
        self.rizz_label.pack(pady=5)
        
        self.rizz_var = tk.StringVar()
        self.yes_button = tk.Radiobutton(self.q1_frame, text="Yes", variable=self.rizz_var, value="yes", command=self.handle_rizz_choice)
        self.no_button = tk.Radiobutton(self.q1_frame, text="No", variable=self.rizz_var, value="no", command=self.handle_rizz_choice)
        self.yes_button.pack()
        self.no_button.pack()
        
        self.q2_frame = tk.Frame(self.main_frame)
        self.q2_frame.pack(fill='both', pady=10)
        
        self.snap_label = tk.Label(self.q2_frame, text="What is your Snap Score?", font=('Arial', 12))
        self.snap_label.pack(pady=5)
        
        self.snap_entry = tk.Entry(self.q2_frame)
        self.snap_entry.pack(pady=5)
        
        self.alt_frame = tk.Frame(self.main_frame)
        self.alt_label = tk.Label(self.alt_frame, text="Is this your alt account?", font=('Arial', 12))
        self.alt_label.pack(pady=5)
        
        self.alt_var = tk.StringVar()
        tk.Radiobutton(self.alt_frame, text="Yes", variable=self.alt_var, value="yes", command=self.handle_alt_choice).pack()
        tk.Radiobutton(self.alt_frame, text="No", variable=self.alt_var, value="no", command=self.handle_alt_choice).pack()
        
        self.real_score_frame = tk.Frame(self.main_frame)
        self.real_score_label = tk.Label(self.real_score_frame, text="What is your real snap score?", font=('Arial', 12))
        self.real_score_label.pack(pady=5)
        
        self.real_score_entry = tk.Entry(self.real_score_frame)
        self.real_score_entry.pack(pady=5)
        
        self.result_label = tk.Label(self.main_frame, text="", font=('Arial', 12), wraplength=350)
        self.result_label.pack(pady=20)
        
        self.date_label = tk.Label(self.main_frame, text=f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", font=('Arial', 10))
        self.date_label.pack(pady=5)
        
        self.user_label = tk.Label(self.main_frame, text=f" {self.get_username()}", font=('Arial', 10))
        self.user_label.pack(pady=5)
        
        self.submit_btn = tk.Button(self.main_frame, text="Submit", command=self.check_answers)
        self.submit_btn.pack(pady=10)
        
        self.reset_btn = tk.Button(self.main_frame, text="Reset", command=self.reset_app)
        self.reset_btn.pack(pady=5)
        
        self.no_count = 0

    def get_username(self):
        return "RIZZ CALC"

    def handle_rizz_choice(self):
        if self.rizz_var.get() == "no":
            self.no_count += 1
            if self.no_count >= 3:
                messagebox.showwarning("Warning", "You really need to work on your rizz!")
                self.root.configure(bg='red')
                self.main_frame.configure(bg='red')
            else:
                messagebox.showinfo("Message", "Are you sure about that?")

    def handle_alt_choice(self):
        if self.alt_var.get() == "yes":
            self.real_score_frame.pack()
        else:
            self.real_score_frame.pack_forget()

    def check_answers(self):
        try:
            rizz = self.rizz_var.get()
            snap_score = self.snap_entry.get()
            
            if not rizz or not snap_score:
                messagebox.showerror("Error", "Please fill in all fields!")
                return
                
            snap_score = int(snap_score)
            
            if snap_score >= 100000:
                self.result_label.config(text="Very active on social media!")
                self.alt_frame.pack_forget()
                self.real_score_frame.pack_forget()
            else:
                self.alt_frame.pack()
                
                if self.alt_var.get() == "yes":
                    self.real_score_frame.pack()
                    try:
                        real_score = int(self.real_score_entry.get())
                        if real_score >= 100000:
                            self.result_label.config(text="That's a very high score!")
                        else:
                            self.result_label.config(text="Why are you hiding that?")
                    except ValueError:
                        if self.real_score_entry.get():
                            messagebox.showerror("Error", "Please enter a valid number!")
                elif self.alt_var.get() == "no":
                    self.result_label.config(text="Keep being active!")
            
            if rizz == "yes":
                self.result_label.config(text=self.result_label.cget("text") + "\nCongrats, you got rizz!")
            else:
                self.result_label.config(text=self.result_label.cget("text") + "\nGet that rizz up!")
                
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for the score!")

    def reset_app(self):
        self.rizz_var.set("")
        self.snap_entry.delete(0, tk.END)
        self.alt_var.set("")
        self.real_score_entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.alt_frame.pack_forget()
        self.real_score_frame.pack_forget()
        self.no_count = 0
        self.root.configure(bg='SystemButtonFace')
        self.main_frame.configure(bg='SystemButtonFace')

if __name__ == "__main__":
    root = tk.Tk()
    app = HuzzChecker(root)
    root.mainloop()