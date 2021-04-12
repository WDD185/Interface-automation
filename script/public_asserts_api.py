import jsonpath
from script.base_api.service_profile.students import students_queryById_get
from script.default_header import jyy_header


def assert_phone_search(student_ids: list, phone):
    if student_ids:
        results = []
        for student_id in student_ids:
            params = {"studentId": student_id}
            student_res = students_queryById_get(params=params, header=jyy_header)
            student_prim_phones = jsonpath.jsonpath(student_res, "$.data.studentPrimPhoneNo")
            student_secondary_phones = jsonpath.jsonpath(student_res, "$.data.studentSecondaryPhoneNo")
            if student_prim_phones and student_secondary_phones:
                student_prim_phone = student_prim_phones[0]
                student_secondary_phone = student_secondary_phones[0]
                result = str(student_prim_phone) == str(phone) or str(student_secondary_phone) == str(phone)
            elif student_prim_phones:
                student_prim_phone = student_prim_phones[0]
                result = str(student_prim_phone) == str(phone)
            elif student_secondary_phones:
                student_secondary_phone = student_secondary_phones[0]
                result = str(student_secondary_phone) == str(phone)
            else:
                result = False
            results.append(result)
        all_result = all(results)
    else:
        all_result = False
    return all_result
