from sys import argv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatAction

def start(bot, update):
    update.message.reply_text("Hello!")

def echo(bot, update):
    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)

    print("Possible actions:\n1. /showTasks\n2. /newTask <task to add>\n3. /removeTask <task to remove> 4. /removeAllTasks <substring to use to remove all the tasks that contain it>")

#  repeat_text = update.message.text
#  update.message.reply_text(repeat_text)

def main():
    updater = Updater("579651830:AAFTlYal4Z_v6BGROXO0HRNVXnkDO-dp4CI")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, echo))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

"""

def new_task(tasks_list):
    string = input("Type the new task:\n>")
    tasks_list.append(string)
    print("The new task was successfully added to the list")

def remove_task(tasks_list):
    string = input("Type the entire content of the task you want to delete:\n>")
    if (string in tasks_list):
        tasks_list.remove(string)
        print("The element was successfully deleted")
    else:
        print("The element you specified is not in the list!")

def remove_multiple_tasks(tasks_list):
    remove_list = []
    substring = input("Type the substring you want to use to remove all tasks that contain it:\n>")
    for single_task in tasks_list:
        if (substring in single_task):
            remove_list.append(single_task)
    if (len(remove_list)>0):
        for task_to_remove in remove_list:
            if (task_to_remove in tasks_list):
                tasks_list.remove(task_to_remove)
                print("The element " + task_to_remove + " was successfully removed")
    else:
        print("We did not find any tasks to delete!")

def print_sorted_list(tasks_list):
    if (len(tasks_list) == 0):
        print("The list is empty")
    else:
        print(sorted(tasks_list))

if __name__ == '__main__':
    tasks_list = []
    ended = False
    filename = ""
    if (len(argv)>1):
        filename = argv[1]
        try:
            txt = open(filename)
            tasks_list = txt.read().splitlines()
            txt.close()
        except IOError:
            print("File not found! We will start with an empty list")

    while not ended:
        print("Insert the number corresponding to the action you want to perform")
        print("1: insert a new task")
        print("2: remove a task (by typing all its content)")
        print("3: remove all the existing tasks that contain a provided string")
        print("4: show all existing tasks sorted in alphabetic order")
        print("5: close the program")
        string = input("Your choice:\n>")
        while string.isdigit() != True:
            string = input("Wrong input! Your choice:\n>")
        choice = int(string)
        if (choice == 1):
            new_task(tasks_list)
        elif (choice == 2):
            remove_task(tasks_list)
        elif (choice == 3):
            remove_multiple_tasks(tasks_list)
        elif (choice == 4):
            print_sorted_list(tasks_list)
        elif (choice == 5):
            ended = True
        else:
            print("Not supported: insert a number between 1 and 4\n")

    if (ended and filename != ""):
        try:
            txt = open(filename, "w")
            for single_task in tasks_list:
                txt.write(single_task+"\n")
            txt.close()
        except IOError:
            print("Problems in saving todo list to file")
"""