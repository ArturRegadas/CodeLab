class Calculator:
    def sum(a:int, b:int, c:int = None) -> int:
        return a + b if c is None else a + b + c
