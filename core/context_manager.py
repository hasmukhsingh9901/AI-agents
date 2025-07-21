import subprocess

def get_git_history():
    log = subprocess.check_output(["git", "log", "--oneline", "-n", "10"])
    return log.decode("utf-8")

def get_changed_files():
    diff = subprocess.check_output(["git", "diff", "--name-only", "HEAD"])
    return diff.decode("utf-8").splitlines()
