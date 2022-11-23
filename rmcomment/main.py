def main():
    file = open("sztring1.py", "r")
    Lines = file.readlines()
    file.close()
    cleanfile = []

    for line in Lines:
        if("#" in line):
            if(line.strip()[0]=="#"):
                cleanfile.append("")
            else:
                comment_start = line.index("#")
                cleanfile.append(line[:comment_start]+"\n")
        else:
            cleanfile.append(line)

    writeme = open("sztring1_clean.py", "w")
    for line in cleanfile:
        writeme.write(line)
    writeme.close()


if __name__ == '__main__':
    main()