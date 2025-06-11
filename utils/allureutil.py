import os
from datetime import datetime
import allure

def attach_screenshot(driver, name="screenshot", directory="screenshots"):
    try:
        # Create directory if it doesn't exist
        os.makedirs(directory, exist_ok=True)

        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"{name}_{timestamp}.png"
        screenshot_path = os.path.join(directory, screenshot_name)

        # Save screenshot
        driver.save_screenshot(screenshot_path)

        # Attach to Allure report
        with open(screenshot_path, "rb") as image_file:
            allure.attach(
                image_file.read(),
                name=name,
                attachment_type=allure.attachment_type.PNG
            )

        # Optional: log saved path
        print(f"Screenshot saved and attached: {screenshot_path}")

    except Exception as e:
        print(f"Failed to capture or attach screenshot: {e}")
