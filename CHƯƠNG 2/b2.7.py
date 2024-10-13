import json
def json_to_python(json_data):
    try:
        python_obj = json.loads(json_data)
        return python_obj
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None
if __name__ == "__main__":
    json_data = '{"name": "Peter", "age": 23, "city": "England"}'
    python_object = json_to_python(json_data)
    if python_object is not None:
        print("Đối tượng Python sau khi chuyển đổi:")
        print(python_object)