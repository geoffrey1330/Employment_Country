# employment-global

Global Employment statistical dataset of individuals base on their Sex, Industry and Country where they work. Data are sourced from International Labour Organization.

## Data

### Sources

1. 
    * Name: Employment by Industry by Country. International Labour Organization Statistical dataset (ILOSTAT)
    * gdrive: https://docs.google.com/spreadsheets/d/1QvbKTaxOgB0Sdb09MNRDpIiiPWqsnmiVpwH7mCAfue4/edit?usp=sharing

## Getting Started
To use this project locally [python](https://www.python.org/downloads/)  needs to be installed.

1. **Clone the repository:**
    ```
    git clone -b main https://github.com/geoffrey1330/employment-global.git
    ```
2. **Enter the project directory:**
    ```
    cd employment-global
    ```
3. **Setup the virtual environment by running:**
    ```
    virtualenv venv
    source venv/bin/activate 
    ```
    
4. **Install External Dependencies:**
    ```
    pip install -r requirements.txt
    ```
   
5. **Running the script**
    In the project root directory, run:
    ```
    python scripts/process.py
    ```
