import subprocess

class SyncEngine:
    def __init__(self):
        self.tcp_params = {
            "TCPWindowSize": 1048576,
            "TcpAckFrequency": 1,
            "TcpNoDelay": 1,
            "TcpDelAckTicks": 0,
            "Tcp1323Opts": 1,
            "TcpMaxDupAcks": 2
        }

    def apply_settings(self):
        try:
            for param, value in self.tcp_params.items():
                command = f"netsh int tcp set global {param}={value}"
                subprocess.run(command, shell=True, check=True)
            print("Network settings optimized successfully.")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while applying settings: {e}")

    def reset_settings(self):
        try:
            command = "netsh int tcp reset"
            subprocess.run(command, shell=True, check=True)
            print("Network settings have been reset to default.")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while resetting settings: {e}")

if __name__ == "__main__":
    print("SyncEngine: Optimizing network settings for better performance.")
    engine = SyncEngine()
    engine.apply_settings()

    user_input = input("Do you want to reset the settings to default? (y/n): ").strip().lower()
    if user_input == 'y':
        engine.reset_settings()
    else:
        print("Settings remain optimized.")