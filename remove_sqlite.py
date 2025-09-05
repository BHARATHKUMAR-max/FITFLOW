import os
import time

def remove_sqlite_file():
    """Remove the SQLite database file if it exists."""
    if os.path.exists('db.sqlite3'):
        try:
            os.remove('db.sqlite3')
            print("SQLite database file successfully removed!")
        except PermissionError:
            print("Could not remove the file because it's being used by another process.")
            print("Please make sure all Django instances are stopped and try again.")
            print("You can also try removing it manually after stopping all Django processes.")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("SQLite database file not found. It may have been already removed.")

if __name__ == "__main__":
    remove_sqlite_file() 