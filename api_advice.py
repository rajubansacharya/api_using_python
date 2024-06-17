import requests

def advice():
    url = "https://api.adviceslip.com/advice"
    all_data =requests.get(url)
    stored_data = all_data.json()

    advice = stored_data["slip"]["advice"]
    return advice

def main():
    try:
        x = advice()
        print(f"The advice of the day is: \n {x}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()