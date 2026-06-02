import schedule
import time
import subprocess

def run_pipeline():
    print("Running pipeline...")
    subprocess.run(["python3", "load_to_db.py"])
    print("Pipeline complete.")

# Schedule it to run every day at 8am
schedule.every().day.at("08:00").do(run_pipeline)

print("Scheduler started. Pipeline will run every day at 08:00.")
print("Press Ctrl+C to stop.")

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)
