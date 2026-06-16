# รับค่าน้ำหนักและส่วนสูง
weight = float(input("กรุณากรอกน้ำหนัก (กิโลกรัม): "))
height_cm = float(input("กรุณากรอกส่วนสูง (เซนติเมตร): "))

# แปลงเซนติเมตรเป็นเมตร
height_m = height_cm / 100

# คำนวณ BMI
bmi = weight / (height_m ** 2)

# แปลผลสุขภาพ
if bmi < 18.5:
    result = "น้ำหนักน้อย"
elif bmi < 23:
    result = "น้ำหนักปกติ"
elif bmi < 25:
    result = "น้ำหนักเกิน"
elif bmi < 30:
    result = "โรคอ้วนระดับ 1"
else:
    result = "โรคอ้วนระดับ 2"

# แสดงผล
print(f"\nค่า BMI = {bmi:.2f}")
print(f"ผลการประเมิน: {result}")
