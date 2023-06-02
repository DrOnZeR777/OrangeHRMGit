import inspect
import logging


class LogGenrator:

    @staticmethod
    def logGen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler(
            "C:\\Practice\\Day33-Reading,Writing,XL file\\OrangeHRM\\Logs\\OrangeHRM_Automation.log")
        format = logging.Formatter(" %(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s")
        logfile.setFormatter(format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger

        # self.log.debug("debug")
        # self.log.info("info")
        # self.log.warning("warning")
        # self.log.error("error")
        # self.log.critical("critical")

        # get log ----> logging.getLogger()
        # logfile ----> path & name
        # format -----> logd format
        # setFormatter --> link file & format
        # Handler ---> maintainence ---> log file
