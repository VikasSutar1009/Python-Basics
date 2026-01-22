import shutil

def backup(src, dest):
    shutil.copy(src, dest)
    print("Backup Completed")

backup("data.txt", "backup_data.txt")