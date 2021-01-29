from lib.todo_manager import TodoManager
# uncomment to try on the rasp pi
from time import sleep

def main():
    todo_manager = TodoManager()
    print("todo manager instantiated...")
    todo_string = todo_manager.getToDoListString()
    # TODO: send things to remarkable
    print(todo_string)

main()



