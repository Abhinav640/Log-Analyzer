from analyze import LogAnalyzer

import argparse

def main():
    parser = argparse.ArgumentParser(description= "This is a LogAnalyser that assis you with logs")
    parser.add_argument("original_file", metavar="RAW_LOG_FILE", type=str, help= "path to your raw log file")
    parser.add_argument("formatted_file", metavar="UPDATED_LOG_FILE", type=str, help= "this file gets created after formating the raw file")
    parser.add_argument("error_type", metavar="ERROR_TYPE", type=str, help= "enter the error type you are looking for")
    parser.add_argument("analyzer", metavar="APP_FUNCTION", type=str, help= "enter what are you looking for")
    
    args = parser.parse_args()

    original_file = args.original_file
    formatted_file = args.formatted_file
    error_type = args.error_type


    analyze = LogAnalyzer(original_file, formatted_file, error_type)

    app_function = args.analyzer

    analyze.log_format()
    if app_function == "log_parser":
        print(analyze.log_parser())
    elif app_function == "log_list":
        print(analyze.log_list())
    elif app_function == "act":
        print(analyze.act())
        

if __name__ == "__main__":
    main()