def calculate_loan_payment(loan_amount, interest_rate, loan_term):
    # Convert annual interest rate to monthly and convert loan term from years to months
    monthly_interest_rate = interest_rate / 12
    number_of_payments = loan_term * 12

    # Calculate monthly payment using the amortization formula
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -number_of_payments)
    
    return monthly_payment

if __name__ == "__main__":
    loan_amount = float(input("Enter the loan amount: "))
    interest_rate = float(input("Enter the annual interest rate (as a decimal): "))
    loan_term = int(input("Enter the loan term (in years): "))

    monthly_payment = calculate_loan_payment(loan_amount, interest_rate, loan_term)
    print(f"Monthly Payment: ${monthly_payment:.2f}")
