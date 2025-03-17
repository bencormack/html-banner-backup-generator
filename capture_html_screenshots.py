import os
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image

def capture_screenshot(html_path):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    file_url = "file://" + os.path.abspath(html_path)
    driver.get(file_url)
    
    time.sleep(10)
    
    try:
        main_container = driver.find_element(By.ID, "mainContainer")
        driver.execute_script("arguments[0].style.transform='scale(0.5)'; arguments[0].style.transformOrigin='top left';", main_container)
        
        time.sleep(1)
        
        location = main_container.location
        size = main_container.size
        
        driver.set_window_size(int(size['width'] * 0.5), int(size['height']))
        
        screenshot_path = os.path.join(os.path.dirname(html_path), "backup.jpg")
        driver.save_screenshot(screenshot_path)
        
        image = Image.open(screenshot_path)
        cropped_image = image.crop((
            int(location['x'] * 0.5), 
            int(location['y'] * 0.5), 
            int(location['x'] + size['width']), 
            int(location['y'] + size['height'])
        ))
        
        quality = 85
        cropped_image.save(screenshot_path, "JPEG", quality=quality, optimize=True)
        
        while os.path.getsize(screenshot_path) > 40 * 1024:
            quality -= 5
            cropped_image.save(screenshot_path, "JPEG", quality=quality, optimize=True)
            if quality <= 10:
                break
        
        print(f"Screenshot saved: {screenshot_path} (Quality: {quality})")
    except Exception as e:
        print(f"Error capturing {html_path}: {e}")
    
    driver.quit()

def find_html_files(directory):
    html_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
    return html_files

directory = os.getcwd()
html_files = find_html_files(directory)
if not html_files:
    print("No HTML files found.")
    exit(1)

for html_file in html_files:
    capture_screenshot(html_file)

print("Screenshots saved as 'backup.jpg' in respective directories.")
