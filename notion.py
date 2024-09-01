import time
import json
from playwright.sync_api import sync_playwright


emails = [
    "random1@example.com", "random2@example.com", "random3example.com"
     "random4@example.com", "random5@example.com", "random6@example.com",
     "random7@example.com", "random8@example.com", "random9@example.com",
     "random10@example.com", "random11@example.com", "random12@example.com",
     "random13@example.com", "random14@example.com", "random15@example.com",
     "random16@example.com", "random17@example.com", "random18@example.com", 
     "random19@example.com", "random20@example.com", "random21@example.com",
     "random22@example.com", "random23@example.com", "random24@example.com",
     "random25@example.com"
]

processed_emails = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()


    def handle_request_finished(request):
        
        
        if "api/v3/createEmailUser" in request.url:
            try:
                
                print(f"Request URL: {request.url}")

                post_data = request.post_data
                print(f"Post data: {post_data}")
                
                payload = json.loads(post_data)
                print(f"Payload: {payload}")
                if isinstance(payload, dict):
                    email = payload.get("email")  
                    print(email)
                
                    if email:
                      processed_emails.append(email)
                      print(True)
                    
                      with open("invited_emails.json", "w") as f:
                         json.dump(processed_emails, f, indent=4)
                         print(True)
            except Exception as e:
                print(f"Error processing request: {e}")
    
    page.on("requestfinished", handle_request_finished)

    page.goto("https://www.notion.so/login")

    # Manual Login due to login issues for me.
     
    page.wait_for_url("https://www.notion.so/Getting-Started-ef3f331586b04d829d4965519788300c")

    time.sleep(5)
    
    page.click("body > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > nav:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(5) > div:nth-child(1) > div:nth-child(2)")
    

    for email in emails:
        
        page.click("body > div:nth-child(5) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)")
        
        time.sleep(5)

        page.fill("input[placeholder='Search name or emails']", email)

        time.sleep(2)
        
        page.click("div[class='notion-invite'] div[class='notion-scroller vertical horizontal'] div div:nth-child(2)")  
        
        page.wait_for_timeout(2000) 

    print(processed_emails)

    
    browser.close()

