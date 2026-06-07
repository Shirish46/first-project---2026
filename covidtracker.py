# making a covid app tracker app
# importing the requests to call APIs (to extract data from internet)

import requests   #library to send requests to websites
import json      #library to work with JSON data types




# functions to get covid data for any specific country
def get_covid_data(country):
    #API url with country name
    url = f"https://disease.sh/v3/covid-19/countries/{country}"

    # Send GET request
    response = requests.get(url)
    # check if the request was successful (i.e. status code = 200)
    print("Status Code:",response.status_code)

    if response.status_code != 200:
        print("Country Not Found")
        return  #exit the function

# converting API response (JSON) to python dictionary


    data = response.json()

    
    #print raw JSON data in a readable format
    print("\n RAW JSON:")
    print(json.dumps(data, indent=4))

    # save JSON data into a file called covid_data.json
    # 'w' means write mode which overwrites file each time
    with open("covid_data.json", "w") as f:
        json.dump(data, f, indent=4)

    print("\n COVID-19 Stats")

    #show country name, total confirmed cases,currently infected people,recovered cases and deaths
    print(f"Country : {data['country']}")

    print(f"Total Cases : {data['cases']}")

    print(f"Active Cases : {data['cases']}")

    print(f"Recovered : {data['recovered']}")

    print(f"Deaths : {data['deaths']}")


#infinite loop (allows user to check multiple times)
while True:

    country = input("\nEnter the country name (or type 'exit'): ")
    #if the uses types 'exit', stop the program
    if country.lower() == "exit":
        print("Goodbye")
        break

    get_covid_data(country)



    
    


    



    




   



