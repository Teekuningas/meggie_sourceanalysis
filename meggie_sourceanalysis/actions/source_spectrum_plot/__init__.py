"""Contains implementation for source spectrum plot"""

import logging

import numpy as np

from meggie.utilities.messaging import exc_messagebox

from meggie.mainwindow.dynamic import Action


class PlotSpectrum(Action):
    """ """

    def run(self):

        try:
            selected_name = self.data["outputs"]["source_spectrum"][0]
        except IndexError:
            return

        subject = self.experiment.active_subject
        try:
            self.handler(subject, {"name": selected_name})
        except Exception as exc:
            exc_messagebox(self.window, exc)

    def handler(self, subject, params):
        meggie_spectrum = subject.source_spectrum.get(params["name"])
        stcs = meggie_spectrum.content

        subjects_dir = meggie_spectrum.params["subjects_dir"]

        for key, stc in stcs.items():
            logging.getLogger("ui_logger").info("Plotting " + str(key))

            # scale to avoid overflows
            stc_copy = stc.copy()
            stc_copy.data = stc_copy.data / np.max(np.abs(stc_copy.data))

            stc_copy.plot(
                time_label=("%0.2f Hz"), hemi="both", subjects_dir=subjects_dir
            )
