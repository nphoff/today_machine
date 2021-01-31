from lib.todo_manager import TodoManager
# uncomment to try on the rasp pi
from rmapy.document import ZipDocument
from rmapy.api import Client

from datetime import date

import subprocess


MARKDOWN_PATH = '/tmp/today.md'

def main():
    todo_manager = TodoManager()
    today = date.today()
    pdf_path = '/tmp/Today-{}.pdf'.format(today.strftime("%b-%d-%Y"))
    todo_string = todo_manager.getToDoListString()
    f = open(MARKDOWN_PATH, "w")
    f.write(todo_string)
    f.close()
    r = subprocess.run(['pandoc', '-s', MARKDOWN_PATH, '-o', pdf_path], stdout=subprocess.PIPE, universal_newlines=True)
    rm = Client()
    rm.renew_token()
    rawDocument = ZipDocument(doc=pdf_path)
    rm.upload(rawDocument)
    print(todo_string)

main()

