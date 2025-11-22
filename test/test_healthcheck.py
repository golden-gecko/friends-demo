from http import HTTPStatus

from test.base import Base


class TestHealthcheck(Base):
    def test_healthcheck(self):
        assert self.friends.is_alive().status_code == HTTPStatus.OK
