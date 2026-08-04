# Hướng dẫn bắt đầu bằng tiếng Việt

Tài liệu này dành cho người mới muốn dùng bộ Facebook Marketing Skills cùng Bina Social Poster MCP để nghiên cứu, viết, lưu nháp và lên lịch nội dung cho Facebook Page.

## 1. Hiểu ba thành phần

- **Skill**: bộ hướng dẫn giúp Codex viết post, chuyển thể nội dung, phân tích Page và soạn phản hồi.
- **Bina Social Poster MCP**: lớp kết nối để Codex đọc Page, media, post và tạo hoặc cập nhật nội dung trong Bina.
- **Bạn**: người duyệt nội dung và xác nhận các thao tác ghi dữ liệu.

Khi chưa kết nối Bina MCP, skill vẫn có thể viết nội dung và xuất bản nháp để bạn copy thủ công. Khi MCP đã kết nối, Codex có thể dùng các công cụ được cấp quyền.

## 2. Cài bộ skill từ thư mục đã clone

Mở PowerShell và chạy:

~~~powershell
Set-Location "C:\Users\minh-nghia\Documents\00. My File\00. Data\facebook-skills"
codex plugin marketplace add .
codex plugin add facebook-skills@facebook-skills
~~~

Sau đó mở một cuộc trò chuyện Codex mới để hệ thống nạp skill. Nếu lệnh `codex plugin` chưa có, hãy cập nhật Codex CLI hoặc cài bộ skill theo cơ chế plugin mà phiên bản Codex của bạn đang hỗ trợ.

## 3. Kết nối Bina Social Poster MCP

MCP cần được cấu hình ở **host của Codex**, không phải trong file skill. Ví dụ cấu hình dạng TOML:

~~~toml
[mcp_servers.bina_social]
url = "https://YOUR-MCP-HOST/mcp"
env_http_headers = { "X-API-Key" = "BINA_MCP_API_KEY" }
default_tools_approval_mode = "writes"
required = true
tool_timeout_sec = 60
~~~

Đặt API key trong biến môi trường của máy, không ghi key thật vào repository, file cấu hình được commit hoặc tin nhắn chat:

~~~powershell
[Environment]::SetEnvironmentVariable(
  "BINA_MCP_API_KEY",
  "PASTE_YOUR_KEY_HERE",
  "User"
)
~~~

Sau khi cấu hình, khởi động lại Codex. Tùy cách cài Bina, tên server có thể khác `bina_social`; hãy dùng đúng tên server trong cấu hình của bạn.

## 4. Những công cụ Bina MCP chính

| Nhu cầu | Công cụ thường dùng |
| --- | --- |
| Xem các Page được kết nối | `list_pages` |
| Xem media đã có | `list_media` |
| Chuẩn bị upload media | `prepare_media_upload` |
| Xem danh sách post | `list_posts` |
| Xem chi tiết một post | `get_post` |
| Lưu một post nháp | `create_post` |
| Sửa post nháp | `update_post` |
| Lên lịch post | `create_scheduled_post` |
| Xem lịch đã tạo | `list_schedules`, `get_schedule` |

Các thao tác ghi dữ liệu thường cần bạn phê duyệt. “Lưu nháp” không đồng nghĩa với “đăng ngay”.

## 5. Kiểm tra kết nối lần đầu

Gửi lần lượt các yêu cầu đơn giản sau trong Codex:

~~~text
Hãy liệt kê các Facebook Page đang được kết nối và cho tôi biết Page nào có thể dùng để tạo post.
~~~

~~~text
Hãy liệt kê 10 media gần đây, gồm tên và media UUID để tôi chọn ảnh cho post.
~~~

