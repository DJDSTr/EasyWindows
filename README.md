
# EasyWindows  

**EasyWindows** is a command-line tool designed to simplify complex Windows CMD commands into user-friendly shortcuts. With EasyWindows, you can manage processes, files, directories, and system functions with ease and speed.

---

## Features  

- **Process Management**: Terminate, refresh, or open processes with simple commands.  
- **File Management**: Create, move, rename, or delete files and directories effortlessly.  
- **System Utilities**: Check connectivity, retrieve system information, or perform shutdown/restart operations.  
- **Network Tools**: Includes IP logging functionality through a Serveo URL.  

---

## Installation  

1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/yourusername/easywindows.git
   ```  

2. **Navigate to the Directory**:  
   ```bash
   cd easywindows
   ```  

3. **Install Dependencies**:  
   EasyWindows doesn’t require external Python libraries. Ensure Python 3.7+ is installed.  

4. **Add to PATH (Optional)**:  
   Add the EasyWindows directory to your system's PATH to use it globally.  

---

## Usage  

Run the script with Python and specify a command.  

### Examples  

- **Terminate a Process**:  
  ```bash
  python easywindows.py terminate chrome.exe
  ```  

- **Download a File**:  
  ```bash
  python easywindows.py download https://example.com/file.zip
  ```  

- **Refresh a Process**:  
  ```bash
  python easywindows.py refresh chrome.exe
  ```  

- **Create a Directory**:  
  ```bash
  python easywindows.py create_directory MyNewFolder
  ```  

- **Ping a Host**:  
  ```bash
  python easywindows.py ping google.com
  ```  

### Help Command:  

Display available commands and usage instructions.  
```bash
python easywindows.py --help
```  

---

## Commands  

| Command              | Description                                               | Example Usage                                     |  
|----------------------|-----------------------------------------------------------|-------------------------------------------------|  
| `terminate`          | Terminate a process by name.                              | `easywindows terminate chrome.exe`             |  
| `download`           | Download a file from a URL.                               | `easywindows download <URL>`                   |  
| `create_directory`   | Create a new directory.                                   | `easywindows create_directory MyFolder`        |  
| `list_directory`     | List contents of a directory (default: current directory).| `easywindows list_directory`                   |  
| `move_file`          | Move a file to a new location.                            | `easywindows move_file source.txt dest/`       |  
| `rename_file`        | Rename a file or directory.                               | `easywindows rename_file old_name new_name`    |  
| `delete_file`        | Delete a file.                                            | `easywindows delete_file myfile.txt`           |  
| `ping`               | Ping a host to check connectivity.                       | `easywindows ping google.com`                  |  
| `open_program`       | Open a program by its path.                               | `easywindows open_program C:\Path\To\app.exe`  |  
| `system_info`        | Display system information.                               | `easywindows system_info`                      |  
| `shutdown`           | Shut down the system.                                     | `easywindows shutdown`                         |  
| `restart`            | Restart the system.                                       | `easywindows restart`                          |  
| `refresh`            | Refresh (restart) a process.                             | `easywindows refresh chrome.exe`               |  
| `ip grab`            | Log the IP of anyone visiting a Serveo URL.              | `easywindows ip grab localhost`               |  

---

## Contributing  

Contributions are welcome! If you’d like to add new features or improve existing ones:  
1. Fork the repository.  
2. Create a feature branch.  
3. Submit a pull request with a detailed description of your changes.  

---

## License  

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  

---

## Roadmap  

- Add additional network utilities.  
- Create a packaged executable for direct use without Python.  
- Develop an intuitive GUI for users who prefer a visual interface.  

---

## Support  

If you encounter any issues or have suggestions, please [open an issue](https://github.com/yourusername/easywindows/issues).  

---
