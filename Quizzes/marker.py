from Objects.question import ShortAnswerQuestion
from Objects.response import Response
import Objects.question as question

class Marker:
    def __init__(self):
        pass
    def mark(self, question_list, response, studentId): 
        '''
        Mark a quiz based on the response and question's answers.
        '''
        total_mark = 0
        formal_answer_list = []
        verifier = False
        try:
            if len(question_list) != len(response):
                raise ValueError("The number of responses does not match the number of questions in the quiz.")
            if isinstance(response, list):
                for q_content in question_list.values():
                    formal_answer_list.append(q_content["answer"])
                for i in range(len(response)):
                    if response[i] == formal_answer_list[i]:
                        verifier = True
                        total_mark += 1
                    else:
                        verifier = False
            else:
                raise ValueError("The response is not a valid response object.")
        except ValueError as e:
            print(e)
        return total_mark
