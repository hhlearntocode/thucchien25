import json
import os

def append_log(log_data):
    """
    Thêm log mới vào file logs/log.json
    Nếu file đã tồn tại, đọc logs cũ và thêm log mới vào
    Nếu chưa có, tạo file mới với log đầu tiên
    """
    os.makedirs("logs", exist_ok=True)
    log_file = "logs/log.json"
    
    # Đọc logs hiện có (nếu có)
    logs = []
    if os.path.exists(log_file):
        try:
            with open(log_file, "r", encoding="utf-8") as f:
                content = f.read().strip()
                if content:
                    # Kiểm tra xem file có phải là mảng hay object đơn
                    data = json.loads(content)
                    if isinstance(data, list):
                        logs = data
                    else:
                        # Nếu là object đơn, chuyển thành mảng
                        logs = [data]
        except json.JSONDecodeError:
            # Nếu file bị lỗi, bắt đầu mới
            logs = []
    
    # Thêm log mới
    logs.append(log_data)
    
    # Ghi lại toàn bộ logs
    with open(log_file, "w", encoding="utf-8") as f:
        f.write(json.dumps(logs, indent=4, ensure_ascii=False))

