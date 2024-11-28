from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import Questions.question as question
from Responses.response import Response


class Quiz:
    def __init__(self, title = "untitled_quiz", questions = None, responses = None):
        self.title = title
        self.total_score = 0

        self.questions = {}
        self.responses = responses if responses is not None else {}
        if questions is not None:
            self.add_questions(questions)

    def __str__(self):
        return f"\n\nQuiz_Title: {self.title} \n\nTotal_Score: {self.total_score} \n\nQuestions: {self.questions} \n\nResponses: {self.responses}"

    def __eq__(self, other):
        return self.title == other.title and self.total_score == other.total_score and self.questions == other.questions
    
    def clone(self):
        """
        Clone the quiz object.
        :return: Quiz object
        """
        return Quiz(self.title, self.questions.copy(), self.responses.copy())

    def add_questions(self, questions=None):
        """
        Add a question or a list of questions to the quiz.
        :param questions: Question or list of questions to be added to the quiz.
        :raises Exception: If the question is not a valid question type.
        :raises Exception: If the question ID already exists in the quiz.
        :return: None
        """        
        try:
            if self.responses:
                raise Exception("Responses Error: Cannot add questions to a quiz with responses")
            if isinstance(questions, list):
                for q in questions:
                    if isinstance(q, question.Question):
                        if q.data["Q_id"] in self.questions:
                            raise Exception(
                                "Duplicate ID Error: Question ID " + str(q.data["Q_id"]) + " already exists")
                        self.questions[q.data["Q_id"]] = q
                        self.total_score += q.data["score"]
                    else:
                        raise Exception("Invalid Type Error:" + str(type(q)) + " is not a valid question type")
            elif isinstance(questions, dict):
                for key, value in questions.items():
                    if isinstance(value, question.Question):
                        if value.data["Q_id"] in self.questions:
                            raise Exception(
                                "Duplicate ID Error: Question ID " + str(value.data["Q_id"]) + " already exists")
                        if value.data["Q_id"] != key:
                            raise Exception("ID Mismatch Error: Question ID " + str(
                                value.data["Q_id"]) + " does not match the key " + str(key))
                        self.questions[value.data["Q_id"]] = value
                        self.total_score += value.data["score"]
                    else:
                        raise Exception("Invalid Type Error:" + str(type(value)) + " is not a valid question type")
            elif isinstance(questions, question.Question):
                self.questions[questions.data["Q_id"]] = questions
                self.total_score += questions.data["score"]
            else:
                raise Exception("Invalid Type Error:" + str(type(questions)) + " is not a valid question type")
        except Exception as e:
            print(e)

    def remove_questions(self, question_ids):
        """
        Remove a question from the quiz.
        :param question_ids: ID of the question to be removed.
        :raises Exception: If the question ID does not exist in the quiz.
        :return: None
        """
        try:
            if self.responses:
                raise Exception("Responses Error: Cannot add questions to a quiz with responses")
            if isinstance(question_ids, list):
                for question_id in question_ids:
                    if question_id in self.questions:
                        del self.questions[question_id]
                    else:
                        raise Exception("ID Error: Question ID " + str(question_id) + " does not exist")
            elif isinstance(question_ids, int):
                if question_ids in self.questions:
                    del self.questions[question_ids]
                else:
                    raise Exception("ID Error: Question ID " + str(question_ids) + " does not exist")
            else:
                raise Exception("Invalid Type Error:" + str(type(question_ids)) + " is not a valid question ID type")
        except Exception as e:
            print(e)

    def add_responses(self, responses = None):
        try:
            if isinstance(responses, Response):
                self.responses[responses.student_id] = responses
            elif isinstance(responses, list):
                for r in responses:
                    if isinstance(r, Response):
                        self.responses[r.student_id] = r
                    else:
                        raise TypeError("Invalid Type Error:" + str(type(r)) + " is not a valid response type")
            elif responses is None:
                while True:
                    student_id = input("Please enter your student ID: ")
                    if student_id in self.responses:
                        print("You have already taken the quiz.")
                        break
                    elif student_id.isnumeric() is False:
                        print("Please enter a valid student ID.")
                    else:
                        self.take_quiz(int(student_id))
                        break
                self.take_quiz(student_id)
            else:
                raise TypeError("Invalid Type Error:" + str(type(responses)) + " is not a valid response type")
        except TypeError as e:
            print(e)

    def take_quiz(self, student_id):
        print(f"Student {student_id}, please answer the following questions:")
        # store the answer list.
        response_list = []
        # access the value that contain the info about each question in the quiz.
        for q in self.questions.values():
            print(q["question"])
            if "notice" in q:
                print(f"note:{q['notice']}")
            if "options" in q:
                print(f"options are {q['options']}")
            answer = input("Your answer: ")
            response_list.append(answer)
        # add the response object to the responses dict.
        self.add_responses(Response(student_id, response_list))

    def export_to_markdown(self):
        """
        Export the quiz to a markdown file.
        :return: None
        """
        with open(self.title + ".md", "w") as file:
            file.write(f"# {self.title}\n")
            for q in self.questions.values():
                file.write(f"""## Q{q.data['Q_id']}. {q.data['question']} <span style="font-size: 14px; opacity: 0.64">({q.data['score']} points)</span>\n""")
                if "notice" in q.data:
                    file.write(f"""\n<span style="font-size: 14px; opacity: 0.32">{q.data['notice']}, Put your answer inside \`\`\`   your_answer    \`\`\`</span>""")
                if "options" in q.data:
                    file.write("""\n<span style="font-size: 14px; opacity: 0.32">Place an `x` in `[ ]` to select your answer.</span>\n""")
                    for option in q.data["options"]:
                        file.write(f"- [ ] {option}\n")
                else:
                    file.write(f"\n```\n\n```\n")
                file.write("\n")
    
    def export_to_html(self):
        """
        Export the quiz to a html file.
        :return: None
        """
        with open(self.title + ".html", "w") as file:
            file.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.title}</title>
