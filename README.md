
# Nonlinear Model Predictive Controller (NMPC) for Reactor System

This repository contains a Python script that implements a Nonlinear Model Predictive Controller (NMPC) for managing the temperature and concentration in a chemical reactor. The controller interacts with the APMonitor server to perform dynamic optimization and control over a series of time steps.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Files](#files)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Visual Studio Code (recommended, but not required)

### Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/jorshimayor/nmpc-controller.git
   cd nmpc-controller
   ```

2. **Install required Python packages**:

   In your terminal, run the following command to install the `apm` package:

   ```bash
   pip install apm
   ```

## Usage

1. **Open the project in VSCode**:

   - Launch Visual Studio Code.
   - Open the project folder (`nmpc-controller`) by selecting `File > Open Folder`.

2. **Run the script**:

   - Open the `nmpc_controller.py` file.
   - To run the script, press `F5` or click on the `Run` button in the top right corner of the editor.
   - Alternatively run the command in your termainal:

   ```bash
   python nmpc_controller.py
    ```

3. **Monitor the output**:

   - The script will print the temperature, concentration, and cooling temperature values to the terminal.
   - If a web viewer is enabled, the URL will be provided in the terminal output. You can open this in your browser to view real-time plots of the control process through this url "<https://byu.apmonitor.com/online/169.150.196.103_nmpc/169.150.196.103_nmpc_oper.htm>".

## Files

- `nmpc_controller.py`: The main Python script that runs the NMPC controller.
- `nmpc.apm`: The APMonitor model file containing the reactor equations and variables.
- `nmpc.csv`: The CSV file containing initial data for the model.

## Project Structure

```bash
nmpc-controller/
│
├── nmpc_controller.py   # Main script
├── nmpc.apm             # APMonitor model file
└── nmpc.csv             # Initial data file
```

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to submit a pull request. Please ensure that your changes are well-documented and include tests where applicable.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Reference

[Apm Monitor](https://github.com/APMonitor/apm_server/tree/master)
