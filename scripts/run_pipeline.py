import subprocess
import sys
import time


def run_script(module_name):
    print(f"\n{'=' * 60}")
    print(f"Running: {module_name}")
    print(f"{'=' * 60}")

    subprocess.run(
        [sys.executable, "-m", module_name],
        check=True
    )


def main():

    start = time.time()

    scripts = [
        "scripts.extract",
        "scripts.transform",
        "scripts.load_postgres",
        "scripts.load_dimension",
        "scripts.load_fact",
        "scripts.load_mongodb",
        "scripts.report_excel"
    ]

    for script in scripts:
        run_script(script)

    end = time.time()

    print("\n✅ Pipeline Completed Successfully!")
    print(f"Execution Time: {round(end - start, 2)} seconds")


if __name__ == "__main__":
    main()