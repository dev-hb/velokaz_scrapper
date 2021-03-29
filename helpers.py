import os


class Helpers:

    def __init__(self, filename):
        self.filename = filename

    # read a file content
    def readFile(self):
        content = ""
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), self.filename)) as f:
            for line in f.readlines():
                content += line
        return content

    # debug a result to log file
    def debug(self, data, ext="html"):
        f = open("log."+ext, "w")
        f.write(str(data))
        f.close()
