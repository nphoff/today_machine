import requests
import json
from lib import secrets
from lib import sample
from datetime import date

# for Sync api
from todoist.api import TodoistAPI

# alternative approach
# leaving here for now in case i need this...

def main():
    useRestAPI()

    # Not totally sure which technique i need for this
    # so going to leave this here for posterity if i need this
    #useSyncLibrary()

def useRestAPI():
    today_and_overdue = getRequestData()
    (today_tasks, overdue_tasks) = getTodayAndOverdue(today_and_overdue)
    printTasks(today_tasks, overdue_tasks)


def getRequestData():
    return requests.get(
        "https://api.todoist.com/rest/v1/tasks",
        params={
            "filter":  getFilterString()
        },
        headers={
            "Authorization": getHeaderString()
        }
    ).json()


def getFilterString():
    today_date = date.today().isoformat()
    return "(due: %s | overdue)" % today_date

def getHeaderString():
    return "Bearer %s" % secrets.API_TOKEN


def printTasks(today, overdue):

    print("☆ﾟ.*･｡ﾟ☆ﾟ.*･｡ﾟ☆ﾟ.*･｡ﾟ☆ﾟ.*･｡ﾟ☆ﾟ.*･｡ﾟ☆ﾟ.*･｡ﾟ")
    print("       Good morning goldsam!")
    print("☆ﾟ.*･｡ﾟ☆ﾟ.*･｡ﾟ☆ﾟ.*･｡ﾟ☆ﾟ.*･｡ﾟ☆ﾟ.*･｡ﾟ☆ﾟ.*･｡ﾟ")
    print("\n")
    print("Here are today's tasks:")
    for task in today:
        print("□ %s" % task['content'])
    print("\nHere are your overdue tasks:")
    for task in overdue:
        print("□ %s" % task['content'])
    
    print("\n\n\n")


def getTodayAndOverdue(all_tasks):
    today = []
    overdue = []
    today_date = date.today().isoformat()

    for task in all_tasks:
        due_date = task['due']['date']
        if (due_date == today_date):
            today.append(task)
        else:
            overdue.append(task)

    return (today, overdue)

def useSyncLibrary():
    api = TodoistAPI(secrets.API_TOKEN)
    api.sync()
    #print(api.state['projects'])
    print("\n\n\n")
    items = api.state["items"]
    print(json.dumps(items))

    # get all completed
    all_comp = api.completed.get_all()

    for item in items:
        if item['checked'] > 0:
            print(item['content'])

main()



