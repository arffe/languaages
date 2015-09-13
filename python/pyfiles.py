#python - file access


def main():
    print "HELLO"
    f = open("textfile.txt","w+")
    for i in range(10):
        f.write("this is line %d\r\n" % (i+1))
    
if __name__ == "__main__":
    main()
