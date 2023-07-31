import psutil

def get_running_processes():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        processes.append(proc.info)
    return processes

def get_running_services():
    services = []
    for service in psutil.win_service_iter():
        services.append(service.as_dict())
    return services

def print_banner():
    banner = """
░█░░░█░█░█░█░█▀█░░░█░█░█▀█░█▀▀░▀█▀░▀█▀░█▀█░█▀▀
░█░░░█░█░█▀▄░█▀█░░░█▀█░█░█░▀▀█░░█░░░█░░█░█░█░█
░▀▀▀░▀▀▀░▀░▀░▀░▀░░░▀░▀░▀▀▀░▀▀▀░░▀░░▀▀▀░▀░▀░▀▀▀"""
    print(banner)

if __name__ == "__main__":
    print_banner()

    print("\nRunning Processes:")
    processes = get_running_processes()
    for proc in processes:
        print(f"PID: {proc['pid']}, Name: {proc['name']}, User: {proc['username']}")

    print("\nRunning Services:")
    services = get_running_services()
    for service in services:
        print(f"Name: {service['name']}, Display Name: {service['display_name']}")

