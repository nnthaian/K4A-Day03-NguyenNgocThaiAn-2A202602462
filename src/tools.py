"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [
    {
        "name": "academic_query",
        "description": "Tra cứu hồ sơ và thông tin học vụ của sinh viên VinUni bằng mã sinh viên.",
        "parameters": {
            "type": "object",
            "properties": {
                "student_id": {
                    "type": "string",
                    "description": "Mã sinh viên cần tra cứu (ví dụ: 'SV2026001')"
                }
            },
            "required": ["student_id"]
        }
    },
    {
        "name": "query_gpa",
        "description": "Tra cứu CGPA và Major GPA của sinh viên VinUni bằng mã sinh viên.",
        "parameters": {
            "type": "object",
            "properties": {
                "student_id": {
                    "type": "string",
                    "description": "Mã sinh viên cần tra cứu."
                }
            },
            "required": ["student_id"]
        }
    },
    {
        "name": "check_graduation_eligibility",
        "description": "Kiểm tra điều kiện tốt nghiệp dựa trên tín chỉ, GPA, học phần trượt, thực tập và khóa luận.",
        "parameters": {
            "type": "object",
            "properties": {
                "student_id": {
                    "type": "string",
                    "description": "Mã sinh viên cần kiểm tra."
                }
            },
            "required": ["student_id"]
        }
    },
    {
        "name": "query_exam_schedule",
        "description": "Tra cứu lịch thi cuối kỳ của sinh viên bằng mã sinh viên.",
        "parameters": {
            "type": "object",
            "properties": {
                "student_id": {
                    "type": "string",
                    "description": "Mã sinh viên cần tra cứu lịch thi."
                }
            },
            "required": ["student_id"]
        }
    },
    {
        "name": "schedule_appointment",
        "description": "Đặt lịch hẹn tư vấn học vụ với Cố vấn học tập VinUni.",
        "parameters": {
            "type": "object",
            "properties": {
                "student_id": {
                    "type": "string",
                    "description": "Mã sinh viên cần đặt lịch"
                },
                "datetime_str": {
                    "type": "string",
                    "description": "Thời gian hẹn theo định dạng dd/MM/yyyy HH:mm"
                },
                "advisor_name": {
                    "type": "string",
                    "description": "Tên cố vấn học tập tham gia buổi tư vấn"
                }
            },
            "required": ["student_id", "datetime_str", "advisor_name"]
        }
    }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

MOCK_DATABASE = {
    "SV2026001": {
        "full_name": "Nguyễn Văn An",
        "class": "AI-K4",
        "email": "an.nv@vinuni.edu.vn",
        "status": "Đang học",
        "advisor": "PGS.TS Nguyễn Văn A",
        "exam_schedule": [
            {
                "course_code": "AI302",
                "course_name": "Học máy",
                "exam_date": "22/09/2026",
                "start_time": "13:30",
                "room": "B105"
            }
        ],

        # --- Thông tin điểm ---
        "cgpa": 3.85,
        "major_gpa": 3.90,

        # --- Thông tin tín chỉ ---
        "total_credits_required": 140,
        "credits_earned": 140,
        "major_credits_required": 60,
        "major_credits_earned": 60,

        # --- Điều kiện bổ sung ---
        "failed_courses": [],              
        "internship_completed": True,
        "thesis_status": "Đã hoàn thành", 
        "min_gpa_to_graduate": 2.0,
    },
    "SV2026002": {
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

        "cgpa": 3.60,
        "major_gpa": 3.55,

        "total_credits_required": 140,
        "credits_earned": 118,
        "major_credits_required": 60,
        "major_credits_earned": 45, 

        "failed_courses": ["CS301 - Thuật toán"],
        "internship_completed": False,
        "thesis_status": "Đang thực hiện",
        "min_gpa_to_graduate": 2.0,
    }
}


def execute_academic_query(student_id: str) -> str:
    """Thực thi tra cứu học vụ theo mã sinh viên"""
    student = MOCK_DATABASE.get(student_id.strip().upper())
    if student:
        return json.dumps({
            "status": "SUCCESS",
            "student_id": student_id,
            "data": student
        }, ensure_ascii=False)
    else:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy dữ liệu sinh viên có mã '{student_id}'"
        }, ensure_ascii=False)


