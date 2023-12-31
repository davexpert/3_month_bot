import sqlite3
from database import sql_queries


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("db.sqlite3")
        self.cursor = self.connection.cursor()


    def sql_create_tables(self):
        if self.connection:
            print("Database connected successfully")

        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_BAN_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_PROFILE_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_LIKE_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_DISLIKE_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_REFERRAL_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_REFERENCE_USERS_TABLE_QUERY)
        try:
            self.connection.execute(sql_queries.ALTER_USER_TABLE)
            self.connection.execute(sql_queries.ALTER_USER_V2_TABLE)
        except sqlite3.OperationalError:
            pass
        self.connection.commit()


    def sql_insert_user(self, tg_id, username, first_name, last_name):
        self.cursor.execute(
            sql_queries.INSERT_USER_QUERY,
            (None, tg_id, username, first_name, last_name, None, 0,)
        )
        self.connection.commit()

    def sql_insert_new_ban_user(self, tg_id):
        self.cursor.execute(
            sql_queries.INSERT_NEW_BAN_USER_QUERY,
            (None, tg_id, 1)
        )
        self.connection.commit()

    def sql_select_ban_user(self, tg_id):
        self.cursor.row_factory = lambda cursor, row:{
            "id": row[0],
            "telegram_id": row[1],
            "ban_count": row[2]
        }
        return self.cursor.execute(
            sql_queries.SELECT_BAN_USER_QUERY,
            (tg_id,)
        ).fetchone()

    def sql_update_ban_user_count(self, tg_id):
        self.cursor.execute(
            sql_queries.UPDATE_BAN_USER_COUNT_QUERY,
            (tg_id,)
        )
        self.connection.commit()

    def sql_insert_profile(self, tg_id, nickname, bio, age, gender, race, city, photo):
        self.cursor.execute(
            sql_queries.INSERT_PROFILE_QUERY,
            (None, tg_id, nickname, bio, age, gender, race, city, photo)
        )
        self.connection.commit()

    def sql_user_registered(self, tg_id):
        return self.cursor.execute(
            sql_queries.SELECT_REGISTERED_PROFILE_QUERY,
            (tg_id,)
        ).fetchone()

    def sql_select_profile(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "bio": row[3],
            "age": row[4],
            "gender": row[5],
            "race": row[6],
            "city": row[7],
            "photo": row[8]
        }
        return self.cursor.execute(
            sql_queries.SELECT_PROFILE_QUERY,
            (tg_id,)
        ).fetchone()

    def sql_select_filter_profiles(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "bio": row[3],
            "age": row[4],
            "gender": row[5],
            "race": row[6],
            "city": row[7],
            "photo": row[8]
        }
        return self.cursor.execute(
            sql_queries.FILTER_LEFT_JOIN_PROFILE_LIKE_QUERY,
            (tg_id, tg_id,)
        ).fetchall()

    def sql_select_dis_filter_profiles(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "bio": row[3],
            "age": row[4],
            "gender": row[5],
            "race": row[6],
            "city": row[7],
            "photo": row[8]
        }
        return self.cursor.execute(
            sql_queries.FILTER_LEFT_JOIN_PROFILE_DISLIKE_QUERY,
            (tg_id, tg_id,)
        ).fetchall()


    def sql_insert_like(self, owner, liker):
        self.cursor.execute(
            sql_queries.INSERT_LIKE_QUERY,
            (None, owner, liker,)
        )
        self.connection.commit()
    def sql_insert_dislike(self, owner, disliker):
        self.cursor.execute(
            sql_queries.INSERT_DISLIKE_QUERY,
            (None, owner, disliker,)
        )
        self.connection.commit()

    def sql_update_profile(self, nickname, bio, age, gender, race, city, photo, tg_id):
        self.cursor.execute(
            sql_queries.UPDATE_PROFILE_QUERY,
            (nickname, bio, age, gender, race, city, photo, tg_id,)
        )
        self.connection.commit()

    def sql_delete_profile(self, tg_id):
        self.cursor.execute(
            sql_queries.DELETE_PROFILE_QUERY,
            (tg_id,)
        )
        self.connection.commit()

    def sql_update_user_link(self, link, tg_id):
        self.cursor.execute(
            sql_queries.UPDATE_USER_LINK_QUERY,
            (link, tg_id,)
        )
        self.connection.commit()

    def sql_select_user(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "username": row[2],
            "first_name": row[3],
            "last_time": row[4],
            "link": row[5],
            "balance": row[6],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_QUERY,
            (tg_id,)
        ).fetchone()

    def sql_reference_menu_data(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "balance": row[0],
            "total_referral": row[1],
        }
        return self.cursor.execute(
            sql_queries.DOUBLE_SELECT_REFERRAL_USER_QUERY,
            (tg_id,)
        ).fetchone()

    def sql_reference_user_data(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "total_referral": row[0],
        }
        return self.cursor.execute(
            sql_queries.SELECT_REFERENCE_USER_QUERY,
            (tg_id,)
        ).fetchone()

    def sql_select_user_by_link(self, link):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "username": row[2],
            "first_name": row[3],
            "last_time": row[4],
            "link": row[5],
            "balance": row[6],
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_BY_LINK_QUERY,
            (link,)
        ).fetchone()

    def sql_insert_referral(self, owner, referral):
        self.cursor.execute(
            sql_queries.INSERT_REFERRAL_QUERY,
            (None, owner, referral)
        )
        self.connection.commit()

    def sql_insert_reference_user(self, reference_user):
        self.cursor.execute(
            sql_queries.INSERT_REFERENCE_USER_QUERY,
            (None, reference_user,)
        )
        self.connection.commit()

    def sql_update_balance(self, owner):
        self.cursor.execute(
            sql_queries.UPDATE_USER_BALANCE_QUERY,
            (None, owner,)
        )
        self.connection.commit()