import json

class Response():
    def __init__(self):
        self.dict_responses = {}
        self.set_bot_response()

    def set_bot_response(self):
        with open("./data/bot.json", encoding="utf-8") as f:
             self.dict_responses = json.load(f)

    def get_dict_response(self):
        return self.dict_responses
