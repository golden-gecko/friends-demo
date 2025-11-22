from sqlalchemy import and_

from handlers import bad_request, conflict, success
from models import db, Friend
from validate import validate_user_id


def create(user_id: int, friend_id: int) -> tuple:
    if not validate_user_id(user_id) or not validate_user_id(friend_id):
        return bad_request(message='User ID is not valid')

    if user_id == friend_id:
        return bad_request(message='Cannot make friend relationship with yourself')

    is_friend = db.session.query(Friend) \
        .filter(and_(Friend.user_id == user_id, Friend.friend_id == friend_id)) \
        .first()

    if is_friend:
        return conflict(message='Friend relationship already exists')

    # add two rows to make friends list retrieval easier
    db.session.add(Friend(user_id=user_id, friend_id=friend_id))
    db.session.add(Friend(user_id=friend_id, friend_id=user_id))
    db.session.commit()

    return success(message='Friend relationship was created', data=Friend.get_friend_list(user_id))


def get(user_id: int) -> tuple:
    if not validate_user_id(user_id):
        return bad_request(message='User ID is not valid')

    return success(data=Friend.get_friend_list(user_id))


def remove(user_id: int, friend_id: int) -> tuple:
    if not validate_user_id(user_id) or not validate_user_id(friend_id):
        return bad_request(message='User ID is not valid')

    db.session.query(Friend).filter(and_(Friend.user_id == user_id, Friend.friend_id == friend_id)).delete()
    db.session.query(Friend).filter(and_(Friend.user_id == friend_id, Friend.friend_id == user_id)).delete()
    db.session.commit()

    return success(message='Friend relationship was deleted')
