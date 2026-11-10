FROM python:3.12-slim
WORKDIR /app
COPY r.txt . 
RUN pip install -r r.txt    
COPY . . 
EXPOSE 5000
CMD ["python", "app.py"]