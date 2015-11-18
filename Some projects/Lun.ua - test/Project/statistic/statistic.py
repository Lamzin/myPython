if __name__ == "__main__":

    report = open("report.txt", "r")
    new_report = open("new_report.txt", "w")

    files = [open("%d.txt" % i, "w") for i in range(4)]

    id = {}
    for line in report:
        line = line.replace("apartment layout", "apartment_layout")
        line_split = line.split()
        if line_split[0] not in id:
            id[line_split[0]] = [line_split[1], line_split[2]]

    res = [[0, 0], [0, 0]]

    for key, value in id.iteritems():
        i_key = value[0].split("=")[1]
        j_key = value[1].split("=")[1]
        i = 0 if i_key == "apartment_layout" else 1
        j = 0 if j_key == "apartment_layout" else 1
        res[i][j] += 1
        files[i * 2 + j].write("%s %s %s\n" % (key, value[0], value[1]))
        new_report.write("%s %s %s\n" % (key, i_key, j_key))

    file_rep = open("count.txt", "w")

    file_rep.write(str(len(id)) + "\n")
    file_rep.write(str(res) + "\n")
