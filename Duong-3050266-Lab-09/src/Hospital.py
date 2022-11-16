from .MaxHeap import MaxHeap
from .Patient import Patient


class Hospital:
    """
    Runs a hospital

    Doesn't make much sense as a class right now,
    but if you needed to modify the heap on-demand this would've been more useful
    """

    def __init__(self) -> None:
        self.heap: MaxHeap[Patient] = MaxHeap()

    def run(self, hospital_records_file_location: str) -> None:
        """
        Takes in a place to read patient in/out log record from and run the commands
        """
        with open(hospital_records_file_location, encoding="utf8") as f:
            log: list[str] = f.readlines()
            for line in log:
                line_formatted: list[str] = line.rstrip("\n").split(" ")
                line_command: str = line_formatted[0].lower()
                line_params: list[str] = line_formatted[1::]
                if line_command == "arrive":
                    self.heap.insert(Patient.parseLine(line_params))
                elif line_command == "count":
                    count: int = len(self.heap)
                    plural: bool = count != 1
                    print(
                        f"There {'are' if plural else 'is'} {count} patient{'s' if plural else ''} waiting."
                        + "\n"
                    )
                elif line_command == "next":
                    next: Patient | None = self.heap.peek()
                    if next:
                        print(
                            "Next patient:" + "\n\t"
                            + "\n\t".join(
                                [
                                    f"Name: {next.l_name}, {next.f_name}",
                                    f"Age: {next.age}",
                                    f"Suffers from: {next.illness}",
                                    f"Illness severity: {next.severity}",
                                ]
                            )
                        + "\n")
                    else:
                        print("No next patient\n")
                elif line_command == "treat":
                    self.heap.pop()
                else:
                    print(
                        f"Invalid command '{line.rstrip()}', could not parse, ignoring..." + "\n"
                    )
