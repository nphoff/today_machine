from lib.todo_manager import TodoManager
# uncomment to try on the rasp pi
from time import sleep
from rmapy.document import ZipDocument
from rmapy.api import Client

import subprocess

def main():
    todo_manager = TodoManager()
    print("todo manager instantiated...")
    todo_string = todo_manager.getToDoListString()
    # TODO: send things to remarkable
    f = open("/tmp/output.md", "w")
    f.write(todo_string)
    f.close()
    r = subprocess.run(['pandoc', '-s', '/tmp/output.md', '-o', '/tmp/output.pdf'], stdout=subprocess.PIPE, universal_newlines=True)
    rm = Client()
    rm.renew_token()
    rawDocument = ZipDocument(doc='/tmp/output.pdf')
    rm.upload(rawDocument)
    print(todo_string)
    print("todo manager done!")

main()



