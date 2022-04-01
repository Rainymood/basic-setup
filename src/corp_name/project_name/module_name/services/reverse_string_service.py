
class ReverseStringService:
    """This is an example of a service. We call this the ReverseStringService
    because it reverses a string. But this can of course be anything. We call it
    a service because it does something."""

    def __init__(self):
        pass

    @staticmethod
    def reverse_string(str):
        return str[::-1]