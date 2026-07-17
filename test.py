print("heleo")
def chao_buoi_sang():
    print("Chào buổi sáng!") # Đây là callback
def lam_gi_do(hanh_dong):
    print("Bắt đầu làm việc...")
    hanh_dong()  # Bạn đặt lời gọi ở đâu, nó chạy đúng ở vị trí đó
    print("Làm việc xong!")
lam_gi_do(chao_buoi_sang)
