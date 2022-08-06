from pathlib import Path


def handle_stats(mode: str) -> int:
    """Handles reading from and writing to the stats.txt file.

    Args:
        mode (str): Can be either 'r' for 'read only' or 'w' for 'read and write'. Calling
        handle_stats('w') will result in the stat counter being increased by one (1).

    Returns:
        int: The stats counter, as an integer.
    """
    # Create file 'stats.txt' if it didn't exist already.
    Path("stats.txt").touch(exist_ok=True)
    data = 0
    # Open 'stats.txt' in read only mode.
    with open("stats.txt", "r") as file:
        data = file.read()
        # If the file is empty, for example on first deploy, simply return 0.
        if mode == "r":
            if data == "":
                return 0
            # If the file is not empty, return the statistic.
            else:
                return int(data)

    # Open the file in write mode, if the function has been called with the 'w' mode.
    if mode == "w":
        with open("stats.txt", "w") as file:
            # If the file is empty, initialize it with the value 1.
            if data == "":
                file.write(str(1))
            else:
                # Else, override the current statistic by the current statistic + 1.
                file.write(str(int(data) + 1))
        file.close()
        return int(data) + 1
