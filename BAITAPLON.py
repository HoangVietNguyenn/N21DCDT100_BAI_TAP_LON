def them_tu(tu_dien):
    tu_moi = input("Nhập từ mới: ")
    nghia = []
    while True:
        loai_tu = input("Nhập loại từ (danh từ, động từ, tính từ, trạng từ, v.v.): ")
        y_nghia = input("Nhập nghĩa: ")
        vi_du = input("Nhập ví dụ: ")
        nghia.append({"loai_tu": loai_tu, "nghia": y_nghia, "vi_du": vi_du})
        break
    tu_dien.append({"từ": tu_moi, "nghia": nghia})
    print(f"Từ '{tu_moi}' đã được thêm vào từ điển.")

def xoa_tu(tu_dien):
    tu_can_xoa = input("Nhập từ cần xóa: ")
    for muc in tu_dien:
        if muc["từ"] == tu_can_xoa:
            tu_dien.remove(muc)
            print(f"Từ '{tu_can_xoa}' đã được xóa khỏi từ điển.")
            return
    print(f"Từ '{tu_can_xoa}' không tồn tại trong từ điển.")

def tra_cuu(tu_dien):
    tu_can_tra_cuu = input("Nhập từ cần tra cứu: ")
    for muc_tu in tu_dien:
        if muc_tu["từ"] == tu_can_tra_cuu:
            print(f"Nghĩa của từ '{tu_can_tra_cuu} là':")
            for nghia in muc_tu["nghia"]:
                print(f" - Loại từ: {nghia['loai_tu']}")
                print(f" - Nghĩa: {nghia['nghia']}")
                print(f" - Ví dụ: {nghia['vi_du']}")
            return
    print(f"Từ '{tu_can_tra_cuu}' không tồn tại trong từ điển.")

def luu_tu_dien(tu_dien, filename):
    with open(filename, "w") as file:
        for tu in tu_dien:
            file.write(f"{tu['từ']} -")
            for nghia in tu['nghia']:
                file.write(f"word type {nghia['loai_tu']},Mean {nghia['nghia']},Example {nghia['vi_du']}; \n")
            file.write('\n')

def tai_tu_dien(filename):
    tu_dien = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split("-")
                if len(parts) >= 2:  # Kiểm tra xem có đủ phần tử sau khi tách dấu -
                    tu_info = parts[0].strip()
                    nghia_info = parts[1].strip().split(",")
                    if len(nghia_info) >= 3:  # Kiểm tra xem có đủ phần tử sau khi tách dấu phẩy không
                        loai_tu = nghia_info[0].split("word type")[1].strip()        # Lấy ví dụ sau từ "word type"
                        nghia = nghia_info[1].split("Mean")[1].strip()                 # Lấy ví dụ sau từ "Mean"
                        vi_du = nghia_info[2].split("Example")[1].strip().strip(";")  # Lấy ví dụ sau  từ "Example" và loại bỏ dấu chấm phẩy cuối cùng
                        tu_dien.append({"từ": tu_info, "nghia": [{"loai_tu": loai_tu, "nghia": nghia, "vi_du": vi_du}]})
                else:
                    print(f"Dòng không đúng định dạng: {line}")
    return tu_dien

def hien_thi_menu():
    print("\nMenu:")
    print("1. Thêm một từ mới vào từ điển")
    print("2. Xóa một từ khỏi từ điển")
    print("3. Tra cứu nghĩa của một từ trong từ điển")
    print("4. Lưu từ điển vào tập tin")
    print("5. Tải từ điển từ tập tin")
    print("6. Thoát chương trình")

def main():
    tu_dien = []
    while True:
        hien_thi_menu()
        lua_chon = input("Nhập lựa chọn của bạn : ")
        if lua_chon == "1":
            them_tu(tu_dien)
        elif lua_chon == "2":
            xoa_tu(tu_dien)
        elif lua_chon == "3":
            tra_cuu(tu_dien)
        elif lua_chon == "4":
            filename = input("Nhập tên tập tin để lưu từ điển: ")
            luu_tu_dien(tu_dien, filename)
            print(f"Từ điển đã được lưu vào {filename}")
        elif lua_chon == "5":
            filename = input("Nhập tên tập tin để nạp từ điển: ")
            tu_dien = tai_tu_dien(filename)
            print(f"Từ điển đã được tải từ {filename}")
        elif lua_chon == "6":
            print("Đang thoát chương trình...")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập một số từ 1 đến 6.")

if __name__ == "__main__":
    main()
