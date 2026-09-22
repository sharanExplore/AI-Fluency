import json

# Read private student data
with open("data/student_data.json", "r") as file:
    data = json.load(file)

print("Student:", data["student"])
print("\nNext Actions:\n")

for application in data["applications"]:

    company = application["company"]
    status = application["status"]
    test_completed = application["test_completed"]
    interview = application["interview"]

    # Fixed rules
    if status == "Applied" and not test_completed:
        action = "Complete the pending assessment/test."

    elif status == "Applied" and test_completed and not interview:
        action = "Prepare for the upcoming interview."

    elif status == "Interview" and interview:
        action = "Follow up after the interview."

    elif status == "Offer":
        action = "Review and respond to the offer."

    else:
        action = "No immediate action."

    print(f"{company} ({application['role']})")
    print(f"Status: {status}")
    print(f"Action: {action}")
    print()
    