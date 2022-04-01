import copy
import argparse
import sys
import os

# Option 1: Add src folder to PYTHONPATH, see: https://stackoverflow.com/q/53760098
# Option 2: Add as source folder in Pycharm
# 1. YOU MUST ADD IT LOCALLY
# sys.path.append(os.path.join(os.path.realpath(os.path.dirname(__file__)), "../", "src"))

# Services (things that *do* things)
from corp_name.project_name.module_name.services.reverse_string_service import ReverseStringService

# Handlers (things that combine and wrap around services)
from corp_name.project_name.module_name.handler import HandlerModuleName

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument(
    '--input',
    type=str,
    default="Hello world",
    help='String to be reversed.'
)

if __name__ == "__main__":
    args = copy.copy(vars(parser.parse_args()))

    handler = HandlerModuleName(reverse_string_service=ReverseStringService)

    output = handler.handle_input(input=args['input'])

    print(output)