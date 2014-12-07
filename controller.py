import model
import collect_info
import view

class Controller(object):
    def __init__(self):
        view.welcome()
        self.evaluations()

    def evaluations(self):
        results = model.Evaluation.correct_not_ratios(collect_info.websites)
        view.show_evaluations(results)


here = Controller()