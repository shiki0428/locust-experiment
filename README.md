



```

pyenv  install 3.9.13
pyenv local 3.9.13
python --version
Python 3.9.13

python -m venv venv
source venv/bin/activate

pip install -r requirement.txt 

uvicorn main:app  --reload 
locust -f test.py
```# locust-experiment
