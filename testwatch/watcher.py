from parser import parse_line

def watch_log(file_path):
    passed = 0
    failed = 0

    with open(file_path, "r") as file:
        lines = file.readlines()

    for line in lines:
        result = parse_line(line)

        if result == "FAIL":
            failed += 1
            print(f"❌ {line.strip()}")
        else:
            passed += 1
            print(f"✔ {line.strip()}")

    print("\nSummary")
    print("Passed:", passed)
    print("Failed:", failed)