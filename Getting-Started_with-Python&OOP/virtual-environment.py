'''in python when we run different project on our system. Then we have to install all the versions that 
particular project uses 
Create virtual environment on your system using: python -m venv venv
then: venv\Scripts\activate
write this to get inside the environment then
run this command it will install all the requirements 
needed to run the project: pip install -r requirements.txt
'''
import pandas as pd
print(pd.__version__)