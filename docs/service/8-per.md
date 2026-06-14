# Dịch vụ nhân vật (persona service)

Mục đích:
chịu trách nhiệm quản lý
hệ thống nhân vật, kho giọng đọc (Voices), các nền tảng tổng hợp giọng nói (TTS Engines)
và xử lý trực tiếp các yêu cầu
chuyển đổi văn bản thành âm thanh (Text-to-Speech).

![alt text](images/persona-swagger.png)

Truy xuất danh sách nhân vật:
Cung cấp danh sách các nhân vật, hỗ trợ phân trang
và cho phép lọc theo persona_id.

Quản lý nhân vật (dành cho quản trị viên ADMIN):
Tạo mới, cập nhật thông tin
hoặc xóa bỏ các nhân vật khỏi hệ thống.

Tải lên file ảnh đại diện avatar
và file âm thanh câu chào mẫu cho từng nhân vật.

Quản lý nền tảng (engines):
cho phép quản trị viên ADMIN
định nghĩa, cập nhật, xóa
và lấy danh sách các nền tảng dịch vụ cung cấp TTS.

Quản lý giọng đọc (voices):
tạo, cập nhật, xóa
và truy xuất danh sách
các giọng đọc cụ thể, cho phép lọc theo nền tảng.

Đồng bộ elevenlabs:
tích hợp tính năng đồng bộ elevenlabs
để cập nhật danh sách giọng đọc mới nhất trực tiếp
từ nhà cung cấp elevenlabs về hệ thống cơ sở dữ liệu.

Cung cấp chức năng tạo ra âm thanh từ văn bản đầu vào với edge_tts và piper_tts.

Với piper_tts cần file mô hình  được lưu tại R2 và được tải xuống khi bắt đầu khởi động dịch vụ

Dữ liệu file mẫu âm thanh audio, hình ảnh images, mô hình  models được lưu tại R2

![alt text](images/r2per.png)

![alt text](images/persona-database-migration.png)

![alt text](images/persona-database.png)
