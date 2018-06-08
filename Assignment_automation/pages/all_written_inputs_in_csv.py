from ..pages.utility_page import UtilityPage


class CorrectWrittenInputsInCsv(UtilityPage):

    def write_all_correct_inputs_in_csv(self):
        """
        writing correct answers in output csv from final result page
        """
        my_file = open("output.csv", "w")
        for number in range(1, 4):
            for index in range(2):
                title = self.grading_question_list(number, index)
                answer_list = self.correct_answers(number, index)
                if len(answer_list):
                    my_file.write('Q: ' + str(title) + "\n")
                    for item in answer_list:
                        my_file.write(str(item.text) + "\n")
