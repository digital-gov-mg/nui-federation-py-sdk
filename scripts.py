import subprocess


def lint():
    subprocess.run(["flake8", "src", "tests"])


def format():
    subprocess.run(["black", "src", "tests"], check=True)
