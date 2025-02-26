THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("quizzler")
        self.window.config(bg=THEME_COLOR)
        self.score=Label(text="Score:0", fg="white")
        self.score.config(pady=20,padx=20, bg=THEME_COLOR)
        self.score.grid(row=0, column=1, sticky="n")
        self.canvas=Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text=self.canvas.create_text(150, 125,text="Some Question Text", fill=THEME_COLOR, font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(pady=20,padx=20,row=1, column=0, columnspan=2)
        self.correct=PhotoImage(file="images/true.png")
        self.wrong = PhotoImage(file="images/false.png")

        self.true = Button(image=self.correct, bg=THEME_COLOR,activebackground=THEME_COLOR, highlightthickness=0, borderwidth=0, command=self.corrects)
        self.true.grid(column=0, row=2, sticky="EW",pady=20,padx=20)

        self.false = Button(image=self.wrong, bg=THEME_COLOR, activebackground=THEME_COLOR, highlightthickness=0,borderwidth=0, command=self.incorrect)
        self.false.grid(column=1, row=2, sticky="EW",pady=20,padx=20)
        self.get_next_question()
        self.window.mainloop()
        
    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score.config(text=f"score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="you've reached the end of the quiz")
            self.canvas.config(bg="white")
            self.true.config(state="disabled")
            self.false.config(state="disabled")
    def corrects(self):
        is_right=self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def incorrect(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

