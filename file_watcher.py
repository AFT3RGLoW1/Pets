import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder):
            file_type = filename.split(".")
            if len(file_type) > 1 and (file_type[1].lower() == "jpg" or file_type[1].lower() == "png" or file_type[1].lower() == "svg"):
                file = folder + "/" + filename
                new_path = folder_dest + "/" + filename
                os.rename(file, new_path)

folder = r""    # write down folder to observe
folder_dest = r""   # write down folder for your photos

handle = Handler()
obs = Observer()
obs.schedule(handle, folder, recursive=True)
obs.start()

if __name__ == "__main__":
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        obs.stop()
    obs.join()
