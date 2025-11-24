# Author: Alejandro Ceballos
# Date: 2025-11-23
# Module 7: Critical Thinking Assignment

def main():
    room_number_dict = {
        "CSC101": "3004",
        "CSC102": "4501",
        "CSC103": "6755",
        "NET110": "1244",
        "COM241": "1411"
    }

    instructors_dict = {
        "CSC101": "Haynes",
        "CSC102": "Alvarado",
        "CSC103": "Rich",
        "NET110": "Burke",
        "COM241": "Lee"
    }

    meeting_time_dict = {
        "CSC101": "8:00 a.m.",
        "CSC102": "9:00 a.m.",
        "CSC103": "10:00 a.m.",
        "NET110": "11:00 a.m.",
        "COM241": "1:00 p.m."
    }

    print("Available Courses:")
    for course in room_number_dict.keys():
        print(course)
    
    print()
    course_number = input("Enter the course number for additional information: ").strip().upper()

    if course_number in room_number_dict:
        print(f"{course_number} - Room Number: {room_number_dict[course_number]}")
        print(f"{course_number} - Instructor: {instructors_dict[course_number]}")
        print(f"{course_number} - Meeting Time: {meeting_time_dict[course_number]}")
    else:
        print("Please enter a valid course number.")

if __name__ == "__main__":
    main()
    