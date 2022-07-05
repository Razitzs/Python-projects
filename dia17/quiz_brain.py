from pickle import FALSE


class QuizBrain:
    def __init__(self, questionList):
        self.questionNumber=0
        self.questionList=questionList
        self.score=0

    def nextQuestion(self):
        text=(self.questionList[self.questionNumber].text).lower()
        uAnswer=input(f"Q.{self.questionNumber+1} {text} (True/False?): ")
        cAnswer=(self.questionList[self.questionNumber].answer).lower()
        self.questionNumber+=1
        self.checkAnswer(uAnswer,cAnswer)

    def stillHasQuestions(self):
        return self.questionNumber<len(self.questionList)

    def checkAnswer(self,uAnswer,cAnswer):
        if uAnswer==cAnswer:
            self.score+=1
            print("You got it right!!!")
        else:
            print("Thats wrong.")
        print(f"The answer was: {cAnswer}")
        print(f"Your current score is: {self.score}/{len(self.questionList)}")

