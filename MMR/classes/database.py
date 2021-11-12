import mysql.connector
from mysql.connector import Error
from mysql.connector.cursor import MySQLCursor
from datetime import datetime

class Database(object):
    """
    Database class for MYSQL handling.
    """
    def __init__(self, host: str, database: str, user: str, password: str) -> None:
        self.initialize_connection(host, database, user, password)

    def initialize_connection(self, db_host: str, db: str, db_user: str, db_user_password: str) -> None:
        """
        Initialize a connection with MySQL server.
        """
        try:
            self.connection = mysql.connector.connect(host = db_host, 
                                                       database = db,
                                                       user = db_user,
                                                       password = db_user_password)
        except Error as error_type:
            print("Error while connecting to MySQL ", error_type)

    def create_cursor(self) -> MySQLCursor:
        """
        Returns a cursor class object for database handling.
        """
        return self.connection.cursor()

        
    def insert_alarm(self, user_id: int, time: str, row_reference: int) -> None:
        """
        Insert alarm into database for given house ID at given time and a reference
        for the row that raised the alarm.

        params:
        user_id - user id of entry
        time - time of alarm
        row_reference - reference to row ID that caused alarm
        """
        cursor = self.create_cursor()
        add_alarm = (
            "INSERT INTO alarms "
            "(user_id, time, reference) "    
            "VALUES (%s, %s, %s)"
        )
        alarm_data = (str(user_id), time, str(row_reference))

        cursor.execute(add_alarm, alarm_data)
        self.connection.commit()
        cursor.close()

    def get_val(self, user_id: int, type = "DESC", desired = "last_val") -> float:
        """
        Get desired value from entrys table in database by certain order type.

        Params:

        user_id - user id of entry
        type - type of return values ordering
        desired - type of desired return value
        """
        cursor = self.create_cursor()

        query_for_last = (
            "SELECT value, time FROM entrys "
            "WHERE user_id = " + str(user_id) + " "
            "ORDER BY time " + type + " "
            "LIMIT 1"
        )

        cursor.execute(query_for_last)
        return_value = None

        for (value, date) in cursor:
            if desired == "last_val":
                return_value = float(value)
            else:
                return_value = date

        if not return_value:
            return_value = -1
        
        cursor.close()
        
        return return_value

    def insert_entry(self, user_id: int, time: str, value: float) -> None:
        """
        Insert entry value into database for given house ID at given time.

        Params:
        user_id - user id of entry to insert
        value - value to insert
        time - time of measuring
        """

        last_val = self.get_val(user_id)
        if last_val < 0:
            last_val = value

        cursor = self.create_cursor()
        delta = value - last_val
        add_entry = (
            "INSERT INTO entrys "
            "(user_id, time, value, delta) "
            "VALUES (%s, %s, %s, %s)"
        )
        entry_data = (str(user_id), time, str(value), str(delta))

        cursor.execute(add_entry, entry_data)
        self.connection.commit()
        cursor.close()
        if delta < 0:
            return -3
        return 1
        
    def fetch_entry_values(self, user_id: int, start_time: datetime) -> list:
        """
        Returns a sorted list of values and the time the value was taken for a given ID
        starting from a given time.

        Params:
        user_id - user id of entry
        start_time - time_frame from wich to get entries
        """
        cursor = self.create_cursor()

        query = (
            "SELECT value, time FROM entrys "
            "WHERE user_id = %s AND %s <= time"
        )

        query_data = (str(user_id), start_time)

        cursor.execute(query, query_data)
        
        return_list = []

        for (value, time) in cursor:
            return_list.append((float(value), time))
        
        cursor.close()
        
        return_list = sorted(return_list, key = lambda x: x[1])

        return return_list

    def get_reference(self, user_id: int) -> int:
        """
        Get reference ID of last entry to database of given user_id

        Params:
        user_id - user ID of alarm raiser
        """
        cursor = self.create_cursor()

        query = (
            "SELECT id FROM entrys "
            "WHERE user_id = " + str(user_id) + " "
            "ORDER BY id DESC "
            "LIMIT 1"
        )

        cursor.execute(query)

        for (id) in cursor:
            return_id = int(id[0])

        return return_id