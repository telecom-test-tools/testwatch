import sys
from watcher import watch_log

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <logfile>")
        return

    logfile = sys.argv[1]
    watch_log(logfile)

if __name__ == "__main__":
    main()