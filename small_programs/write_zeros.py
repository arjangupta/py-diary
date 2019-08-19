import sys

def main():
    input_file_name = sys.argv[1]
    f = open(input_file_name, "r")
    output_file = input_file_name.replace("output", "output2", 1)
    g = open(output_file, "w")
    corrected_line = ""
    if f.mode == "r" and g.mode == "w":
        lines = f.readlines()
        for line in lines:
            line = line.replace(", ...", "", 1)
            g.write(line)
    f.close()
    g.close()

                

if __name__ == '__main__':
    main()