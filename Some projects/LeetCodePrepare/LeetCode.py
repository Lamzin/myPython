import os


def Solved():
    file = open("Solved.txt", "r")
    for line in file:
        if len(line) > 1:
            line_split = line.split()
            while(len(line_split[0]) < 3):
                line_split[0] = "0" + line_split[0]
            solve_name = "Solution/" + " ".join(line_split[0:-2]) + ".cpp"
            solve = open(solve_name, "w")

def All():
    file = open("All.txt", "r")
    for line in file:
        if len(line) > 1:
            line_split = line.split()
            while(len(line_split[0]) < 3):
                line_split[0] = "0" + line_split[0]
            solve_name = "All/" + " ".join(line_split[0:-2]) + ".cpp"
            solve = open(solve_name, "w")

if __name__ == "__main__":
    # Solved()
    All()
