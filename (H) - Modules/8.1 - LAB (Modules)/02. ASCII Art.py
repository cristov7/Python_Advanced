from pyfiglet import figlet_format


def print_art(message):
    message_art = figlet_format(message)
    print(message_art)


text = input()
print_art(text)


# import pyfiglet
# text = pyfiglet.figlet_format(input())
# print(text)