Nếu Codex trả về danh sách, kết nối cơ bản đã hoạt động. Nếu không, xem mục [Xử lý lỗi thường gặp](#14-xử-lý-lỗi-thường-gặp).

## 6. Viết post đầu tiên

Bạn nên nêu rõ sản phẩm, người đọc, mục tiêu, giọng điệu và giới hạn độ dài. Ví dụ:

~~~text
Viết 3 phiên bản Facebook post bằng tiếng Việt cho sản phẩm bình giữ nhiệt Bina.
- Đối tượng: nhân viên văn phòng 25-35 tuổi
- Mục tiêu: khuyến khích thử sản phẩm
- Giọng điệu: gần gũi, thực tế, không phóng đại
- Độ dài: dưới 80 từ mỗi phiên bản
- Mỗi phiên bản có hook rõ ràng và một CTA nhẹ
Chỉ hiển thị bản nháp, chưa gọi công cụ ghi dữ liệu.
~~~

Skill sẽ thường đi theo quy trình:

1. Làm rõ mục tiêu và đối tượng.
2. Tạo hook, nội dung chính và CTA.
3. Loại bỏ câu chữ máy móc, sáo rỗng hoặc khẳng định thiếu căn cứ.
4. Hiển thị bản nháp để bạn đọc.
5. Chờ bạn duyệt trước khi lưu hoặc lên lịch.

Để sửa bản nháp, nói cụ thể điều cần thay đổi:

~~~text
Giữ ý chính của phiên bản 2, nhưng viết tự nhiên hơn, bỏ 2 emoji, thêm một ví dụ sử dụng vào buổi sáng và giữ dưới 70 từ.
~~~

## 7. Lưu post thành draft trong Bina

Khi nội dung đã ổn, hãy chỉ rõ Page và yêu cầu lưu nháp:

~~~text
Lưu phiên bản 2 thành draft cho Page "Tên Page của tôi". Hãy xác nhận lại Page, loại post và nội dung cuối cùng trước khi thực hiện.
~~~

Với Bina MCP, `create_post` tạo post ở trạng thái `DRAFT`. Công cụ yêu cầu `idempotency_key` để tránh tạo trùng khi request bị gửi lại. Bạn không cần tự tạo key; hãy để host hoặc skill tạo key mới cho mỗi lần thử nội dung.

Không nên yêu cầu Codex đoán Page UUID. Hãy lấy Page từ `list_pages`, chọn đúng Page rồi mới tạo draft.

## 8. Gắn ảnh hoặc video

Trước tiên, tìm media:

~~~text
Hãy tìm trong media của Page "Tên Page của tôi" một ảnh sản phẩm bình giữ nhiệt phù hợp với post này. Chỉ dùng media UUID do Bina trả về.
~~~

Sau khi chọn được media UUID, yêu cầu:

~~~text
Lưu post này thành draft dạng IMAGE cho Page "Tên Page của tôi", dùng đúng media UUID vừa tìm được. Không dùng URL hoặc UUID tự đoán.
~~~

Các loại post được hỗ trợ trong workflow hiện tại gồm `TEXT`, `IMAGE`, `VIDEO` và `LINK`. Nếu file chưa có trong Bina, hãy upload qua giao diện Bina hoặc dùng workflow `prepare_media_upload` nếu host của bạn hỗ trợ đầy đủ bước upload.

Không tự bịa media UUID và không giả định mọi URL ảnh đều có thể dùng trực tiếp. Giới hạn file, MIME type và kích thước phụ thuộc vào media service của Bina.

## 9. Lên lịch đăng

Chỉ lên lịch sau khi đã có nội dung cuối cùng và xác nhận đúng Page, thời gian, múi giờ:

~~~text
Lên lịch phiên bản draft này cho Page "Tên Page của tôi" vào 2026-08-10 09:00 theo múi giờ Asia/Ho_Chi_Minh. Trước khi thực hiện, hãy hiển thị lại Page, thời gian, múi giờ, loại post và nội dung cuối.
~~~

`create_scheduled_post` tạo lịch ở trạng thái sẵn sàng theo cấu hình Bina. Thời gian cần ở tương lai, dùng định dạng thời gian hợp lệ và theo quy tắc của server; thông thường thời điểm phải cách hiện tại ít nhất 5 phút. Sau khi tạo, có thể kiểm tra bằng `list_schedules` hoặc `get_schedule`.

Hiện workflow MCP không có công cụ “đăng ngay” độc lập. Nếu bạn nói “đăng ngay”, hãy yêu cầu Codex tạo draft trước, hoặc dùng luồng publish trong giao diện Bina nếu hệ thống của bạn đã cung cấp luồng đó.

## 10. Sửa một draft đã lưu

Nếu đã có post UUID, dùng yêu cầu:

~~~text
Đọc post UUID "POST_UUID" bằng get_post. Sau đó đề xuất bản sửa, chưa cập nhật dữ liệu.
~~~

Sau khi duyệt:

~~~text
Đã duyệt bản sửa. Hãy cập nhật post UUID "POST_UUID" với đúng nội dung trên và kiểm tra version hiện tại trước khi ghi.
~~~

`update_post` dùng optimistic locking. Nếu có lỗi version conflict, hãy đọc lại bằng `get_post`, xem thay đổi mới nhất và xác nhận lại trước khi cập nhật tiếp.

## 11. Soạn phản hồi bình luận

Bina MCP hiện không có công cụ riêng để trả lời comment. Bạn có thể dán nội dung post và các comment vào Codex:

~~~text
Dựa trên post và các comment dưới đây, hãy soạn 5 câu trả lời ngắn bằng tiếng Việt.
- Thân thiện, không tranh cãi
- Mỗi câu dưới 35 từ
- Với câu hỏi chưa đủ thông tin, đề xuất hỏi thêm một chi tiết
- Chỉ xuất bản trả lời để tôi copy thủ công, không gọi create_post
~~~

Không dùng `create_post` để giả lập comment reply; công cụ đó tạo Facebook post mới.

## 12. Một số yêu cầu hữu ích

~~~text
Hãy làm cho post này tự nhiên hơn, giữ nguyên thông tin và không thêm claim mới.
~~~

~~~text
Chuyển post này thành 3 phiên bản: giáo dục, kể chuyện cá nhân và ưu đãi nhẹ.
~~~

~~~text
Từ nội dung này, hãy tạo kế hoạch 7 post cho Facebook Page, mỗi post gồm mục tiêu, hook, định dạng và CTA.
~~~

~~~text
Phân tích 20 post gần đây của Page này và chỉ ra 3 chủ đề hoặc hook nên thử tiếp. Nếu thiếu dữ liệu, nói rõ giới hạn.
~~~

## 13. Quy tắc an toàn cần nhớ

- Kiểm tra đúng Page trước mọi thao tác ghi dữ liệu.
- Không đoán Page UUID, post UUID, media UUID hoặc thời gian đăng.
- Đọc lại nội dung cuối trước khi lưu hoặc lên lịch.
- Không dùng lại cùng một idempotency key cho payload khác.
- Chỉ yêu cầu xóa khi bạn nêu rõ post UUID và xác nhận lần cuối.
- Khi gặp version conflict, đọc lại dữ liệu trước khi sửa.
- Không đưa API key vào prompt, README, commit hoặc file public.
- Nếu thông tin đầu vào chưa đủ, để Codex hỏi lại hoặc xuất bản nháp thay vì tự suy đoán.

## 14. Xử lý lỗi thường gặp

### Không thấy công cụ Bina MCP

Kiểm tra URL MCP, tên server, biến môi trường API key rồi khởi động lại Codex. Thử yêu cầu `list_pages` trong một cuộc trò chuyện mới.

### Không thấy Page hoặc media

Xác nhận tài khoản Bina có quyền truy cập, sau đó gọi lại `list_pages` hoặc `list_media`. Không nhập UUID thủ công nếu chưa lấy từ kết quả MCP.

### Idempotency conflict

Thường là cùng một key đã được dùng cho payload khác. Yêu cầu tạo request mới với idempotency key mới; không lặp lại key cũ cho nội dung đã thay đổi.

### Version conflict khi cập nhật

Có thay đổi mới hơn trên server. Gọi `get_post`, so sánh nội dung và version, rồi duyệt lại bản cập nhật.

### Chưa có Bina MCP

Skill vẫn viết được post, kế hoạch và câu trả lời. Hãy yêu cầu `Chỉ tạo bản nháp, không gọi MCP`, sau đó copy nội dung sang Bina hoặc Facebook theo quy trình thủ công.

## 15. Checklist 5 phút đầu tiên

- [ ] Cài plugin từ thư mục `facebook-skills`.
- [ ] Kết nối Bina MCP và giữ API key ngoài repository.
- [ ] Gọi `list_pages` để xác nhận Page.
- [ ] Gọi `list_media` nếu post cần ảnh hoặc video.
- [ ] Viết một post và yêu cầu chỉ hiển thị draft.
- [ ] Đọc lại Page, loại post, media, thời gian và nội dung.
- [ ] Duyệt `create_post` để lưu draft hoặc `create_scheduled_post` để lên lịch.

Khi đã quen, hãy xem thêm `README.md`, `references/bina-mcp-workflows.md` và tài liệu riêng của từng skill trong thư mục `skills/`.

