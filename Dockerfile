FROM python:3.11.4
WORKDIR /usr/src/myapp
# Copy requirements and install them
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
# Copy the rest of your app
COPY . .
CMD ["python", "scripts/demo/initalize_demo.py; python run.py"]

