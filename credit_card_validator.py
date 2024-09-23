def validate_credit_card(card_number):
    digits = [int(d) for d in card_number[::-1]]

    for i in range(1, len(digits), 2):
        digits[i] *= 2
        # If doubling results in a number greater than 9, subtract 9
        if digits[i] > 9:
            digits[i] -= 9

    total = sum(digits)

    # A valid card number will have a total that is a multiple of 10
    return total % 10 == 0

if __name__ == "__main__":
    credit_card_number = input("Enter the credit card number: ").strip()

    is_valid = validate_credit_card(credit_card_number)
    print(f"Credit Card Valid: {is_valid}")
