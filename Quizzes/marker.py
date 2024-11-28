from Quizzes.quiz import Quiz
from Questions.question import ShortAnswerQuestion
def mark(quiz, studentId): 
    '''
    Mark a quiz based on the response and question's answers.
    '''
    total_mark = 0
    formal_answer_list = []
    verifier = False
    user_response_list = quiz.responses[studentId].response
    if isinstance(quiz, Quiz):
        for q_content in quiz.questions.values():
            formal_answer_list.append(q_content["answer"])
        for i in range(len(user_response_list)):
            if user_response_list[i] == formal_answer_list[i]:
                verifier = True
                total_mark += 1
            else:
                verifier = False

    if(not verifier and isinstance(quiz, ShortAnswerQuestion)):
       # need to handle short answer question here.
       pass

    # return total score student get.
    return total_mark