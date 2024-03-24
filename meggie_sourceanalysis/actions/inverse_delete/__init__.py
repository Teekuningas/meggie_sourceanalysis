""" Contains implementation for delete inverse
"""

from meggie.utilities.messaging import exc_messagebox

from meggie.mainwindow.dynamic import Action
from meggie.mainwindow.dynamic import subject_action


class DeleteInverse(Action):
    """Deletes inverse items"""

    def run(self):

        subject = self.experiment.active_subject

        try:
            selected_name = self.data["outputs"]["inverse"][0]
        except IndexError:
            return

        try:
            self.handler(subject, {"name": selected_name})
            self.experiment.save_experiment_settings()
        except Exception as exc:
            exc_messagebox(self.window, exc)
            return

        self.window.initialize_ui()

    @subject_action
    def handler(self, subject, params):
        subject.remove(params["name"], "inverse")
