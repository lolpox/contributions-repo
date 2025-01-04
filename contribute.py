import os
from datetime import datetime, timedelta
from subprocess import Popen

def generate_custom_dates():
    current_date = datetime.now()
    start_date = current_date - timedelta(weeks=51 + 1)  # 53 semanas atrás desde la fecha actual
    start_date = start_date - timedelta(days=start_date.weekday() + 1)  # Ajustar al domingo

    # Patrón original de intervalos en semanas y días
    intervals = [
        1, 1, 1, 1, 1, 1, 4, 7, 4, 1, 1, 1, 1, 1, 1, 8, 1, 1,
        1, 1, 1, 1, 1, 3, 3, 1, 3, 3, 1, 6, 8, 1, 1, 1, 1, 1, 1,
        7, 7, 8, 1, 1, 1, 1, 1, 1, 7, 7, 9, 1, 1, 1, 1, 2, 6, 1,
        6, 1, 6, 2, 1, 1, 1, 1, 23, 1, 1, 1, 1, 1, 1, 1,
        6, 1, 3, 3, 1, 1, 2, 1, 1, 1, 8, 1, 1, 1, 1, 1, 1, 8, 7, 
        1, 1, 1, 1, 1, 1, 1, 14, 1, 1, 1, 1, 1, 1, 4, 7, 4, 1, 1,
        1, 1, 1, 1, 8, 1, 1, 1, 1, 1, 8, 7, 7, 1, 1, 1, 1, 1, 1, 9,
        1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 3, 3, 2, 1, 2, 1, 1

    ]

    custom_dates = []
    current = start_date
    for interval in intervals:
        custom_dates.append(current.strftime("%Y-%m-%d"))
        current += timedelta(days=interval)
    return custom_dates

def main():
    directory = "custom-contributions-repo"
    if not os.path.exists(directory):
        os.mkdir(directory)
    os.chdir(directory)
    run(["git", "init", "-b", "main"])

    custom_dates = generate_custom_dates()
    for date in custom_dates:
        create_contributions_for_date(date)

    print("Contributions added successfully!")

def create_contributions_for_date(date):
    base_date = datetime.strptime(date, "%Y-%m-%d")
    for i in range(5):
        commit_time = base_date + timedelta(hours=i * 3)
        contribute(commit_time)

def contribute(date):
    with open(os.path.join(os.getcwd(), "README.md"), "a") as file:
        file.write(f"Contribution on {date.strftime('%Y-%m-%d %H:%M:%S')}\n")
    run(["git", "add", "."])
    run(["git", "commit", "-m", f"Contribution on {date.strftime('%Y-%m-%d %H:%M:%S')}",
         "--date", date.strftime("%Y-%m-%d %H:%M:%S")])

def run(commands):
    Popen(commands).wait()

if __name__ == "__main__":
    main()