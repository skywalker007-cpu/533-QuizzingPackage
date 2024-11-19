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
    
    quiz_1 = Quiz()
    
    quiz_1.add(Q1)
    quiz_1.add(Q2)
    quiz_1.add(Q3)
    quiz_1.add([Q4, Q5, Q6, Q7])
    quiz_1.add({8: Q8, 9: Q9})
    
    
    quiz_2 = Quiz([Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9])
    quiz_2.remove(3)
    quiz_2.remove([1, 9, 8, 7, 5, 2, 4])
    
    print(quiz_1)
    print(quiz_2)

if __name__ == "__main__":
    main()