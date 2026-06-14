# Dịch vụ trò chuyện (conversation service) và Dịch vụ chatbot (chatbot service)

Sơ đồ tổng quan về Dịch vụ trò chuyện (conversation service) và Dịch vụ chatbot (chatbot service)

![alt text](images/conversation-and-chatbot-overview.png)



![alt text](images/conversation-PR.png)
![alt text](images/conversation-lint.png)

![alt text](images/conversation-database-migration.png)
![alt text](images/conversation-database.png)

![alt text](images/chatbot-database-migration.png)
![alt text](images/chatbot-database.png)

![alt text](images/r2chat.png)

<!-- Chưa cần vì hết chức năng -->
<!-- x: Nhận thông tin sự kiện thanh toán thành công kafka -->
<!-- x: Nhận thông tin sự kiện thanh toán thành công kafka -->
<!-- x: Kiểm tra người dùng hiện tại có phải người dùng VIP? -->

Nhận POST chat id, text, và file (VIP) gửi vào ai python agentic bằng gRPC

Chức năng xóa DELETE chat bằng RabbitMQ

Chỉ lưu thông tin chat id khi nhận request của frontend

Quản lý việc lưu lại bookmark

Quản lý việc chia sẻ share

Xử lý chia sẻ Chat


Đây là phần quan trọng nhất của hệ thống, sử dụng langgraph tạo agentic ai phức tạp.

Chat => lưu cơ sở dữ liệu
Get ra
Xóa theo sự kiện của RabbitMQ

Thêm xử lý file cho người dùng VIP





<!-- Dịch vụ trò chuyện (conversation service)  -->

![alt text](images/conversation-swagger.png)


Mục đích:
chịu trách nhiệm quản lý
giao tiếp giữa người dùng
và hệ thống Agentic RAG.
Dịch vụ này xử lý trực tiếp
các cuộc trò chuyện văn bản
theo cơ chế streaming, cấp phát quyền truy cập cho luồng giao tiếp giọng nói, và cung cấp các tiện ích lưu trữ, chia sẻ trò chuyện.



bắt đầu một luồng trò chuyện mới.


cấp phát token trò chuyện giọng nói

xử lý tin nhắn   từ người dùng

xóa bỏ   một  cuộc trò chuyện    khỏi hệ thống.


Người dùng có thể tạo các thư mục lưu trữ


Cho phép Đánh dấu một  cuộc trò chuyện  và Ghi chú nội dung

Tạo ra một "bản snapshot" Chia sẻ cuộc trò chuyện

Cung cấp URL công khai có  shareId  và  token


Chủ sở hữu đoạn chat có thể xem danh sách các liên kết đã tạo   và   thu hồi quyền truy cập   bất cứ lúc nào.



<!-- Dịch vụ chatbot (chatbot service) -->

![alt text](images/chatbot-swagger.png)

Mục đích:
dùng các công nghệ AI
xử lý trao đổi với người dùng.
Sau đó lưu lại lịch sử trò chuyện và cung cấp các API
về  lịch sử các cuộc trò chuyện
và chi tiết thông tin suy luận, nguồn tài liệu của từng câu trả lời  của  cuộc trò chuyện.
Lắng nghe  RabbitMQ để tạo và thu hồi chia sẻ trò chuyện.
Lắng nghe  Livekit  để  thực hiện  chức năng trò chuyện giọng nói với người dùng.
