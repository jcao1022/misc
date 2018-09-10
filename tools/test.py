import logging
import robot
from robot.output.pyloggingconf import RobotHandler

VERBOSE = 0
FORMAT = "[%(asctime)s] - %(name)-20s - %(levelname)s: %(message)s"

FORMAT2 = "[%(asctime)s] - %(name)s: %(message)s"
DATEFMT = "%Y-%m-%d %H:%M:%S"
# to match with RF
TRACE = logging.DEBUG // 2
SESSION_LOG = 15

DEFAULT_LOGGER_CONFIG = dict(
    console=False,
    level="ERROR"
)

class _CFormatter(logging.Formatter):
    DEFAULT_FORMAT = "[%(asctime)s.%(msecs)d] - %(name)-20s - %(levelname)s: %(message)s"
    TESTSUITE_FORMAT = "[%(asctime)s.%(msecs)d] - %(name)-20s - %(levelname)s: .. %(message)s"
    TESTCASE_FORMAT = "[%(asctime)s.%(msecs)d] - %(name)-20s - %(levelname)s: .... %(message)s"
    TESTSTEP_FORMAT = "[%(asctime)s.%(msecs)d] - %(name)-20s - %(levelname)s: ...... %(message)s"
    DEFAULT_LEVEL = 0
    TESTSUITE_LEVEL = 1
    TESTCASE_LEVEL = 2
    TESTSTEP_LEVEL = 3

    def __init__(self, fmt=FORMAT, dfmt=DATEFMT):
        logging.Formatter.__init__(self, fmt, dfmt)
        self.level = 0

    def set_test_level(self, level):
        self.level = level

    def format(self, record):
        format_orig = self._fmt

        # Replace the original format with one customized by logging level
        if self.level == self.DEFAULT_LEVEL:
            self._fmt = self.DEFAULT_FORMAT

        elif self.level == self.TESTSUITE_LEVEL:
            self._fmt = self.TESTSUITE_FORMAT

        elif self.level == self.TESTCASE_LEVEL:
            self._fmt = self.TESTCASE_FORMAT

        elif self.level == self.TESTSTEP_LEVEL:
            self._fmt = self.TESTSTEP_FORMAT


        # Call the original formatter class to do the grunt work
        result = logging.Formatter.format(self, record)
        # Restore the original format configured by the user
        self._fmt = format_orig
        return result

class CFormatter(_CFormatter): pass



def get_log_formatter():
    return CFormatter()


if __name__ == '__main__':
    print("---------------------------------")
    for h in logging.root.handlers:
        print('*********************')
        print(h)
        if isinstance(h, RobotHandler):
            h.setLevel('DEBUG')
            print('log was setted to DEBUG')
    print("---------------------------------")
