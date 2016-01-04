# mami-linda-cookbook

Some install notes
- clone repo
- mkvirtualenv cookbook -p `which python3`
- pip install -r requirements.txt
- generate secret_key.txt with secret-key-gen.py
- fix the registration import lines:
from django.contrib.sites.models import RequestSite
should be:
from django.contrib.sites.requests import RequestSite
