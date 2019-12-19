python -m venv --copies venv
virtualenv venv
venv\Scripts\activate & pip3 install --requirement requirements.txt & pytest & python sew_ek_analog_digital_uhr.py & deactivate & virtualenv --relocatable --always-copy venv