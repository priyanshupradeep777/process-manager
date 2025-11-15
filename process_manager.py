import psutil

def list_processes():
    print("\n--- Running Processes ---")
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            print(f"PID: {proc.info['pid']}\tName: {proc.info['name']}\tCPU: {proc.info['cpu_percent']}%\tMemory: {round(proc.info['memory_percent'], 2)}%")
        except:
            pass

def system_info():
    print("\n--- System Information ---")
    print(f"CPU Cores: {psutil.cpu_count(logical=True)}")
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    print(f"Total RAM: {round(psutil.virtual_memory().total / (1024**3), 2)} GB")
    print(f"RAM Usage: {psutil.virtual_memory().percent}%")

def main():
    while True:
        print("\n========== PROCESS MANAGER ==========")
        print("1. List all running processes")
        print("2. View system information")
        print("3. Kill a process")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_processes()

        elif choice == '2':
            system_info()

        elif choice == '3':
            try:
                pid = int(input("Enter PID to kill: "))
                p = psutil.Process(pid)
                p.terminate()
                print(f"Process {pid} terminated successfully!")
            except Exception as e:
                print(f"Failed to terminate process: {e}")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()




 
