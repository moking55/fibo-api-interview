# Fibonacci API

# ฟีเจอร์
- สามารถคำนวณลำดับ Fibonacci ได้
- การตรวจสอบอินพุตเพื่อให้แน่ใจว่าตัวเลขเป็นค่าบวกและอยู่ในช่วงที่กำหนด
- มีเอกสาร API สำหรับการทดสอบด้วย Swagger UI

# การติดตั้ง
1. ดาวน์โหลดโปรเจคนี้
```bash
git clone https://github.com/moking55/fibo-api-interview.git
```
2. ติดตั้ง dependencies ด้วย pip
```bash
pip install -r requirements.txt
```
3. รันโปรแกรม
```bash
uvicorn main:app --reload
```
4. เข้าถึง API ได้ที่ http://localhost:8000/api/v1/fibo/{number}


Swagger UI: http://localhost:8000/api/docs

ReDoc: http://localhost:8000/api/redoc