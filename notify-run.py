import os
import time
import requests

# Change here
link = ""

# Clear command supported for every OS
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')


# Spam
def flood():
    a = input("What text do you want to flood?\n>>> ")
    clear()
    b = input("How much messages do you want?\n>>> ")
    clear()
    time.sleep(1)
    print(f"Flood started! ([{a}], {b} times.)")
    i = 1
    while i < int(b) + 1:
        requests.post(link, data=a.encode("utf-8"))
        i += 1
    print("Flood been successful!")
    time.sleep(3)
    choice()


# Send a single message
def send():
    a = input("What text do u want to send?\n>>> ")
    requests.post(link, data=a.encode("utf-8"))
    clear()
    print("Done!")
    time.sleep(2)
    clear()
    repeating()


def repeating():
    aa = input("Do you want to repeat? Y/N\n>>> ")
    if aa == "Y":
        clear()
        send()
    if aa == "y":
        clear()
        send()
    if aa == "N":
        clear()
        choice()
    if aa == "n":
        clear()
        choice()
    else:
        choice()


def AIO():
    clear()
    a = input("Start reading from the .txt file? Y/N\n>>> ")
    if a == "Y":
        AIO_Process()
    if a == "y":
        AIO_Process()
    if a == "N":
        clear()
        choice()
    if a == "n":
        clear()
        choice()
    else:
        choice()


def AIO_Process():
    filename = "AIOtext.txt"
    print("Starting AIO method...")
    time.sleep(2)
    with open(filename, 'r') as f:
        for line in f:
            requests.post(link, data=line.encode("utf-8"))
    print("AIO Method been successful!")
    time.sleep(2)
    choice()


# User interface
def choice():
    clear()
    if link == "":
        print("Unable to get Notify-run link, please change it inside the script.")
        time.sleep(5)
        exit()
    else:
        print("Created by: Splexas")
        a = input("What tool do you want to use? Enter a number\n"
                  "1. Single message - sends a single notification, can be repeatable\n"
                  "2. Flood - floods notifications\n"
                  "3. AIO Method - reads every line from the .txt file, and sends them as notifications.\n"
                  "4. Quit the script\n"
                  ">>> ")
        if a == "1":
            clear()
            send()
        if a == "2":
            clear()
            flood()
        if a == "3":
            clear()
            AIO()
        if a == "4":
            clear()
            exit()
        print("Unknown tool!")
        time.sleep(2)
        clear()
        choice()


choice()
