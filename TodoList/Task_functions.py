from TodoList.TodoList_main import add_task_2, update_task, delete_task,mark_completed,get_task
from databse import ToDoList_db
from TodoList.run import open_todo_list,stop_todo_list,start_Server
from Basic_Utilization.Say import say
import time
# Identify that what user wants to do 

def ToDOmain(query):
    query = query.lower()
    
    if query is None:
        return False
    for i in ToDoList_db.add_task_phrases:
        if i.lower() in query:
            server = start_Server()
    # if query in ToDoList_db.add_task_phrases:
            print("For adding a Task Giving the following details: ")
            say("For adding a Task Giving the following details: ")
            time.sleep(1)
            print("Description: ")
            say("Description: ")
            description = input() 
            print("Due Date: ")
            say("Due Date: ")
            due_date = input()
            print("Priority: ")
            say("Priority: ")
            priority = input()
            add_task_2(description,due_date,priority)
            stop_todo_list(server)
            return True
        
    for i in ToDoList_db.view_tasks_phrases:
        if i.lower() in query:
            server = start_Server()
        # print("Any Specific Task Category or All Tasks: ")
        # say("Any Specific Task Category or All Tasks: ")
        # time.sleep(1)
        # print("All Tasks")
        # say("All Tasks")
            open_todo_list()
            # get_task()
            return True
    
    for i in ToDoList_db.delete_task_phrases:
        if i.lower() in query:
            server = start_Server()
            delete_task()
            stop_todo_list(server)
            return True

    for i in ToDoList_db.complete_task_phrases:
        if i.lower() in query:
            server = start_Server()
            mark_completed()
            stop_todo_list(server)
            return True
            
    for i in ToDoList_db.update_task_phrases:
        if i.lower() in query:
            server = start_Server()
            update_task()
            stop_todo_list(server)
            return True
    
    return False
    
if __name__ == "__main__":
    ToDOmain("add a task")