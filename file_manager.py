import os

FILENAME = "time.txt"

def load_time():
    if not os.path.exists(FILENAME):
        return None
        
    try:
        with open(FILENAME, 'r') as file:
            return float(file.read())
    except ValueError:
        return None

def save_time(time_taken):
    current_best = load_time()
    
    if current_best is None or time_taken<current_best:
        try:
            with open(FILENAME, 'w') as file:
                file.write(str(time_taken))
            print(f"New best: {time_taken:.2f} seconds!")
        except IOError:
            print("Best time couldnt be saved")