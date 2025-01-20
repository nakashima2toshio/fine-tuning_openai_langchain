import os
import json


class ReadWriteFile:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_from_json_file(self):
        try:
            with open(self.file_path, 'r') as fp:
                return json.load(fp)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error while reading from JSON file: {str(e)}")
            return None

    def read_file(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as fp:
                return fp.read()
        except FileNotFoundError as e:
            print(f"Error while reading from file: {str(e)}")
            return None

    def write_file(self, content):
        try:
            with open(self.file_path, 'w') as fp:
                fp.write(content)
        except Exception as e:
            print(f"Error while writing to file: {str(e)}")

    def write_to_json_file(self, content):
        try:
            with open(self.file_path, 'w') as fp:
                json.dump(content, fp)
        except Exception as e:
            print(f"Error while writing to JSON file: {str(e)}")

    def append_to_file(self, content):
        try:
            with open(self.file_path, 'a') as fp:
                fp.write(content)
        except Exception as e:
            print(f"Error while appending to file: {str(e)}")
