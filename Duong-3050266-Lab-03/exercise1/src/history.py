import os.path
import sys
from .linked_list import LinkedList

class History:
    def __init__(self):
        self._buffer = LinkedList()
        # init at -1, as default failcase
        self.index = 0
        self.COMMANDS = {
            "NAVIGATE": self.navigate_to,
            "BACK": self.back,
            "FORWARD": self.forward,
            "HISTORY": self.history,
        }

    def navigate_to(self, url=None):
        """
        Navigate to a url

        :param url: string to navigate to
        """
        if url is None or url == "":
            print("A url is a required parameter for NAVIGATE")
            return
        if self.index != len(self._buffer):
            self._buffer = self._buffer[:self.index + 1] + LinkedList(url)
        else:
            self._buffer.append(url)
        self.forward()

    def back(self):
        """
        Goes back in history
        """
        self.index -= 1 if self.index > 0 and len(self._buffer) > 1 else 0

    def forward(self):
        """
        Goes forward in history
        """
        history_len = len(self._buffer) - 1  # 0 indiced
        self.index += 1 if history_len > self.index and self.index != history_len else 0

    def history(self):
        """
        Displays the current history
        """
        list_history = "\n".join(
            iter(
                LinkedList(
                    *iter(
                        f'{f"{url}":<20}{"<==current" if index == self.index else ""}'.rstrip()
                        for index, url in enumerate(self._buffer)
                    )
                )
            )
        )
        print(
            f"""Oldest
===========
{list_history}
===========
Newest
"""
        )

    def input_command(self, command, *argv):
        """
        Input a command

        :param command: Command to use, supported commands 'NAVIGATE', 'BACK', 'FORWARD', 'HISTORY', 'EXIT'
        :param *argv: Superfluous arguments to pass to command function
        """
        command_upper = command.upper()
        if command_upper not in LinkedList(
            "NAVIGATE", "BACK", "FORWARD", "HISTORY", "EXIT"
        ):
            print(f"Invalid command '{command_upper}'.\nIgnoring and continuing...")
        else:
            try:
                self.COMMANDS[command_upper](*argv)
            except TypeError:
                print(
                    f"Invalid command '{command_upper}' with invalid arguments: {argv}\nIgnoring and continuing..."
                )

    def prompt_file_input(self):
        """Prompt the user for a file to read history from"""

        file_name = input("Enter the name of the input file (exercise1_input.txt): ")
        if file_name == "":
            file_name = "exercise1_input.txt"
        while not os.path.isfile(file_name):
            file_name = input(
                "File was not found, please try again (exercise1_input.txt): "
            )
            if file_name == "":
                file_name = "exercise1_input.txt"
        with open(file_name, encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                # I think split uses a list built-in? Is this allowed. w/e...
                self.input_command(*line.strip().split(" "))
