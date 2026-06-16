# รับค่าเงินเดือนจากผู้ใช้
salary = float(input("กรุณากรอกเงินเดือน: "))

# คำนวณภาษี 3%
tax = salary * 0.03

# คำนวณเงินคงเหลือ
net_salary = salary - tax

# แสดงผล
print(f"ภาษีที่ต้องจ่าย: {tax:.2f} บาท")
print(f"เงินเดือนสุทธิ: {net_salary:.2f} บาท")
