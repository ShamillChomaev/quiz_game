from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250,bg='white')
        self.canvas.grid(row=1,column=0,  columnspan=2, pady=50)
        self.text = self.canvas.create_text(150,125,
                                            width=280,
                                            text="Some text",
                                            fill=THEME_COLOR,
                                            font=("Arial",20, "italic"))
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)
        self.trueimg = PhotoImage(file="images/true.png")
        self.falseimg = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.trueimg, highlightthickness=0, command=self.right_answer)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=self.falseimg, highlightthickness=0, command=self.wrong_answer)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="You have reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def right_answer(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)

    def wrong_answer(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)