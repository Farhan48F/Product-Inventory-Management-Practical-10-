

import subprocess
import sys

def run_ruff():
    print("Running Ruff checks...")

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "ruff",
            "check",
            "inventory.py",
            "test_inventory.py"
        ],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.returncode == 0:
        print("No linting errors found!")
    else:
        print("Linting issues detected!")
        print(result.stderr)


if __name__ == "__main__":
    run_ruff()
