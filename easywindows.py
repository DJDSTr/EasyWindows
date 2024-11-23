import argparse
import os
import subprocess
import shutil

def run_command(name, *args):
    """Run a predefined command with arguments."""
    commands = {
        "ip grab": lambda localhost: subprocess.run([f"ssh", "-R", f"80:localhost:{localhost}", "serveo.net"], check=True),
        "terminate": lambda process_name: subprocess.run(["taskkill", "/IM", process_name, "/F"], check=True),
        "download": lambda url: subprocess.run(["curl", "-O", url], check=True),
        "create_directory": lambda directory_name: os.makedirs(directory_name, exist_ok=True),
        "list_directory": lambda path=".": print("\n".join(os.listdir(path))),
        "move_file": lambda source, destination: shutil.move(source, destination),
        "rename_file": lambda old_name, new_name: os.rename(old_name, new_name),
        "delete_file": lambda file_path: os.remove(file_path),
        "ping": lambda host: subprocess.run(["ping", "-n", "4", host], check=True),
        "open_program": lambda program_path: os.startfile(program_path),
        "system_info": lambda: subprocess.run(["systeminfo"], check=True),
        "shutdown": lambda: subprocess.run(["shutdown", "/s", "/t", "0"], check=True),
        "restart": lambda: subprocess.run(["shutdown", "/r", "/t", "0"], check=True),
        "refresh": lambda process_name: (
            subprocess.run(["taskkill", "/IM", process_name, "/F"], check=True),
            subprocess.run(["start", process_name], shell=True),
        ),
    }

    try:
        if name not in commands:
            raise ValueError(f"Unknown command: {name}")
        commands[name](*args)
        print(f"Command '{name}' executed successfully.")
    except Exception as e:
        print(f"Error executing '{name}': {e}")

def main():
    parser = argparse.ArgumentParser(
        description="EasyWindows - Simplify Windows CMD commands.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    # If no arguments are provided, show a usage message
    if len(os.sys.argv) == 1:
        print("Usage: python easywindows.py command [arguments ...]")
        return

    # Define the command-line arguments
    parser.add_argument("command", help="The command to execute")
    parser.add_argument("arguments", nargs="*", help="Arguments for the command")

    # Add subcommands with descriptions for each command
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    subparsers.add_parser("terminate", help="Terminate a process by name.\nArguments: process_name")
    subparsers.add_parser("download", help="Download a file from a URL.\nArguments: url")
    subparsers.add_parser("create_directory", help="Create a new directory.\nArguments: directory_name")
    subparsers.add_parser("list_directory", help="List contents of a directory.\nArguments: [path] (default: current directory)")
    subparsers.add_parser("move_file", help="Move a file to a new location.\nArguments: source destination")
    subparsers.add_parser("rename_file", help="Rename a file or directory.\nArguments: old_name new_name")
    subparsers.add_parser("delete_file", help="Delete a file.\nArguments: file_path")
    subparsers.add_parser("ping", help="Ping a host to check connectivity.\nArguments: host")
    subparsers.add_parser("open_program", help="Open a program by its path.\nArguments: program_path")
    subparsers.add_parser("system_info", help="Display system information.\nNo arguments required.")
    subparsers.add_parser("shutdown", help="Shut down the system.\nNo arguments required.")
    subparsers.add_parser("restart", help="Restart the system.\nNo arguments required.")
    subparsers.add_parser("refresh", help="Refresh (restart) a process.\nArguments: process_name")
    subparsers.add_parser("ip grab", help="Gets anyones ip that enter the serveo url. \nArguments: localhost")


    # Parse the command-line arguments
    args = parser.parse_args()

    if args.command is None:
        # Display the general usage if no command is provided
        parser.print_help()
    else:
        # Execute the command if valid
        run_command(args.command, *args.arguments)

if __name__ == "__main__":
    main()
