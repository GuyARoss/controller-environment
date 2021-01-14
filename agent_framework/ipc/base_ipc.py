import socket
import sys

from typing import Callable

class BaseIPC:
    def __init__(self, name: str):
        pass

    def write(self, data: str):
        pass

    def read(self) -> str:
        pass