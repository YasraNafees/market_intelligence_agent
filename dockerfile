# 1. Base Image: Humne Python 3.10 mangi (Halka version)
FROM python:3.10-slim

# 2. Work Directory: Container ke andar 'app' ka folder banaya
WORKDIR /app

# 3. Copy Requirements: Pehle list copy ki taake installation fast ho
COPY requirements.txt .

# 4. Install Libraries: Sari libraries box mein dal di
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy Everything: Ab apna 'engin.py' aur 'app_ui.py' andar dala
COPY . .

# 6. Port: Streamlit hamesha 8501 par chalta hai
EXPOSE 8501

# 7. Start Command: Jab Render box kholay to ye command chale
CMD ["streamlit", "run", "app_ui.py", "--server.port=8501", "--server.address=0.0.0.0"]
