from .automation_utils import execute_command

if __name__ == "__main__":
    while True:
        execute_command('/weather clear')
        execute_command('/time set day')
        time.sleep(60)
