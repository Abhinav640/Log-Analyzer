from analyze import log_format, log_parser, log_list

def main():
    orignal_file = "sample.log"
    formatted_file = "formated.log"
    error_type = "debug"
    log_format(orignal_file, formatted_file)
    print(log_parser(formatted_file))
    log_list(formatted_file, error_type.upper())


if __name__ == "__main__":
    main()