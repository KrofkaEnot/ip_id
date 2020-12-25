

def in_terminal_print(message):
    print(
        f"ID: {message['from']['id']} FirstName: {message['from']['first_name']} UserName: {message['from']['username']} "
        f"languageCode: {message['from']['language_code']} TEXT: {message['text']}")


