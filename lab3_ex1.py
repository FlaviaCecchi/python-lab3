from sys import argv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def new_task(bot, update, args):
    taskToAdd = ' '.join(args)
    if taskToAdd and taskToAdd.strip() and (not taskToAdd.isspace()):
        tasks_list.append(taskToAdd)
        message = "The new task was successfully added to the list!"
    else:
        message = "You did not specify any task!"
    bot.sendMessage(chat_id=update.message.chat_id, text=message)
    saveListToFile()

def remove_task(bot, update, args):
    taskToRemove = ' '.join(args)
    message = ''
    if taskToRemove and taskToRemove.strip() and (not taskToRemove.isspace()):
        if (taskToRemove in tasks_list):
            tasks_list.remove(taskToRemove)
            message = "The task was successfully deleted!"
        else:
            message = "The task you specified is not in the list!"
    else:
        message = "You did not specify any task!"
    bot.sendMessage(chat_id=update.message.chat_id, text=message)
    saveListToFile()

def remove_multiple_tasks(bot, update, args):
    remove_list = []
    removed_elements = []
    substring = ' '.join(args)
    message = ''
    if substring and substring.strip() and (not substring.isspace()):
        for single_task in tasks_list:
            if (substring in single_task):
                remove_list.append(single_task)
        if (len(remove_list)>0):
            for task_to_remove in remove_list:
                if (task_to_remove in tasks_list):
                    tasks_list.remove(task_to_remove)
                    removed_elements.append(task_to_remove)
            message = "The elements "+ ' , '.join(removed_elements)+" were successfully removed!"
        else:
            message = "I did not find any task to delete!"
    else:
        message = "You did not specify any string!"
    bot.sendMessage(chat_id=update.message.chat_id, text=message)
    saveListToFile()

def print_sorted_list(bot, update):
    message = ''
    if (len(tasks_list) == 0):
        message="Nothing to do, here!"
    else:
        message = sorted(tasks_list)
    bot.sendMessage(chat_id=update.message.chat_id, text=message)

def start(bot, update):
    update.message.reply_text('Hello! This is AmITaskListBot. You can use one of the following commands:')
    update.message.reply_text('/newTask <task to add>')
    update.message.reply_text('/removeTask <task to remove>')
    update.message.reply_text('/removeAllTasks <substring used to remove all the tasks that contain it>')
    update.message.reply_text('/showTasks')

def echo(bot, update):
    receivedText = update.message.text
    textToSend = "I'm sorry, I can't do that"
    bot.sendMessage(chat_id=update.message.chat_id, text=textToSend)

def saveListToFile():
    filename = "task_list.txt"
    try:
        txt = open(filename, "w")
        for single_task in tasks_list:
            txt.write(single_task + "\n")
        txt.close()
    except IOError:
        print("Problems in saving todo list to file")

if __name__ == '__main__':
    tasks_list = []
    filename = "task_list.txt"
    try:
        txt = open(filename)
        tasks_list = txt.read().splitlines()
        txt.close()
    except IOError:
        print("File not found!")
        exit()
    updater = Updater(token='579651830:AAFTlYal4Z_v6BGROXO0HRNVXnkDO-dp4CI')
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    newTask_handler = CommandHandler('newTask', new_task, pass_args=True)
    dispatcher.add_handler(newTask_handler)
    removeTask_handler = CommandHandler('removeTask', remove_task, pass_args=True)
    dispatcher.add_handler(removeTask_handler)
    removeAllTasks_handler = CommandHandler('removeAllTasks', remove_multiple_tasks, pass_args=True)
    dispatcher.add_handler(removeAllTasks_handler)
    showTasks_handler = CommandHandler('showTasks', print_sorted_list)
    dispatcher.add_handler(showTasks_handler)
    updater.start_polling()
    updater.idle()