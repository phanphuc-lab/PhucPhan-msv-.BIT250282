data = {}
n = int(input("nhập số người:"))
for i in range(n):
    ten = input(f"Nhập tên người thứ {i+1}: ")
    tuoi = int(input(f"Nhập tuổi của {ten}: "))
    data[ten] = tuoi
if data:
    trung_binh = sum(data.values()) / len(data)
    print(f"Danh sách đã lưu: {data}")
    print(f"Tuổi trung bình là: {trung_binh:.2f}")
else:
    print("Danh sách trống")
