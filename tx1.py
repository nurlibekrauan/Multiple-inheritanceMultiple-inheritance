from abc import ABC, abstractmethod


class AccesControl(ABC):
    @abstractmethod
    def can_read(self):
        """Returns True if access rights are available"""
        pass

    @abstractmethod
    def can_write(self):
        """Returns True if write access rights are available"""
        pass

    @abstractmethod
    def can_delete(self):
        """Returns True if delete access rights are available"""
        pass
    def log_message(self,message):
        print(f"{message}")
    def log_error(self, error):
        print(f"Error: {error}")
    def log_warning(self, warning):
        print(f"Warning: {warning}")
    def log_info(self, info):
        print(f"Info: {info}")
        
    


class AdminAccess(AccesControl):
    def can_read(self):
        return True

    def can_write(self):
        return True

    def can_delete(self):
        return True


class ModeratorAccess(AccesControl):
    def can_read(self):
        return True

    def can_write(self):
        return False

    def can_delete(self):
        return True


class UserAccess(AccesControl):
    def can_read(self):
        return True

    def can_write(self):
        return False

    def can_delete(self):
        return False

class Initializator:
    def __init__(self, name):
        self.name = name
class Admin(Initializator,AdminAccess):
    'you can override some methods or create new ones'
    pass
class Moderator(Initializator,ModeratorAccess):
    pass
class User(Initializator,UserAccess):
    pass
class AdminModerator(Initializator,AdminAccess,ModeratorAccess):
    pass
class AdminUser(Initializator,AdminAccess,ModeratorAccess):
    pass
class ModeratorUser(Initializator,ModeratorAccess,UserAccess):
    pass

# Создание экземпляров пользователей с разными уровнями доступа
admin = Admin(name="Alice")
moderator = Moderator(name="Bob")
user = User(name="Charlie")
admin_moderator = AdminModerator(name="David")  # Комбинированная роль

# Проверка прав доступа
print(admin.can_read())     # True, т.к. админ может читать
print(admin.can_write())    # True, т.к. админ может писать
print(admin.can_delete())   # True, т.к. админ может удалять

print(moderator.can_read())     # True, т.к. модератор может читать
print(moderator.can_write())    # False, модератор не может писать
print(moderator.can_delete())   # True, модератор может удалять контент

print(user.can_read())     # True, пользователь может читать
print(user.can_write())    # False, у пользователя нет прав на запись
print(user.can_delete())   # False, у пользователя нет прав на удаление

# Комбинированные роли
print(admin_moderator.can_read())     # True, т.к. обе роли могут читать
print(admin_moderator.can_write())    # True, админ может писать
print(admin_moderator.can_delete())   # True, админ имеет права на удаление (приоритет админа)