def execute_query_gpa(student_id: str) -> str:
    """Tra cứu CGPA và Major GPA của sinh viên"""
    student = MOCK_DATABASE.get(student_id.strip().upper())
    if not student:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy dữ liệu sinh viên có mã '{student_id}'"
        }, ensure_ascii=False)

    return json.dumps({
        "status": "SUCCESS",
        "student_id": student_id,
        "data": {
            "cgpa": student["cgpa"],
            "major_gpa": student["major_gpa"]
        }
    }, ensure_ascii=False)


def execute_check_graduation_eligibility(student_id: str) -> str:
    """Kiểm tra điều kiện tốt nghiệp từ dữ liệu học vụ của sinh viên"""
    student = MOCK_DATABASE.get(student_id.strip().upper())
    if not student:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy dữ liệu sinh viên có mã '{student_id}'"
        }, ensure_ascii=False)

    reasons = []
    if student["credits_earned"] < student["total_credits_required"]:
        reasons.append(
            f"Còn thiếu tín chỉ tổng: {student['credits_earned']}/{student['total_credits_required']}"
        )
    if student["major_credits_earned"] < student["major_credits_required"]:
        reasons.append(
            f"Còn thiếu tín chỉ chuyên ngành: {student['major_credits_earned']}/{student['major_credits_required']}"
        )
    if student["cgpa"] < student["min_gpa_to_graduate"]:
        reasons.append(f"CGPA dưới mức tối thiểu {student['min_gpa_to_graduate']}")
    if student["failed_courses"]:
        reasons.append(f"Còn học phần chưa đạt: {', '.join(student['failed_courses'])}")
    if not student["internship_completed"]:
        reasons.append("Chưa hoàn thành thực tập")
    if student["thesis_status"] != "Đã hoàn thành":
        reasons.append(f"Tình trạng khóa luận: {student['thesis_status']}")

    return json.dumps({
        "status": "SUCCESS",
        "student_id": student_id,
        "eligible": not reasons,
        "reasons": reasons
    }, ensure_ascii=False)


def execute_query_exam_schedule(student_id: str) -> str:
    """Tra cứu lịch thi cuối kỳ của sinh viên"""
    student = MOCK_DATABASE.get(student_id.strip().upper())
    if not student:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy dữ liệu sinh viên có mã '{student_id}'"
        }, ensure_ascii=False)

    return json.dumps({
        "status": "SUCCESS",
        "student_id": student_id,
        "data": student["exam_schedule"]
    }, ensure_ascii=False)


def execute_schedule_appointment(student_id: str, datetime_str: str, advisor_name: str = "PGS.TS Nguyễn Văn A") -> str:
    """Thực thi đặt lịch hẹn tư vấn học vụ"""
    student = MOCK_DATABASE.get(student_id.strip().upper())
    if not student:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy dữ liệu sinh viên có mã '{student_id}'"
        }, ensure_ascii=False)
    if advisor_name != student["advisor"]:
        return json.dumps({
            "status": "ADVISOR_MISMATCH",
            "student_id": student_id,
            "requested_advisor": advisor_name,
            "actual_advisor": student["advisor"],
            "message": f"Cố vấn phụ trách của {student_id} là {student['advisor']}, không phải {advisor_name}."
        }, ensure_ascii=False)

    return json.dumps({
        "status": "SUCCESS",
        "booking_id": f"BK-{student_id}-99",
        "student_id": student_id,
        "datetime": datetime_str,
        "advisor": advisor_name,
        "message": f"Đặt lịch thành công cho sinh viên {student_id} với {advisor_name} vào lúc {datetime_str}."
    }, ensure_ascii=False)


# Router gọi tool thực tế
TOOL_ROUTER = {
    "academic_query": execute_academic_query,
    "query_gpa": execute_query_gpa,
    "check_graduation_eligibility": execute_check_graduation_eligibility,
    "query_exam_schedule": execute_query_exam_schedule,
    "schedule_appointment": execute_schedule_appointment
}

def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm trung chuyển thực thi tool"""
    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)
    return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)
