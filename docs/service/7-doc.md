# Dịch vụ văn bản (document service)

Mục đích:
tiếp nhận, lưu trữ và quản lý luồng xử lý tài liệu
của người dùng.
Dịch vụ này không chỉ lưu trữ file
mà còn hỗ trợ quy trình
trích xuất nội dung thành định dạng
Markdown, tạo bản tóm tắt
và vector hóa tài liệu.

![alt text](images/document-swagger.png)

Tải lên tài liệu mới: người dùng gửi file tài liệu lên hệ thống. Sau khi tiếp nhận thành công, hệ thống sẽ trả về mã định danh duy nhất (doc_id), tên file gốc và trạng thái khởi tạo ban đầu để đưa vào hàng đợi xử lý.

Dựa vào doc_id, người dùng có thể truy xuất trạng thái xử lý hiện tại của tài liệu.
Hệ thống sẽ báo cáo chi tiết về sự tồn tại của các thành phần dữ liệu thông qua các cờ trạng thái:
has_file, has_content, has_summary.

Trong trường hợp quá trình bóc tách hoặc tóm tắt gặp sự cố, hệ thống cung cấp một API chuyên biệt để kích hoạt lại quy trình xử lý cho tài liệu đó mà không cần phải upload lại file gốc.

<!-- Nếu từ cùng 1 người dùng tải lên 1 file => sao chép quá trình -->

x: Nhận thông tin sự kiện thanh toán thành công kafka

Chức năng này chỉ dành cho người dùng VIP
x: Kiểm tra người dùng hiện tại có phải người dùng VIP?

Chỉ cần tải lên file

Dùng cloudflare R2 lưu file người dùng

Dùng docling để trích xuất thông tin file người dùng

Công việc sau đó được xử lý ngầm:

Tóm tắt nội dung file

Vector hóa file với RAG và lưu vào qdrant

<!-- RabbitMQ -->
<!-- Vẽ  Hướng dẫn Mermaid tạo sơ đồ  -->

![alt text](images/r233333.png)

![alt text](images/r2summmmmm.png)

![alt text](images/document-database-migration.png)

![alt text](images/document-database.png)
