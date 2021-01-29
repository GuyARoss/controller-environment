import os
import socket
import sys
import struct

from typing import Callable, NoReturn

class BaseIPC:
    instance = None

    def __init__(self, name: str):
        if not os.path.exists('./temp'):
            os.makedirs('./temp')

        self.fifo_path = f'./temp/{name}' 
        try:
            os.mkfifo(self.fifo_path)
        except:
            # fifo already exists
            pass

    def write(self, data: str):
        instance = os.open(self.fifo_path, os.O_RDWR) if self.instance is None else self.instance   
        self.instance = instance

        encoded_data = str.encode(data)
        os.write(instance, struct.pack('B', len(encoded_data)))
        os.write(instance, encoded_data)

    def read(self) -> str:
        instance = os.open(self.fifo_path, os.O_RDONLY|os.O_NONBLOCK) if self.instance is None else self.instance   
        self.instance = instance 

        size = struct.unpack('B', os.read(instance, 1))[0]
        data = []
        for cidx in range(size):
            data += os.read(instance, 1).decode()

        return "".join(data) 

    def close(self) -> NoReturn:
        os.close(self.instance)

if __name__ == '__main__':
    ipc = BaseIPC(name='test123')
    ipc.write('123')

    resp = ipc.read()
    print('respo', resp)

    ipc.close()
    assert resp == '123'
