from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

if __name__ == '__main__':

    question_bank = []
    play_game = input("Play or Exit: ")
    if play_game == "Exit":
        print("WORKS")
    else:
        print("FAILURE")

    # # Creates a new question bank from data stored in Data
    # for question in question_data:
    #     question_text = question["question"]
    #     question_answer = question["correct_answer"]
    #     new_question = Question(question_text, question_answer)
    #     question_bank.append(new_question)
    #
    # quiz_game = QuizBrain(question_bank)
    # print(question_bank[0].question)
    # print(question_bank[0].answer)
    #
    # while quiz_game.still_has_questions():
    #     quiz_game.next_question()
    #
    # print("------------------------------------------------------------------------------")
    # print("You've completed the quiz!")
    # print(f"You final score was {quiz_game.score} out of {len(question_bank)} questions.")
    # print("------------------------------------------------------------------------------")
