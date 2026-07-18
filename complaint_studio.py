from complaint_categorizer import ComplaintCategorizer


class ComplaintStudio:

    def __init__(self):

        self.categorizer = ComplaintCategorizer()

    def display_menu(self):

        while True:

            print("\n")

            print("=" * 60)

            print("           SMART COMPLAINT CATEGORIZER")

            print("=" * 60)

            print("1. Analyze Complaint")

            print("2. View Complaint History")

            print("3. View Statistics")

            print("4. Delete History")

            print("5. Exit")

            choice = input("\nEnter Choice : ").strip()

            if choice == "1":

                self.categorizer.analyze_complaint()

            elif choice == "2":

                self.categorizer.view_history()

            elif choice == "3":

                self.categorizer.statistics()

            elif choice == "4":

                self.categorizer.delete_history()

            elif choice == "5":

                print("\nThank You For Using Smart Complaint Categorizer!")

                break

            else:

                print("\nInvalid Choice. Please Try Again.")


if __name__ == "__main__":

    app = ComplaintStudio()

    app.display_menu()