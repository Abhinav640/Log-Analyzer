from analyze import log_format

def main():
    orignal_file = "sample.log"
    formatted_file = "formated.log"
    log_format(orignal_file, formatted_file)


if __name__ == "__main__":
    main()