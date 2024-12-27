# pip install rich
# rich can display highly customizable progress bars, making it easier to track the progress of long-running tasks

from rich.progress import Progress

import time

# set up progress bar
with Progress() as progress:
    task = progress.add_task("[red]Downloading...", total=100)

    # update progress in a loop
    while not progress.finished:
        progress.update(task, advance=10)
        time.sleep(0.4)