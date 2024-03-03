def get_name(message):
    user = message.from_user.first_name
    return user

def get_id(message):
    id = message.from_user.id
    return id
