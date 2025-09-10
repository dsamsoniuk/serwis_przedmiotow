import datetime

class TokenService():
    def isExpired(self, time: int) -> bool:
        now = datetime.datetime.now()
        timestamp = int(now.timestamp())
        if timestamp < time:
            return False
        return True