import subprocess
import webbrowser

def install_requirements():
    try:
        subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
        print("Requirements installed successfully.")
    except subprocess.CalledProcessError:
        print("Error installing requirements.")

def run_script():
    try:
        subprocess.run(["python", "run.py"], check=True)
        print("run.py executed successfully.")
    except subprocess.CalledProcessError:
        print("Error running run.py.")

def open_browser():
    try:
        url = "https://textmate-frontend.vercel.app"
        webbrowser.open(url, new=0, autoraise=True)
        print("Web browser opened successfully.")
    except Exception as e:
        print(f"Error opening web browser: {e}")

if __name__ == "__main__":
    install_requirements()
    open_browser()
    run_script()
