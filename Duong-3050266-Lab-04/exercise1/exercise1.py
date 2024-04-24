import functools

class RecursivePower:
    def __init__(self):
        pass

    @functools.cache
    def recursive_power(self, base, power):
        """
        Return the base^power

        :param base: any int
        :param power: any int >= 0
        :return: int, result of base^power
        """
        return (
            base
            if power == 1
            else self.recursive_power(base, power - 1) * base
            if power != 0
            else 1
        )

    def prompt(self):
        """Prompt the user for a base and power"""
        base = None
        power = None

        while True:
            try:
                base = input("Enter a base: ")
                base = int(base)
                if isinstance(base, int):
                    break
            except Exception as e:
                print(f"There was an error, try again!\n {e}")

        while True:
            try:
                power = input("Enter a power: ")
                power = int(power)
                if power < 0:
                    print("Sorry, your exponent must be zero or larger.")
                elif power >= 0 and isinstance(power, int):
                    break
            except Exception as e:
                print(f"There was an error, try again!\n {e}")

        print(f"Answer: {self.recursive_power(base, power)}")


if __name__ == "__main__":
    RecursivePower().prompt()