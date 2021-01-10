# import face_recognition_models
# from PIL import Image
# import fa
# img  face_recognition_models.cnn_face_detector_model_location()
#
#
#
# def color_translator(color):
#     if color == "red":
#         hex_color = "#ff0000"
#     elif color == "green":
#         hex_color = "#00ff00"
#     elif color == "blue":
#         hex_color = "#0000ff"
#     else:
#         hex_color = "unknown"
#     return 'unknown'
#
#
# print(color_translator("blue"))  # Should be #0000ff
# print(color_translator("yellow"))  # Should be unknown
# print(color_translator("red"))  # Should be #ff0000
# print(color_translator("black"))  # Should be unknown
# print(color_translator("green"))  # Should be #00ff00
# print(color_translator(""))  # Should be unknown
#

def exam_grade(score):
    if score == 100:
        grade = "Top Score"
    elif 60 <= score <= 95:
        grade = "Pass"
    else:
        grade = "Fail"
    return grade


print(exam_grade(65))  # Should be Pass
print(exam_grade(55))  # Should be Fail
print(exam_grade(60))  # Should be Pass
print(exam_grade(95))  # Should be Pass
print(exam_grade(100))  # Should be Top Score
print(exam_grade(0))  # Should be Fail
