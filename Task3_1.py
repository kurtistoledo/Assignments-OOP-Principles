# Lesson 3: OOP Principles
# 1. Encapsulation in Personal Budget Management

class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget

    def get_category_name(self):
        return self.__category_name

    def set_category_name(self, new_name):
        self.__category_name = new_name

    def get_allocated_budget(self):
        return self.__allocated_budget

    def set_allocated_budget(self, new_budget):
        if new_budget >= 0:
            self.__allocated_budget = new_budget
            self.__remaining_budget = new_budget
        else:
            print("Budget amount must be a positive number.")

    def add_expense(self, amount):
        if amount > 0:
            if amount <= self.__remaining_budget:
                self.__remaining_budget -= amount
                print(f"${amount} expense added to {self.__category_name} category.")
            else:
                print("Expense amount exceeds remaining budget.")
        else:
            print("Expense amount must be a positive number.")

    def display_category_summary(self):
        print(f"Category Name: {self.__category_name}")
        print(f"Allocated Budget: ${self.__allocated_budget}")
        print(f"Remaining Budget: ${self.__remaining_budget}")


# Example usage
food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()
