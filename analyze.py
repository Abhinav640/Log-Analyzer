import re
import pdb

def log_format(orignal_file, formatted_file):

    log_data = []    
    current_log = ""
    timestamp_pattern = r'^(\[\d{4}-\d{2}-\d{2})'

    with open (orignal_file, "r") as file:
        # pdb.set_trace()
        log_file = file.readlines()
        for lines in log_file:
            lines = lines.strip()

            if re.match(timestamp_pattern, lines):
                if current_log != "":
                    log_data.append(current_log)
                current_log = lines
            else:
                current_log = current_log + " " + lines

        if current_log != "":
            log_data.append(current_log)
                
    with open(formatted_file, "w") as cor_file:
        for line in log_data:
            updated_line = line.replace("  ", " ")
            cor_file.write(updated_line + "\n")

def log_parser(formatted_file):
    error_type = {}
    with open (formatted_file, "r") as file:
        log_file = file.readlines()
        for lines in log_file:
            error = lines.split(" ")[2]
            if error not in error_type:
                error_type[error] = 1
            else:
                error_type[error] += 1
            
    return error_type

def log_list(formatted_file, error_type):
    with open (formatted_file, "r") as file:
        log_file = file.readlines()
        for lines in log_file:
            if error_type in lines:
                print(lines)
    