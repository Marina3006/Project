import os
import signal
import subprocess
import shlex
from typing import List

from flask import Flask

app = Flask(__name__)


def get_pids(port: int) -> List[int]:
    """
    Возвращает список PID процессов, занимающих переданный порт
    @param port: порт
    @return: список PID процессов, занимающих порт
    """
    if not isinstance(port, int):
        raise ValueError

    pids: List[int] = []
    cmd = f"lsof -i :{port}"
    args = shlex.split(cmd)
    output = subprocess.run(args, capture_output=True)
    result = str(output.stdout).split('\\n')[1:]
    [pids.append(int(i.split()[1])) for i in result if len(i) > 1]
    return pids


def free_port(port: int) -> None:
    """
    Завершает процессы, занимающие переданный порт
    @param port: порт
    """
    pids: List[int] = get_pids(port)
    [os.kill(pid, signal.SIGINT) for pid in pids if pids]


def run(port: int) -> None:
    """
    Запускает flask-приложение по переданному порту.
    Если порт занят каким-либо процессом, завершает его.
    @param port: порт
    """
    free_port(port)
    app.run(port=port)


if __name__ == '__main__':
    run(5000)