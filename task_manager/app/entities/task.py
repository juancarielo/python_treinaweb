class Task():
    def __init__(self, title, description, date_expiration, priority):
        self.__title = title
        self.__description = description
        self.__date_expiration = date_expiration
        self.__priority = priority

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def date_expiration(self):
        return self.__date_expiration

    @date_expiration.setter
    def date_expiration(self, date_expiration):
        self.__date_expiration = date_expiration

    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority):
        self.__priority = priority