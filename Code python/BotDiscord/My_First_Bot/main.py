#python 3.7.9
import os

from dotenv import load_dotenv

from my_first_bot import RobotCop
from response import Response

load_dotenv(dotenv_path="config")

responses = Response()
robotcop = RobotCop(responses.get_dict_response())

extensions = ["cogs.greetings", "cogs.CommandEvents"]

if __name__=="__main__":

    for ext in extensions:
        robotcop.load_extension(ext)

    robotcop.run(os.getenv("TOKEN"))