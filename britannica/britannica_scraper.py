import json
import os
import requests

url = "https://api.minexa.ai/scraper/"
api_key = "YOUR_API_KEY"

# Your JSON data for the request body
data = {
    # Copy paste the data from the website directly without any modification to train the scraper
    # or Write a short description of your required data, for example: "clinical trials results"
    "look_for": """technology
technology, the application of scientific knowledge to the practical aims of human life—or, as it is sometimes phrased, to the change and manipulation of the human environment. The word technology is a combination of the Greek technē, which means “art, craft,” and logos, which means “word, speech.” ...

History of technology
History of technology, the development over time of systematic techniques for making and doing things. ...

Automation
Automation, application of machines to tasks once performed by human beings or, increasingly, to tasks that would otherwise be impossible. ...

Massachusetts Institute of Technology (MIT) (university, Cambridge, Massachusetts, United States)
Massachusetts Institute of Technology, privately controlled coeducational institution of higher learning known for scientific and technical research. ...

Virtual reality (VR) (computer science)
Virtual reality (VR), the use of computer modeling and simulation that enables a person to interact with an artificial three-dimensional (3-D) visual or ...

Technology of photography
Technology of photography, equipment, techniques, and processes used in the production of photographs. In its simplest form, the camera is a light-tight ...

Artificial intelligence (AI)
Technology Computers. artificial intelligence. Actions. Cite. Share. Give Feedback. External Websites. Also known as: AI. Written by. B.J. Copeland. Professor ...

Robot (technology)
Adept Technology, Inc., spun off from Stanford and Unimation to make electric arms, is the only remaining American firm. Foreign licensees of ...

History of technology - Technological Dilemma, Innovation, Impact ...
Any technological stimulus can trigger a variety of social responses, depending on such unpredictable variables as differences between human personalities; ...

High-speed rail (train)
Technology ... Most high-speed rail lines use steel wheels that travel over steel rails, like conventional trains. Older turbo trains, used in ...""",

    # Provide a single url corresponding to pages with listed data
    "urls":
    [
    "https://britannica.com/search?query=Technology"
    ],

    # uncomment if you need to recrawl the HTML again from scratch by ignoring cached data (like its the first time you scrape it)
    #"reset": True,

    # Unocomment and set it when manaully detecting your container after first try
    # No need to use for creating scraper for a particular page for the first time
    # "xpath": "/html/body/div/div/div[3]/div[1]/div[2]",

    "mode": "list" #  Use list if the data you're scraping is in form of an itemized collection
}



headers = {
    "Content-Type": "application/json",
    "api-key": api_key
}

print("Creating scraper.. This may take up to 2 minutes")

# Make the POST request
response = requests.post(url, json=data, headers=headers)

# Print the response
if response.status_code == 200:
    print("Please confirm container is well located:", response.json()['response']['web_app'])

    # Create and save the file
    scraper_id = response.json()["response"]["id"]
    file_path = f"{os.path.dirname(os.path.abspath(__file__))}/scraper_id_{scraper_id}.json"

    # Save the scraper.json
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(response.json(), file, ensure_ascii=False, indent=4)

    print("Full scraper json saved at: {}".format(file_path))
else:
    print("Error status code {} occurred ".format(response.status_code))
    try:
        print(response.status_code)
        print(response.json())
    except Exception as e:
        print("{} in showing error".format(e))
