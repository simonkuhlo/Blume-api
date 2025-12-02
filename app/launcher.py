import subprocess
import threading
import sys

def forward_output(pipe, prefix):
    for line in iter(pipe.readline, b''):
        sys.stdout.write(f"{prefix} {line.decode()}")
    pipe.close()

if __name__ == "__main__":
    frontend = subprocess.Popen(
        ["python", "server.py"],
        cwd="frontend",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    backend = subprocess.Popen(
        ["python", "server.py"],
        cwd="backend",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # Threads to forward stdout and stderr of frontend
    threading.Thread(target=forward_output, args=(frontend.stdout, "FRONTEND:")).start()
    threading.Thread(target=forward_output, args=(frontend.stderr, "FRONTEND ERR:")).start()

    # Threads to forward stdout and stderr of backend
    threading.Thread(target=forward_output, args=(backend.stdout, "BACKEND:")).start()
    threading.Thread(target=forward_output, args=(backend.stderr, "BACKEND ERR:")).start()

    frontend.wait()
    backend.wait()
