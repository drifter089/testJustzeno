import zenodopy
import time  # Optional: For adding delay between retries

max_retries = 5

for attempt in range(1, max_retries + 1):
    try:

        zeno = zenodopy.Client(
            sandbox=True,
            token="CNXNk6GBg0dQUvZJsCUEajG4ZZnAr8YUrWPR9oCucnu8vq39jFJDUGoYW6WK",
        )

        zeno.set_project(dep_id=106299)

        zeno.update(
            source="/home/runner/work/testJustzeno/testJustzeno/test.py",
            publish=True,
            metadata_json="/home/runner/work/testJustzeno/testJustzeno/.zenodo.json",
        )
        print("Update succeeded.")
        break  # Exit the loop if the update is successful

    except Exception as e:
        print(f"Attempt {attempt} failed with error: {e}")

        time.sleep(2)  # Optional: Wait before retrying

        zeno._delete_project(dep_id=106299)

        if attempt == max_retries:
            print("Max retries reached. Exiting.")
            raise  # Re-raise the exception to fail after max retries
        else:
            time.sleep(2)  # Optional: Wait before retrying
