![image](https://github.com/tientruongwork/E7RefreshShopTool/assets/99798487/cddcf4cf-db9f-438a-9d1b-f4c2e9ab4e29)# E7RefreshShopTool

## Overview
- This tool use to automate refresh shop action in EpicSeven (mobile game)
- Default bought item: **Covenant Bookmarks** and **Mystic Medals**

## Limitation
- Only support BlueStacks at the moment
- Only support Windows OS at the moment
- Only works when moved BlueStack to primary monitor (incase you're using multiple monitor)

## Installation
- Download this repo and extract it
- Go to `installation` folder
- Run `download_application.bat` file
- After application are downloaded, check if there's `python_installation.exe` and `tesseract-ocr_installation.exe`

### 1. Install Python:
- Double click on `python_installation.exe`
- Check on **Add python.exe to PATH** checkbox
- Click on `Install Now` then wait for the installation is success

### 2. Install Tesseract-OCR:
- Double click on `tesseract-ocr_installation.exe`
- **Leave everything as default**
- Click `Next` until the installation is sucess

### 3. Install python library
- Double click on `install_packages.bat`
- Wait for the process is success


## How to use
### 1. Make sure application name is corrects:
- Go to `scripts/config.py`
- Update application name which equals to your LD player application name
![Screenshot 2024-01-13 111358](https://github.com/tientruongwork/E7RefreshShopTool/assets/99798487/c0658ddc-9586-4ffb-939b-243f60ea6388)

### 2. Setup coordinates:
- Double click on `setup_coordinates.bat`. Then it'll asked for 4 action
- *Q1. "Hover to "Refresh" button then hit Enter:*
![image](https://user-images.githubusercontent.com/99798487/226973885-88b23ab5-b806-4477-9f68-a83608496f93.png)
- *Q2. "Click on "Refresh" button, hover to "Confirm" button then hit Enter*
![image](https://user-images.githubusercontent.com/99798487/226974083-290a8488-d04a-4cc2-a651-07b9353926e9.png)
- *Q3. "Click on "Buy" button on any item, hover to "Buy" button then hit Enter*
![image](https://user-images.githubusercontent.com/99798487/226974347-42599d13-3269-4591-92de-ac487839a309.png)
- *Q4. "Hover to the blank space between item name and price, then hit Enter"*
![image](https://user-images.githubusercontent.com/99798487/226974612-1945891d-fa27-4bc1-91ea-55f5f05551aa.png)

### 3. Start automate scripts:
- Right click on `start.bat`
- Click on `Run as Administrator`
- Input the refresh times you want then hit Enter
- Enjoy !

## Execution time:
100 refresh ~ 12mins

## Give me a star if you like it :P
