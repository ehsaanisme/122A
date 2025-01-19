import sys

roster = sys.stdin.read()
roster = roster.split()

def hello(name: str) -> str:
    print(f"Hello {name}!")

for name in roster:
    hello(name)