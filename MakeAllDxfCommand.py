import adsk.core
import adsk.fusion
import traceback

import os

from os.path import expanduser

from .Fusion360Utilities.Fusion360Utilities import get_app_objects
from .Fusion360Utilities.Fusion360CommandBase import Fusion360CommandBase


class MakeAllPdfCommand(Fusion360CommandBase):

    def on_execute(self, command, inputs, args, input_values):

        # document = get_app_objects()['document']

        # if document.isSaved:
            # document.close(False)

            close_command = get_app_objects()['ui'].commandDefinitions.itemById('cmdID_Make_All_Pdf')
            close_command.execute()