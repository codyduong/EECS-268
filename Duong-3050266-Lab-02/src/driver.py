
from .cpu_scheduler import CPUScheduler

def main():
    file_name = input("Enter the name of the input file (default: entry.txt): ")
    cpu = CPUScheduler()
    with open(file_name  or "entry.txt", encoding="utf-8") as f:
        cpu.run(f.read())


if __name__ == "__main__":
    main()
