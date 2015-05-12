import os

import win32com.client

from .. import hecrasgeometry
from ..runtime import Runtime


ras_version = os.environ['RAS_CONTROLLER_VERSION']
ras = __import__(ras_version.lower(), globals(), locals(), [], -1)


class HECRASController(ras.Controller, ras.ControllerDeprecated):
    """HEC-RAS Controller.

    project_file : str
        TODO:
    
    """

    def __init__(self, filename=None):
        super(HECRASController, self).__init__()
        self._rc = win32com.client.DispatchEx(
            "{0}.HECRASController".format(ras_version))
#            self._rc = win32com.client.DispatchWithEvents(
#                "{0}.HECRASController".format(ras_version), ras.RASEvents)
        self._events = win32com.client.WithEvents(self._rc, ras.RASEvents)
        self._ras_version = ras_version
        self._error = 'Not available in version "{}" of controller'.format(
            self._ras_version)

        self._filename = filename

        self._geometry = hecrasgeometry.HECRASGeometry(ras_version)
        self._runtime = Runtime(self)

        if filename:
            self.Project_Open(filename)

    def __enter__(self):
        """ """
        self.ShowRas()
        return self

    def __exit__(self, type, value, traceback):
        """ """
        self.close()

    def pause(self, time):
        """ """
        self._runtime.pause(time)

    def runtime(self):
        """ """
        return self._runtime

    def close(self):
        self._runtime.close()
