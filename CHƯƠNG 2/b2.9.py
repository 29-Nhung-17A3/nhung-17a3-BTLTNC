import json
if __name__ == "__main__":
    python_dict = {
        "name": "Peter",
        "age": 23,
        "city": "England",
        "is_student": False,
        "grades": [95, 89, 78]
    }
    json_string = json.dumps(python_dict, indent=4, sort_keys=True)
    print(f"Chuỗi JSON sau khi chuyển đổi:\n{json_string}")