from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer


db = SQLAlchemy()


class Friend(db.Model):
    __tablename__ = 'friends'

    user_id = Column(Integer, primary_key=True, nullable=False)
    friend_id = Column(Integer, primary_key=True, nullable=False)

    def to_dict(self) -> dict:
        return {
            'user_id': self.user_id,
            'friend_id': self.friend_id
        }

    def __repr__(self):
        return '<Friend(user_id={}, friend_id={})>'.format(self.user_id, self.friend_id)

    @staticmethod
    def get_friend_list(user_id: int) -> list:
        friend_list = db.session.query(Friend) \
            .filter(Friend.user_id == user_id) \
            .all()

        return [x.friend_id for x in friend_list]
