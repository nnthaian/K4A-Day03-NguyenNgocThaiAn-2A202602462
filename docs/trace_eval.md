# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Nguyễn Ngọc Thái An
> **Mã Sinh Viên / Mã Học viên:** 2A202602462  
> **Chủ đề Lựa chọn:** Trợ lý học vụ có thể tra cứu điểm GPA (CGPA và Major GPA), lịch thi, xét điều kiện tốt nghiệp hoặc đặt lịch tư vấn với cố vấn học tập


---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 4 / 5 | Agent phải phân loại đúng ý định trong 3 loại truy vấn độc lập (GPA/điều kiện tốt nghiệp/lịch thi), mỗi loại kéo theo chuỗi xử lý riêng. Với việc đặt lịch hẹn, agent xử lý 2 kịch bản kích hoạt khác nhau: (a) sinh viên yêu cầu đặt lịch trực tiếp ngay từ đầu, hoặc (b) agent tự đề xuất đặt lịch sau khi tra cứu phát hiện vấn đề |
| **2. Tool Interaction** | 4 / 5 | Cần kết nối tối thiểu 2 nguồn dữ liệu ngoài: database điểm và hệ thống lịch. Agent phải chọn đúng tool tương ứng với từng loại truy vấn, và một tool riêng cho hành động đặt lịch. |
| **3. Dynamic Decision** | 4 / 5 | Ba lớp quyết định động: (a) nhận diện đúng loại truy vấn; (b) sau khi có kết quả tra cứu, agent tự quyết định có nên chủ động đề xuất đặt lịch tư vấn hay không; (c) xử lý được trường hợp sinh viên bỏ qua bước tra cứu và yêu cầu đặt lịch trực tiếp |
| **4. Long Horizon Goal** | 2 / 5 | Toàn bộ luồng diễn ra trong phạm vi một phiên tương tác, không yêu cầu duy trì trạng thái hay mục tiêu xuyên suốt nhiều ngày/nhiều phiên |
| **TỔNG ĐIỂM AGENTIC FIT** | **14 / 20** | *Nếu tổng điểm > 12/20: Bài toán rất phù hợp triển khai Agentic System.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "query": "Tôi là sinh viên SV2026002. Hãy kiểm tra điều kiện tốt nghiệp của tôi, nếu chưa đủ thì đặt giúp tôi lịch tư vấn với cố vấn phụ trách vào lúc 09:30 ngày 16/09/2026.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "check_graduation_eligibility",
    "arguments": {
      "student_id": "SV2026002"
    },
    "observation": {
      "status": "SUCCESS",
      "student_id": "SV2026002",
      "eligible": false,
      "reasons": [
        "Còn thiếu tín chỉ tổng: 118/140",
        "Còn thiếu tín chỉ chuyên ngành: 45/60",
        "Còn học phần chưa đạt: CS301 - Thuật toán",
        "Chưa hoàn thành thực tập",
        "Tình trạng khóa luận: Đang thực hiện"
      ]
    },
    "latency_ms": 7899.34
  },
  {
    "step": 2,
    "query": "Tôi là sinh viên SV2026002. Hãy kiểm tra điều kiện tốt nghiệp của tôi, nếu chưa đủ thì đặt giúp tôi lịch tư vấn với cố vấn phụ trách vào lúc 09:30 ngày 16/09/2026.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "academic_query",
    "arguments": {
      "student_id": "SV2026002"
    },
    "observation": {
      "status": "SUCCESS",
      "student_id": "SV2026002",
      "data": {
        "full_name": "Trần Thị Bình",
        "class": "AI-K4",
        "email": "binh.tt@vinuni.edu.vn",
        "status": "Đang học",
        "advisor": "TS. Lê Thị B",
        "exam_schedule": [
          {
            "course_code": "DB204",
            "course_name": "Cơ sở dữ liệu",
            "exam_date": "24/09/2026",
            "start_time": "08:00",
            "room": "A203"
          }
        ],
        "cgpa": 3.6,
        "major_gpa": 3.55,
        "total_credits_required": 140,
        "credits_earned": 118,
        "major_credits_required": 60,
        "major_credits_earned": 45,
        "failed_courses": [
          "CS301 - Thuật toán"
        ],
        "internship_completed": false,
        "thesis_status": "Đang thực hiện",
        "min_gpa_to_graduate": 2.0
      }
    },
    "latency_ms": 11982.63
  },
  {
    "step": 3,
    "query": "Tôi là sinh viên SV2026002. Hãy kiểm tra điều kiện tốt nghiệp của tôi, nếu chưa đủ thì đặt giúp tôi lịch tư vấn với cố vấn phụ trách vào lúc 09:30 ngày 16/09/2026.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "schedule_appointment",
    "arguments": {
      "advisor_name": "TS. Lê Thị B",
      "student_id": "SV2026002",
      "datetime_str": "16/09/2026 09:30"
    },
    "observation": {
      "status": "SUCCESS",
      "booking_id": "BK-SV2026002-99",
      "student_id": "SV2026002",
      "datetime": "16/09/2026 09:30",
      "advisor": "TS. Lê Thị B",
      "message": "Đặt lịch thành công cho sinh viên SV2026002 với TS. Lê Thị B vào lúc 16/09/2026 09:30."
    },
    "latency_ms": 12237.83
  },
  {
    "step": 4,
    "query": "Tôi là sinh viên SV2026002. Hãy kiểm tra điều kiện tốt nghiệp của tôi, nếu chưa đủ thì đặt giúp tôi lịch tư vấn với cố vấn phụ trách vào lúc 09:30 ngày 16/09/2026.",
    "action_type": "FINAL_ANSWER",
    "thought": "NVIDIA NIM phản hồi trực tiếp bằng văn bản.",
    "output": "Chào bạn Trần Thị Bình (SV2026002),\n\nTôi đã kiểm tra điều kiện tốt nghiệp của bạn và kết quả cho thấy **bạn chưa đủ điều kiện tốt nghiệp** với các lý do sau:\n\n1. **Thiếu tín chỉ tổng**: 118/140 tín chỉ (còn thiếu 22 tín chỉ)\n2. **Thiếu tín chỉ chuyên ngành**: 45/60 tín chỉ (còn thiếu 15 tín chỉ)\n3. **Học phần chưa đạt**: CS301 - Thuật toán\n4. **Chưa hoàn thành thực tập**\n5. **Khóa luận**: Đang thực hiện\n\nTuy nhiên, GPA của bạn khá tốt (CGPA: 3.6, Major GPA: 3.55) - đều vượt quá ngưỡng tối thiểu 2.0 để tốt nghiệp.\n\nTheo yêu cầu của bạn, tôi đã **đặt lịch tư vấn thành công** với cố vấn học tập phụ trách **TS. Lê Thị B**:\n- **Mã đặt lịch**: BK-SV2026002-99\n- **Thời gian**: 09:30 ngày 16/09/2026\n- **Cố vấn**: TS. Lê Thị B\n\nBạn hãy chuẩn bị các câu hỏi về kế hoạch hoàn thiện tín chỉ, học lại CS301, thực tập và tiến độ khóa luận để thảo luận chi tiết với cố vấn trong buổi tư vấn này nhé.\n\nChúc bạn có một buổi tư vấn hiệu quả!",
    "latency_ms": 16962.22
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Nvidia Nim).
- **Tổng số Test Cases đã chạy thành công:** 9/9 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** 10 lượt.
- [x] **Kết quả đẩy Repo nộp bài:** Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
