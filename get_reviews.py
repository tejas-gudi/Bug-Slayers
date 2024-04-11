import requests
import json
def get_reviews():
    url = "https://data.g2.com/api/v1/survey-responses"
    headers = {
        "Authorization": "Token token=0d288768e7bfad85b03736685628f7aea153669d68dd0c4844bb0768bf70f0cd",
        "Content-Type": "application/vnd.api+json"
    }
    params = {
        "filters[product_name]": "G2 Marketing Solutions",
        "page[size]": "100"
    }
    responses = []
    while True:
        response = requests.get(url, headers=headers, params=params)
        print(response.status_code)
        if response.status_code == 200:
            data = response.json()
            responses.extend(data["data"])
            if "next" in data["links"]:
                url = data["links"]["next"]
            else:
                break
        else:
            print("Error:", response.status_code)
            break
    return responses

def main():
    response = get_reviews()
    with open("./reviews.json", "w") as file:
        json.dump(response, file)
main()