</head>

<body>
    <h1>{self.title}</h1>
""")
            for q in self.questions.values():
                file.write(f"""    <h2>Q{q.data['Q_id']}. {q.data['question']} <span style="font-size: 14px; opacity: 0.64">({q.data['score']} points)</span></h2>\n""")
                if "notice" in q.data:
                    file.write(f"""    <span>{q.data['notice']}</span>\n""")
                    file.write(f"""    <br><textarea name="{q.data['Q_id']}" id="{q.data['Q_id']}" cols="30" rows="10"></textarea>\n""")
                if "options" in q.data:
                    for option in q.data["options"]:
                        file.write(f"""    <input type="checkbox" id="{q.data['Q_id']}_{option}" name="{option}"> <label for="{option}">{option}</label><br>\n""")
                else:
                    file.write(f"""    <p><code></code></p>\n""")
                file.write("\n")
            file.write("""</body>
</html>""")
    
    def export_to_pdf(self):
        """
        Export the quiz to a PDF with checkboxes and text areas.
        :param title: The title of the quiz
        :param questions: A dictionary of quiz questions
        :return: None
        """
        # Create a PDF file
        pdf_file = self.title + ".pdf"
        c = canvas.Canvas(pdf_file, pagesize=letter)

        # Title
        c.setFont("Helvetica-Bold", 16)
        c.drawString(100, 750, self.title)

        # Add questions with interactive fields
        c.setFont("Helvetica", 12)
        y = 700
        for q in self.questions.values():
            # Question Text
            c.drawString(50, y, f"Q{q['Q_id']}. {q['question']} ({q['score']} points)")
            y -= 20

            # Add checkbox or text area
            if "options" in q:  # Multiple-choice with checkboxes
                for i, option in enumerate(q["options"]):
                    c.drawString(70, y, option)
                    c.rect(50, y - 3, 10, 10)  # Draw a checkbox
                    y -= 15
            else:  # Text area for open-ended questions
                c.drawString(50, y, "Answer:")
                c.rect(50, y - 40, 400, 40)  # Draw a text area (rectangle)
                y -= 60

            if "notice" in q:
                c.drawString(50, y, f"Note: {q['notice']}")
                y -= 20

            y -= 10  # Space between questions

            # Move to next page if space runs out
            if y < 50:
                c.showPage()
                y = 750

        # Save the PDF
        c.save()
        print(f"PDF saved as {pdf_file}")
        