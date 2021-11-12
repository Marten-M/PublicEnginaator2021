from classes.azur import AzurClient
from classes.database import Database
import datetime

class RequestHandler(object):
    """
    Class to handle post requests.
    """

    def __init__(self, azur_client: AzurClient, database: Database) -> None:
        self.client = azur_client
        self.database = database

    def handle_request(self, request: str) -> int:
        """
        Handle post requests.

        Params:
        
        request - post request made by client
        """

        user_id = int(request.args["user_id"])
        date = datetime.datetime(*list(map(int, request.args["date"].split("."))))
        value = self.client.read_number(request.data)
        
        if value < 0:
            return value

        entry = self.database.insert_entry(user_id, date, value)

        if entry < 0:
            return -3 * user_id

        if self.raise_alarm(user_id, date):
            ref = self.database.get_reference(user_id)
            self.database.insert_alarm(user_id, date, ref)
        
        return 1
    

    def raise_alarm(self, user_id: int, date: datetime.datetime) -> bool:
        """
        Check whether value has constantly increased over the last 24 hours.

        Params:
        user_id - id of user to check values for
        date - current date
        """
        last_day = date - datetime.timedelta(days = 1)

        if self.database.get_val(user_id, "ASC", "date") > last_day:
            return False
        
        lst = self.database.fetch_entry_values(user_id, last_day)

        last_val = lst[0][0]

        for value, time in lst[1:]:
            if value > last_val:
                last_val = value
                continue
            return False
        return True


    