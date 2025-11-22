def validate_user_id(user_id: int) -> bool:
    try:
        int(user_id)
    except ValueError:
        return False
    else:
        return 0 < user_id < 2147483647
