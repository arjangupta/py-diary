def main():
    f = open("file.txt", "r")
    g = open("file_corrected.txt", "w")
    corrected_line = ""
    if f.mode == "r" and g.mode == "w":
        lines = f.readlines()
        for line in lines:
            line = line.replace(" 1 ", " 0 ", 1)
            g.write(line)
    f.close()
    g.close()

                

if __name__ == '__main__':
    main()