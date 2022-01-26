class Hello:
    _name: str = None

    def __init__(self, name: str = None) -> None:
        self._name = name

    def __repr__(self) -> str:
        return self._name

    def say_hello(self) -> None:
        msg: str = f"Hello, {self._name}; welcome to the world of Python."
        print(msg)


def main() -> None:
    inp_str = input("Enter your name: ")
    hello = Hello(inp_str)
    hello.say_hello()

if __name__ == "__main__":
    main()
