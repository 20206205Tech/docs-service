import os

DATA = [
    {"abbr": "AI", "eng": "Artificial Intelligence", "vie": "Trí tuệ nhân tạo"},
    {
        "abbr": "API",
        "eng": "Application Programming Interface",
        "vie": "Giao diện lập trình ứng dụng",
    },
    {"abbr": "LLM", "eng": "Large Language Model", "vie": "Mô hình ngôn ngữ lớn"},
    {
        "abbr": "RAG",
        "eng": "Retrieval Augmented Generation",
        "vie": "Tạo tăng cường truy xuất",
    },
    {"abbr": "DDD", "eng": "Domain Driven Design", "vie": "Thiết kế hướng miền"},
    {"abbr": "MSA", "eng": "Microservice Architecture", "vie": "Kiến trúc vi dịch vụ"},
    {
        "abbr": "SQL",
        "eng": "Structured Query Language",
        "vie": "Ngôn ngữ truy vấn cấu trúc",
    },
    {
        "abbr": "JWT",
        "eng": "JSON Web Token",
        "vie": "Một tiêu chuẩn dùng để truyền tải thông tin dưới dạng JSON",
    },
    {
        "abbr": "JSON",
        "eng": "JavaScript Object Notation",
        "vie": "Ký hiệu đối tượng JavaScript",
    },
    {
        "abbr": "OOP",
        "eng": "Object-Oriented Programming",
        "vie": "Lập trình hướng đối tượng",
    },
    {
        "abbr": "URL",
        "eng": "Uniform Resource Locator",
        "vie": "Định danh tài nguyên Internet",
    },
    {"abbr": "CLI", "eng": "Command Line Interface", "vie": "Giao diện dòng lệnh"},
    {
        "abbr": "NLP",
        "eng": "Natural Language Processing",
        "vie": "Xử lý ngôn ngữ tự nhiên",
    },
    {"abbr": "CSDL", "eng": "Cơ sở dữ liệu", "vie": "Cơ sở dữ liệu"},
    {"abbr": "SSE", "eng": "Server-sent events", "vie": "Sự kiện máy chủ gửi"},
    {
        "abbr": "TOTP",
        "eng": "Time-based One-Time Password",
        "vie": "Mật khẩu dùng một lần dựa trên thời gian",
    },
    {"abbr": "2FA", "eng": "Two-Factor Authentication", "vie": "Xác thực hai yếu tố"},
    {"abbr": "MFA", "eng": "Multi-Factor Authentication", "vie": "Xác thực đa yếu tố"},
    {"abbr": "VIP", "eng": "Very Important Person", "vie": "Người rất quan trọng"},
    {"abbr": "K8s", "eng": "Kubernetes", "vie": "Kubernetes"},
    {"abbr": "CI", "eng": "Continuous Integration", "vie": "Tích hợp liên tục"},
    {
        "abbr": "CD",
        "eng": "Continuous Delivery / Deployment",
        "vie": "Chuyển giao/Triển khai liên tục",
    },
    #       {
    #     "abbr": "HTML",
    #     "eng": "Hyper Text Markup Language",
    #     "vie": "Ngôn ngữ Đánh dấu Siêu văn bản",
    # },
]


# <!-- *	SMTP: Simple Mail Transfer Protocol (Giao thức truyền thư đơn giản) -->

# <!-- *	UI: User Interface (Giao diện người dùng) -->


# Ack
# <!-- UML -->


# CQRS (Command Query Responsibility Segregation)

# là mẫu thiết kế tách biệt mô hình dữ liệu cho các thao tác đọc (Query) và ghi (Command). Việc tách biệt này giúp tối ưu hóa hiệu suất, tăng khả năng mở rộng (scalability), bảo mật tốt hơn và quản lý độ phức tạp trong các hệ thống lớn

# <!-- CQRS là viết tắt của Command and Query Responsibility Segregation -->


def generate_markdown():
    # Path relative to the root of the repository
    md_path = os.path.join("docs", "0", "9.md")

    # Sắp xếp theo Từ viết tắt (A-Z)
    sorted_data = sorted(DATA, key=lambda x: x["abbr"])

    # Tạo nội dung Markdown
    md_content = "# Danh sách viết tắt\n\n"
    md_content += "| Từ viết tắt | Từ viết đầy đủ | Mô tả |\n"
    md_content += "| --- | --- | --- |\n"

    for item in sorted_data:
        md_content += f"| {item['abbr']} | {item['eng']} | {item['vie']} |\n"

    # Ghi ra file markdown
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)

    print(f"Successfully updated {md_path}")


if __name__ == "__main__":
    generate_markdown()
