# Excel Utility Suite

This project is a modular Python application with a graphical user interface (GUI) for performing various operations on Excel files. It supports tasks such as filtering logs, converting formats, applying color coding, and generating visual graphs from `.xlsx` files. The tool is designed to streamline log parsing and data analysis workflows.

Overview:
The application is composed of several Python scripts:

- `Excelgui.py`: Main GUI to select Excel files and access functionalities.
- `filterfile.py`: Filters Excel rows based on specific keywords or patterns.
- `convert.py`: Converts Excel data to a custom pipe-separated format.
- `colourcoding.py`: Applies color formatting based on content (e.g., error/warning detection).
- `showgraph.py`: Plots graphs from Excel data using `matplotlib`.
- `newexcel.py`: Helper for creating and writing to Excel files programmatically.

Features:
- GUI-based file selection and operation menu
- Keyword-based filtering of logs
- Custom Excel-to-text conversion
- Conditional formatting of Excel sheets
- Graph generation from structured Excel data
- Simple modular structure for easy maintenance and extension


Prerequisites:
- Python 3.x
- tkinter
- csv
- pandas

Running the Application:
1. Clone the repository or download the folder
2. Navigate to the directory in your terminal.
3. Run the script using Python
