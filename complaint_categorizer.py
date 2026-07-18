import json
import os
import re


class ComplaintCategorizer:

    def __init__(self):

        self.file_name = "complaint_history.json"

        self.history = []

        self.categories = {

            "Billing": [
                "bill", "payment", "refund",
                "invoice", "charge", "money"
            ],

            "Technical": [
                "error", "bug", "crash",
                "login", "server", "issue"
            ],

            "Delivery": [
                "delivery", "late",
                "courier", "shipping",
                "parcel"
            ],

            "Account": [
                "password", "account",
                "profile", "signup",
                "login"
            ]

        }

        self.load_history()

    def load_history(self):

        if os.path.exists(self.file_name):

            try:

                with open(
                    self.file_name,
                    "r",
                    encoding="utf-8"
                ) as file:

                    self.history = json.load(file)

            except:

                self.history = []

    def save_history(self):

        with open(
            self.file_name,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.history,
                file,
                indent=4
            )

    def normalize(self, text):

        text = text.lower()

        text = re.sub(
            r"[^a-z0-9 ]",
            " ",
            text
        )

        return text

    def detect_category(self, complaint):

        complaint = self.normalize(complaint)

        scores = {}

        for category in self.categories:

            score = 0

            for keyword in self.categories[category]:

                if keyword in complaint:

                    score += 1

            scores[category] = score

        best = max(
            scores,
            key=scores.get
        )

        if scores[best] == 0:

            return "General"

        return best

    def detect_priority(self, complaint):

        complaint = complaint.lower()

        critical = [

            "fraud",

            "hacked",

            "urgent",

            "stolen",

            "data leak",

            "security"

        ]

        high = [

            "failed",

            "not working",

            "error",

            "crash"

        ]

        for word in critical:

            if word in complaint:

                return "Critical"

        for word in high:

            if word in complaint:

                return "High"

        if len(complaint) > 180:

            return "Medium"

        return "Low"

    def assign_department(self, category):

        mapping = {

            "Billing": "Finance Team",

            "Technical": "Technical Support",

            "Delivery": "Logistics Team",

            "Account": "Account Support",

            "General": "Customer Care"

        }

        return mapping.get(
            category,
            "Customer Care"
        )

    def analyze_complaint(self):

        print("\n========== Complaint ==========\n")

        complaint = input(
            "Enter Complaint : "
        ).strip()

        if complaint == "":

            print("\nComplaint cannot be empty.")

            return

        category = self.detect_category(
            complaint
        )

        priority = self.detect_priority(
            complaint
        )

        department = self.assign_department(
            category
        )

        result = {

            "complaint": complaint,

            "category": category,

            "priority": priority,

            "department": department

        }

        self.history.append(
            result
        )

        self.save_history()

        print("\n========== RESULT ==========\n")

        print("Category   :", category)

        print("Priority   :", priority)

        print("Department :", department)

    def view_history(self):

        print("\n========== HISTORY ==========\n")

        if not self.history:

            print("No Complaint History Found.")

            return

        for number, item in enumerate(

            self.history,

            start=1

        ):

            print(f"{number}.")

            print(

                "Complaint :",

                item["complaint"]

            )

            print(

                "Category  :",

                item["category"]

            )

            print(

                "Priority  :",

                item["priority"]

            )

            print(

                "Department:",

                item["department"]

            )

            print("-" * 45)

    def statistics(self):

        print("\n========== STATISTICS ==========\n")

        if not self.history:

            print("No Data Available.")

            return

        category_count = {}

        priority_count = {}

        for item in self.history:

            category = item["category"]

            priority = item["priority"]

            category_count[category] = (

                category_count.get(category, 0)

                + 1

            )

            priority_count[priority] = (

                priority_count.get(priority, 0)

                + 1

            )

        print("Category Summary\n")

        for key, value in category_count.items():

            print(

                f"{key} : {value}"

            )

        print("\nPriority Summary\n")

        for key, value in priority_count.items():

            print(

                f"{key} : {value}"

            )

    def delete_history(self):

        choice = input(

            "\nDelete History (yes/no): "

        ).lower()

        if choice == "yes":

            self.history.clear()

            self.save_history()

            print(

                "\nHistory Deleted Successfully."

            )

        else:

            print(

                "\nOperation Cancelled."

            )