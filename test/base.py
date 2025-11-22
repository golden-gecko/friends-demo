import os
import psycopg2

from test.friends import Friends


class Base:
    def setup_method(self, method):
        self.friends = Friends(os.environ.get('FRIENDS_URL'), os.environ.get('FRIENDS_VERSION'))

        params = 'dbname={} user={} host={} password={}'.format(
            os.environ.get('POSTGRES_DATABASE_NAME'),
            os.environ.get('POSTGRES_USER'),
            os.environ.get('POSTGRES_HOST'),
            os.environ.get('POSTGRES_PASSWORD')
        )

        with psycopg2.connect(params) as connection:
            with connection.cursor() as cursor:
                cursor.execute('DELETE FROM friends')
