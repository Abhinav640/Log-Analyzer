import re
import pdb

class LogAnalyzer:
    def __init__(self,orignal_file, formatted_file, error_type):
        self.orignal_file = orignal_file
        self.formatted_file = formatted_file
        self.error_type = error_type
        

    def log_format(self):

        log_data = []    
        current_log = ""
        timestamp_pattern = r'^(\[\d{4}-\d{2}-\d{2})'

        with open (self.orignal_file, "r") as file:
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
                    
        with open(self.formatted_file, "w") as cor_file:
            for line in log_data:
                updated_line = line.replace("  ", " ")
                cor_file.write(updated_line + "\n")

    def log_parser(self):
        error_types = {}
        with open (self.formatted_file, "r") as file:
            log_file = file.readlines()
            for lines in log_file:
                error = lines.split(" ")[2].upper()
                if error not in error_types:
                    error_types[error] = 1
                else:
                    error_types[error] += 1
                
        return error_types

    def log_list(self):
        error_list = []
        with open (self.formatted_file, "r") as file:
            log_file = file.readlines()
            for lines in log_file:
                error_type = str(self.error_type).upper()                
                if error_type in lines:                    
                    error_list.append(lines) 
        return error_list
    
    def act(self):
        error_count = self.log_parser()[self.error_type.upper()]
        if error_count >= 10:
            return f"high amount of {self.error_type} - log count: {error_count}"
        