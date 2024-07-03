import requests
import math

def fetch_all_records():
    base_url = "https://jsonmock.hackerrank.com/api/medical_records"
    response = requests.get(base_url)
    print(response)
    response_data = response.json()

    total_pages = response_data['total_pages']
    all_records = response_data['data']
    for page in range(2, total_pages + 1):
        response = requests.get(f"{base_url}?page={page}")
        page_data = response.json()
        all_records.extend(page_data['data'])

    return all_records

def filter_records(records, diagnosis_name, doctor_id):
    return [
        record for record in records
        if record['diagnosis']['name'] == diagnosis_name and
           record['doctor']['id'] == doctor_id
    ]

def calculate_average_pulse(records):
    if not records:
        return 0

    total_pulse = sum(record['vitals']['pulse'] for record in records)
    average_pulse = total_pulse / len(records)
    return math.trunc(average_pulse)

def get_average_pulse_rate(diagnosis_name, doctor_id):
    all_records = fetch_all_records()
    relevant_records = filter_records(all_records, diagnosis_name, doctor_id)
    return calculate_average_pulse(relevant_records)


if __name__ == "__main__":
    diagnosis_name = "Pleurisy"
    doctor_id = 2
    average_pulse_rate = get_average_pulse_rate(diagnosis_name, doctor_id)
    print(average_pulse_rate)
