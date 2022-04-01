
from corp_name.project_name.module_name.services.reverse_string_service import ReverseStringService

class HandlerModuleName:
    """This is an example of a handler. We call this the HandlerModuleName (or
    ModuleNameHandler) because it handles whatever is happening in ModuleName.
    The idea is that a handler handles the input and is instantiated or consumes
    multiple services. In this case, the ReverseStringService."""

    def __init__(self, reverse_string_service: ReverseStringService):
        self.reverse_string_service = reverse_string_service

    def handle_input(self, input):
        return self.reverse_string_service.reverse_string(input)