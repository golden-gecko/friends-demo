import pytest

from http import HTTPStatus

from test.base import Base


class TestFriends(Base):
    @pytest.mark.parametrize('user_id, friend_id', [
        (0, 10),
        (10, 0),
        (2147483648, 10),
        (10, 2147483648)
    ])
    def test_adding_friend_with_zero_id(self, user_id, friend_id):
        response = self.friends.add(user_id, friend_id)
        assert response.status_code == HTTPStatus.BAD_REQUEST

    @pytest.mark.parametrize('user_id, friend_id', [
        (-1, 2),
        (2, -1),
        ('AAA', 10),
        (10, 'BBB')
    ])
    def test_adding_friend_with_invalid_id(self, user_id, friend_id):
        """
        Swagger makes negative numbers and string returning 404.
        Returning 400 requeries custom validator or passing ID as string.
        """
        response = self.friends.add(user_id, friend_id)
        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_adding_friends(self):
        response = self.friends.add(10, 20)
        assert response.status_code == HTTPStatus.OK

        response = self.friends.add(10, 30)
        assert response.status_code == HTTPStatus.OK

        response = self.friends.get(10)
        assert response.status_code == HTTPStatus.OK
        assert response.json()['response'] == [20, 30]

    def test_adding_friend_to_yourself(self):
        response = self.friends.add(15, 15)
        assert response.status_code == HTTPStatus.BAD_REQUEST

    def test_adding_friend_twice(self):
        response = self.friends.add(30, 60)
        assert response.status_code == HTTPStatus.OK

        response = self.friends.add(30, 60)
        assert response.status_code == HTTPStatus.CONFLICT

    def test_adding_friend_makes_mutual_relationship(self):
        response = self.friends.add(500, 600)
        assert response.status_code == HTTPStatus.OK

        response = self.friends.get(500)
        assert response.status_code == HTTPStatus.OK
        assert response.json()['response'] == [600]

        response = self.friends.get(600)
        assert response.status_code == HTTPStatus.OK
        assert response.json()['response'] == [500]

    def test_adding_friend_mutually_causes_error(self):
        response = self.friends.add(2, 4)
        assert response.status_code == HTTPStatus.OK

        response = self.friends.add(4, 2)
        assert response.status_code == HTTPStatus.CONFLICT

    @pytest.mark.parametrize('user_id, friend_id', [
        (0, 10),
        (10, 0),
        (2147483648, 10),
        (10, 2147483648)
    ])
    def test_removing_friend_with_zero_id(self, user_id, friend_id):
        response = self.friends.remove(user_id, friend_id)
        assert response.status_code == HTTPStatus.BAD_REQUEST

    @pytest.mark.parametrize('user_id, friend_id', [
        (-1, 2),
        (2, -1),
        ('AAA', 10),
        (10, 'BBB')
    ])
    def test_removing_friend_with_invalid_id(self, user_id, friend_id):
        """
        Swagger makes negative numbers and string returning 404.
        Returning 400 requeries custom validator or passing ID as string.
        """
        response = self.friends.remove(user_id, friend_id)
        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_removing_non_existent_friend(self):
        response = self.friends.remove(10, 20)
        assert response.status_code == HTTPStatus.OK

    def test_removing_friend(self):
        response = self.friends.add(10, 20)
        assert response.status_code == HTTPStatus.OK

        response = self.friends.add(10, 30)
        assert response.status_code == HTTPStatus.OK

        response = self.friends.remove(10, 20)
        assert response.status_code == HTTPStatus.OK

        response = self.friends.get(10)
        assert response.status_code == HTTPStatus.OK
        assert response.json()['response'] == [30]
