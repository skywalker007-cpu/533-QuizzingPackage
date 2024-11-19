from Quiz import Quiz
import Question

def main():
    Q1 = Question.MultipleChoice(1, "What is the capital of France?", "Paris", 1, ["Paris", "London", "Berlin", "Madrid"])
    Q2 = Question.ShortAnswerQuestion(2, "What is the capital of France?", "Paris", 1, "Please answer in one word")
    Q3 = Question.TrueFalseQuestion(3, "Is Paris the capital of France?", "True", 1, ["True", "False"])
    Q4 = Question.MultipleChoice(4, "What is the capital of France?", "Paris", 1, ["Paris", "London", "Berlin", "Madrid"])
    Q5 = Question.ShortAnswerQuestion(5, "What is the capital of France?", "Paris", 1, "Please answer in one word")
    Q6 = Question.TrueFalseQuestion(6, "Is Paris the capital of France?", "True", 1, ["True", "False"])
    Q7 = Question.MultipleChoice(7, "What is the capital of France?", "Paris", 1, ["Paris", "London", "Berlin", "Madrid"])
    Q8 = Question.ShortAnswerQuestion(8, "What is the capital of France?", "Paris", 1, "Please answer in one word")
    Q9 = Question.TrueFalseQuestion(9, "Is Paris the capital of France?", "True", 1, ["True", "False"])
    
    quiz = Quiz()
    
    quiz.add(Q1)
    quiz.add(Q2)
    quiz.add(Q3)
    quiz.add([Q4, Q5, Q6, Q7])
    quiz.add({8: Q8, 9: Q9})
    
    print(quiz)

if __name__ == "__main__":
    main()