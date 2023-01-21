from api.user.schemas import UserOut


class Helper:
    def __init__(self):
        self.users_db: dict[int, UserOut] = {}
        self.current_id = 0

    @property
    def next_id(self) -> int:
        self.current_id += 1
        return self.current_id