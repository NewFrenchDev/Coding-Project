import os

from dotenv import load_dotenv

from my_first_bot import RobotCop
from response import Response

load_dotenv(dotenv_path="config")

if __name__=="__main__":
    
    responses = Response()
    robotcop = RobotCop(responses.get_dict_response())
    robotcop.run(os.getenv("TOKEN"))