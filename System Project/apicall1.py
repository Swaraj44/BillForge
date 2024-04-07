import requests as rq

def cur2bangla(ss):
    Base_url = 'http://swaraj66.pythonanywhere.com/'
    payload = {'input': ss}
    
    try:
        response = rq.get(Base_url, params=payload)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
        
        json_value = response.json()
        rq_input1 = json_value['input']
        rq_input2 = json_value['convert']

        return rq_input2
    except rq.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return None  # You can choose how to handle the error in your specific case
