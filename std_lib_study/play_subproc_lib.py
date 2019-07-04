import subprocess

def main():
    proc = subprocess.Popen("ls -l")
    print(proc.stdout)

if __name__ == "__main__":
    main()