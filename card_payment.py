card_detected = False
payment_successful = False
while True:
    cash_register = "Cash register"
    payment_processed = "Payment successful"
    payment_not_processed = "Payment failed"
    payment = "Payment"
    not_detected = "Try again"
    unknown = "Tap card"
    answer = input(f"Tap card to {cash_register} (yes/no)").lower()
    if answer == "no":
        print(f"{unknown}")
    if answer == "yes":
        card_detected = True
        if card_detected == True:
           answer = input(f"Whether to debit the {payment}? (yes/no/try)")
           if answer == "yes":
               payment_successful = True
               if payment_successful == True:
                   print(f"{payment_processed}")
                   break
           elif answer == "try":
               payment_successful = False
               if payment_successful == False:
                   print(f"{not_detected}")
           elif answer == "no":
               payment_successful = False
               if payment_successful == False:
                   print(f"{payment_not_processed}")
                   break
