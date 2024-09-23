class Customer:
    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.policies = [] 

    def add_policy(self, policy):
        self.policies.append(policy)

    def get_info(self):
        info = f"Name: {self.name}\nAddress: {self.address}\nEmail: {self.email}\nPolicies:"
        for policy in self.policies:
            info += f"\n  - {policy.get_info()}"
        return info


class InsurancePolicy:
    def __init__(self, coverage_type, premium, start_date):
        self.coverage_type = coverage_type
        self.premium = premium
        self.start_date = start_date

    def get_info(self):
        return f"Coverage Type: {self.coverage_type}, Premium: ${self.premium}, Start Date: {self.start_date}"


if __name__ == "__main__":
    customer_name = input("Enter customer's name: ")
    customer_address = input("Enter customer's address: ")
    customer_email = input("Enter customer's email: ")
    
    customer = Customer(customer_name, customer_address, customer_email)

    while True:
        coverage_type = input("\nEnter policy coverage type (e.g., Auto, Health, Home): ")
        premium = float(input("Enter policy premium amount: "))
        start_date = input("Enter policy start date (YYYY-MM-DD): ")

        policy = InsurancePolicy(coverage_type, premium, start_date)
        customer.add_policy(policy)

        another = input("Do you want to add another policy? (yes/no): ").strip().lower()
        if another != 'yes':
            break

    print("\nCustomer Information:")
    print(customer.get_info())
