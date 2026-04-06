"""
Completed by: Linsheng Zhang(120073242) 
Group: 12
Date: 2026-04-05
"""


class StudentRecordSystem:
    """
    A student record system implemented using a hash table (Python dictionary).
    Provides insert, retrieve, and delete operations.
    """

    def __init__(self):
        """
        Initializes an empty dictionary to store student records.
        Dictionary provides average O(1) time complexity for insert/retrieve/delete.
        """
        self.records = {}  # student_id -> {"name": name, "gpa": gpa}

    def insert(self, student_id, name, gpa):
        """
        Inserts a new student record.
        If student_id already exists, prints a warning and does nothing.
        Time complexity: O(1) average, O(n) worst-case (hash collision).
        """
        if student_id in self.records:
            print(f"Student {student_id} already exists. Please delete first if you want to update.")
        else:
            self.records[student_id] = {"name": name, "gpa": gpa}
            print(f"Inserted successfully: {student_id} - {name}, GPA {gpa}")

    def retrieve(self, student_id):
        """
        Retrieves and returns the student record for the given ID.
        If not found, prints a message and returns None.
        Time complexity: O(1) average, O(n) worst-case.
        """
        if student_id in self.records:
            info = self.records[student_id]
            print(f"Retrieved: {student_id} - {info['name']}, GPA {info['gpa']}")
            return info
        else:
            print(f"Student {student_id} not found")
            return None

    def delete(self, student_id):
        """
        Deletes the student record with the given ID.
        If not found, prints a message.
        Time complexity: O(1) average, O(n) worst-case.
        """
        if student_id in self.records:
            del self.records[student_id]
            print(f"Deleted student {student_id}")
        else:
            print(f"Student {student_id} not found, cannot delete")

    def display_all(self):
        """
        Prints all student records in the hash table.
        Time complexity: O(n) where n is number of records.
        """
        if not self.records:
            print("\nNo student records found.")
            return
        print("\nAll student records:")
        for sid, info in self.records.items():
            print(f"{sid}: {info['name']}, GPA {info['gpa']}")


if __name__ == "__main__":
    system = StudentRecordSystem()

    # Test insert
    system.insert("A001", "Alice", 3.8)
    system.insert("B002", "Bob", 3.5)
    system.insert("A001", "Alice", 3.9)      # duplicate test
    system.insert("C003", "Charlie", 3.2)

    # Test retrieve
    system.retrieve("A001")
    system.retrieve("D999")

    # Display all
    system.display_all()

    # Test delete
    system.delete("B002")
    system.display_all()
    system.delete("B002")  # second delete should fail

    # Research Question 2 answer 
    """
    Q2: Advantages of hash table over sorted list for student records:
        - Hash table provides average O(1) search, insert, delete.
        - Sorted list requires O(log n) search (binary search) but O(n) insert/delete due to shifting elements.
        - Hash table is better for dynamic data with frequent updates.
        - Sorted list only beneficial if sorted order is needed for range queries.
    """