import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.edge.service import Service
import os
from datetime import date


# Step 1: Send a request to the website
url = 'https://www.nutritics.com/menu/ma4080'
response = requests.get(url)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Find the menu items
def findWebsites(firstinput):
    n = 0
    firstList = []
    menu_items = soup.find_all('div', class_='menu')
    for item in menu_items:
        title_element = item.find('span', class_='title')
        if title_element:
            title = title_element.get_text(strip=True)
            if firstinput in title:
                n = n + 1
                # Extract the 'onclick' attribute from the matching item
                onclick_attr = item.get('onclick')
                if onclick_attr:
                    # Use regex to extract the URL from the 'onclick' attribute
                    match = re.search(r"location\.href='([^']+)'", onclick_attr)
                    if match:
                        relative_link = match.group(1)
                        full_link = f"https://www.nutritics.com{relative_link}"  # Complete the relative URL
                        firstList.append(f'Title: {title}, Link: {full_link}')
    if firstList == []:
        print("I'm sorry, there is no data for this date...")
        link = "None"
        return link
                        
    if n > 1:
        
        while True:
            mealTime = input("Which meal do you want? Type 'B' for Breakfast, 'L' for Lunch, 'D' for Dinner: ")
            if mealTime == 'B' or mealTime == 'L':
                uppermealTime = " Br" 
                lowerMealTime = " br"
                break  # Exit the loop if input is valid
            elif mealTime == 'D':
                uppermealTime = " Di" 
                lowerMealTime = " di"
                break  # Exit the loop if input is valid
            else:
                print("Invalid input, please try again.")



        for entry in firstList:
            if uppermealTime in entry:  # Check if mealTime is in the formatted list item  # Print the matching entry (title + link)
                link = re.search(r'https?://\S+', entry).group()
                return link
            elif lowerMealTime in entry:  # Check if mealTime is in the formatted list item  # Print the matching entry (title + link)
                link = re.search(r'https?://\S+', entry).group()
                return link
            else:
                print("I'm sorry, there is no data for that specified meal.")



def findFood(link):
    if link == "None":
        return None
    else:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Use the correct class without extra spaces
        menu_items = soup.find_all('span', class_='name')  # Corrected class attribute
        printed_items = set()

        for item in menu_items:
            item_text = item.text.replace("- 1 Serving", "").strip()
            if item_text not in printed_items:
                print(item_text)
                printed_items.add(item_text)




def convert_to_month_day(): 


    today = date.today()

# Format as 'Month Day'
    formatted_date = today.strftime("%B %-d")   
    
    # Return the formatted string
    return formatted_date




firstinput = convert_to_month_day() # Example input
link = findWebsites(firstinput)
findFood(link)


