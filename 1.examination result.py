# Examination Result and Grace-Mark Validation

marks = int(input("Enter your marks: "))
grace_marks = int(input("Enter grace marks: "))

total = marks + grace_marks

print("Original Marks:", marks)
print("Grace Marks:", grace_marks)
print("Final Marks:", total)

if total >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")
