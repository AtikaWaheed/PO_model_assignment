from ..pages.utility_page import UtilityPage
import csv


class ReadAndWriteCorrectInput(UtilityPage):

    def read_and_enter_correct_answers(self):
        """
        Read each question from csv and put correct inputs
        """
        my_file = 'output.csv'
        with open(my_file, 'r') as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                if row[0].startswith('Q:'):
                    question = row[0].replace('Q: ', '')
                    question_found = False
                    for number in range(2):
                        headings = self.questions_headings()
                        for ind, title in enumerate(headings):
                            if title.text == question:
                                next_answer = next(csv_reader)
                                print next_answer
                                print next_answer[0]
                                self.first_uncheck_all_options(ind)
                                self.correct_input_from_csv(ind, next_answer[0])
                                question_found = True
                                break
                        if question_found:
                            break
                        else:
                            self.click_next_button()
                else:
                    print row[0]
                    self.multiple_inputs_from_csv(row[0])
                    # break
