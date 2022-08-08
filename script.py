import sys
import getopt

def main(argv):
    first_name = ""
    last_name = ""
    file_path = ""
    
    try:
        opts, args = getopt.getopt(argv[1:], "f:l:o:", ["fname=", "lname="])
    except getopt.GetoptError:
        print("fail")

    for opt, arg in opts:
        if opt in ("-f", "--fname"):
            first_name = arg
        elif opt in ("-l", "--lname"):
            last_name = arg
        elif opt in ("-o", "--ofile"):
            file_path = arg
            
    with open(file_path, "w") as f:
        f.write(first_name)
        f.write(" ")
        f.write(last_name)


if __name__ == "__main__":
    main(sys.argv)

