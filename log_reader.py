def read_logs(file_path):
    print("\n🔍 Error Lines Found:\n")

    with open(file_path, "r") as file:
        for line in file:
            if "error" in line.lower() or "fail" in line.lower():
                print(line.strip())

if __name__ == "__main__":
    log_file = "application.log"
    read_logs(log_file)
