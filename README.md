<p align="center">
  <img src="assets/hero.png" alt="Bộ kỹ năng marketing Facebook cho Claude Code và Codex" width="900" />
</p>

# Facebook Marketing Skills

Bộ 8 kỹ năng giúp Claude Code và Codex trở thành trợ lý nội dung cho Facebook Page. Công cụ hỗ trợ viết, chỉnh sửa, kiểm tra và lập kế hoạch nội dung bằng tiếng Việt hoặc ngôn ngữ bạn sử dụng.

> Người mới nên bắt đầu với [hướng dẫn sử dụng tiếng Việt](references/huong-dan-bat-dau-vi.md).

<p align="center">
  <img src="https://img.shields.io/github/v/release/minhnghia1522/facebook-skills?color=111827&label=release" alt="Phiên bản mới nhất">
  <img src="https://img.shields.io/badge/Claude_Code-Tương_thích-D97757?logo=anthropic&logoColor=white" alt="Tương thích Claude Code">
  <img src="https://img.shields.io/badge/Codex-Tương_thích-111827" alt="Tương thích Codex">
  <img src="https://img.shields.io/badge/License-MIT-22C55E.svg" alt="Giấy phép MIT">
  <img src="https://img.shields.io/github/stars/minhnghia1522/facebook-skills?style=social" alt="GitHub stars">
</p>

## Cài đặt

### Codex CLI

```bash
codex plugin marketplace add minhnghia1522/facebook-skills
codex plugin add facebook-skills@facebook-skills
```

### Claude Code

```text
/plugin marketplace add minhnghia1522/facebook-skills
/plugin install facebook-skills@facebook-skills
```

### Cài từ bản sao cục bộ

```bash
git clone https://github.com/minhnghia1522/facebook-skills.git
cd facebook-skills
codex plugin marketplace add .
codex plugin add facebook-skills@facebook-skills
```

Với Claude Desktop hoặc claude.ai, chọn **Skills → Add from GitHub** rồi nhập `minhnghia1522/facebook-skills`.

## Bạn có thể làm gì?

- Viết bài Facebook Page ngắn, rõ và có khả năng tạo tương tác.
- Biến nội dung từ LinkedIn, X, blog hoặc newsletter thành bài Facebook tự nhiên.
- Kiểm tra và loại bỏ các dấu hiệu văn phong do AI tạo ra.
- Phân tích hook của một bài viết có nhiều lượt chia sẻ.
- Soạn trả lời bình luận theo đúng giọng thương hiệu.
- Lập kế hoạch nội dung Facebook Page theo tuần.
- Tối ưu tên Page, username, ảnh đại diện, ảnh bìa, CTA, phần giới thiệu và bài ghim.
- Đọc thống kê Page và danh sách người bình luận công khai qua Apify.

Mọi bản nháp đều được hiển thị để bạn xem và phê duyệt trước. Không có nội dung nào được đăng nếu bạn chưa đồng ý.

## 8 kỹ năng

| Kỹ năng | Chức năng |
|---|---|
| Post Writer | Viết bài ngắn hoặc bài kể chuyện dài cho Page. |
| Repurposer | Chuyển nội dung từ nền tảng khác thành bài Facebook bản địa. |
| Humanizer | Làm văn phong tự nhiên và kiểm tra trước khi đăng. |
| Hook Extractor | Phân tích hook và tạo công thức để tái sử dụng. |
| Engagement Drafter | Soạn câu trả lời cho bình luận. |
| Content Planner | Lập kế hoạch nội dung theo tuần. |
| Page Optimizer | Kiểm tra và viết lại thông tin trên Page. |
| Audience Insights | Đọc dữ liệu Page và người bình luận công khai. |

## Ví dụ câu lệnh

```text
Viết một bài Facebook ngắn giới thiệu sản phẩm mới của chúng tôi.
Lập kế hoạch nội dung Facebook Page trong 7 ngày cho một tiệm bánh địa phương.
Kiểm tra bài viết sau xem có dấu hiệu văn phong AI không: [dán nội dung]
Soạn câu trả lời cho các bình luận sau theo giọng thân thiện: [dán bình luận]
```

## Đăng bài và Bina Social Poster MCP

Khi Bina Social Poster MCP được cấu hình, bộ kỹ năng có thể đọc Page, media và tạo bản nháp hoặc lịch đăng bằng các công cụ được cấp quyền. Nội dung, Page, media và thời gian luôn được đưa ra để bạn phê duyệt trước khi ghi dữ liệu.

Nếu MCP chưa được kết nối, bộ kỹ năng vẫn hoạt động ở chế độ chỉ tạo bản nháp và trả về khối nội dung để bạn sao chép thủ công. Không đặt API key hoặc thông tin đăng nhập Facebook vào repository này.

Xem chi tiết quy trình tại [`references/bina-mcp-workflows.md`](references/bina-mcp-workflows.md).

## Quy tắc giọng văn

- Ưu tiên câu mở đầu ngắn, cụ thể và dễ chia sẻ.
- Dùng tên thương hiệu đúng cách viết.
- Tránh từ ngữ sáo rỗng, giọng văn doanh nghiệp và các dấu hiệu thường gặp của AI.
- Ưu tiên số liệu cụ thể thay cho tính từ chung chung.
- Dùng hashtag và emoji có chừng mực.

## Tài liệu tham khảo

- [`references/hook-formulas.md`](references/hook-formulas.md): 10 công thức hook Facebook.
- [`references/algorithm-heuristics.md`](references/algorithm-heuristics.md): các tín hiệu phân phối nội dung.
- [`references/bina-mcp-workflows.md`](references/bina-mcp-workflows.md): quy trình MCP, phê duyệt và lập lịch.
- [`references/voice-rules.md`](references/voice-rules.md): quy tắc giọng văn dùng chung.

## Giấy phép

MIT. Xem [LICENSE](LICENSE).

## Các dự án liên quan

Bộ kỹ năng này được phát triển cùng ý tưởng với các bộ skill mạng xã hội khác như [LinkedIn Skills](https://github.com/sergebulaev/linkedin-skills), [Instagram Skills](https://github.com/sergebulaev/instagram-skills) và [X Skills](https://github.com/sergebulaev/x-skills).
