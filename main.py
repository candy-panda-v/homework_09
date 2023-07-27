bot_working = True

contact_dict = {}

def input_error(func):
    def inner(*args, **kwargs):
        consecutive_errors = 0
        while bot_working:
            try:
                return func(*args, **kwargs)
            except UnboundLocalError:
                print('Enter command')
            except TypeError:
                print('Enter name and phone separated by a space!')
            except KeyError:
                print('This name found!')
            except IndexError:
                print('This name found! Enter another name.')
            except Exception as e:
                print('Error:', e)
            consecutive_errors += 1
            if consecutive_errors >= 5: 
                print("Exiting due to consecutive wrong commands.")
                close()
                break
    return inner


def close():
    global bot_working
    bot_working = False
    return ("Good bye!")


def hello():
    return ('How can I help you?')


def add(name, phone):
    contact_dict[name] = phone
    return f"Added contact:  {name}: {phone}"


def change(name, new_phone):
    if name in contact_dict.keys():
        contact_dict[name] = new_phone
        return f"{name} : {new_phone} changed"
    raise IndexError


def phone(name):
    return f"{name} : {contact_dict[name]}"


def showall():
    result = ''
    for name, phone in contact_dict.items():
        result += f"{name} : {phone} \n"
    return result


def helper():
    for key in COMMANDS.keys():
        res += f"{key}\n"
    return "Available bot commands:\n"


def command_parse(input):
    com = input.lower()
    for key in COMMANDS.keys():
        if key in com:
            command = key
    com = com.split(command)
    args = com[1].split(' ')
    args.remove('')
    if args:
        args[0] = args[0].capitalize()
    return command, args


COMMANDS = {'hello': hello,
            'add': add,
            'change': change,
            'phone': phone,
            'show all': showall,
            'good bye': close,
            'exit': close,
            'close': close,
            'help': helper,
            }


def get_handler(func):
    return COMMANDS[func]


@input_error
def main():
    print('How may I help you?')
    while bot_working:
        user_input = input()
        print(get_handler(command_parse(user_input)[0])(*command_parse(user_input)[1]))


if __name__ == '__main__':
    main()
