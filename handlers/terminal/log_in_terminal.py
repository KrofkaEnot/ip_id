def in_terminal_logging(message):
    return (f"ID: {message['from']['id']}\n"
            f"FirstName: {message['from']['first_name']}\n"
            f"UserName: {message['from']['username']}\n"
            f"languageCode: {message['from']['language_code']}\n"
            f"TEXT: {message['text']}\n"
            f"----------------")


def in_terminal_logging_inline(call):
    return (f'ID: {call.from_user.id}, IsBot: {call.from_user.is_bot}\n'
            f'Last_Name: {call.from_user.last_name}, First_Name: {call.from_user.first_name}\n'
            f'Username: {call.from_user.username}, Lang: {call.from_user.language_code}\n'
            f'----------------')
