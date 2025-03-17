# html-banner-backup-generator
A Python script automates the process of capturing JPEG backups of HTML banner ads. It recursively scans the working directory for HTML files, loads them in a headless Chrome browser, and captures a scaled-down screenshot of the `#mainContainer` element, saving it as `backup.jpg` in the same directory as the original HTML file. The script also optimizes the JPEG to ensure the file size does not exceed 40KB.

## Prerequisites

Before using this script, ensure you have the following installed:

- **Python 3.8+** (recommended)
- **Google Chrome** (latest version)
- **Chromedriver** (handled automatically by `webdriver_manager`)
- **Required Python packages**:
  - `selenium`
  - `webdriver_manager`
  - `Pillow`
  - `pyautogui`

You can install the dependencies using:

```sh
pip install selenium webdriver-manager Pillow pyautogui
```

## How It Works

1. The script searches for all `.html` files in the current directory and its subdirectories.
2. It opens each HTML file in a headless Chrome browser.
3. It waits 10 seconds for animations or dynamic content to load.
4. It locates the `#mainContainer` element and applies a `0.5x` scale transformation.
5. It captures a screenshot, crops it to fit the banner ad, and saves it as `backup.jpg`.
6. It optimizes the JPEG quality to keep the file size below **40KB**.
7. If no HTML files are found, the script exits with a message.

## Usage

To run the script, simply execute:

```sh
python script.py
```

This will process all HTML files in the current working directory and save their respective `backup.jpg` images.

## Notes

- The script assumes the banner ad is inside an element with `id="mainContainer"`. If your banners use a different container, modify the `driver.find_element(By.ID, "mainContainer")` line accordingly.
- The script waits **10 seconds** before capturing the screenshot to allow for animations or dynamic content to load. Adjust the `time.sleep(10)` line if needed.
- If the final JPEG file size exceeds 40KB, the script progressively reduces the quality down to a minimum of 10%.

## Troubleshooting

- **Chrome/Webdriver issues**: Ensure Chrome is installed and up to date. If you encounter webdriver errors, try manually updating chromedriver:
  
  ```sh
  pip install --upgrade webdriver-manager
  ```
  
- **No HTML files found**: Ensure you are running the script in the correct directory where your HTML banners are stored.
- **Images not cropping correctly**: Check that `#mainContainer` exists in your HTML and is correctly positioned.

## License

This script is provided "as is" without any warranties. Feel free to modify and adapt it for your use case.

