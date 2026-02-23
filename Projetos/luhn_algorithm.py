def verify_card_number(number):
    
    digits = [int(d) for d in str(number).replace(" ", "").replace("-", "")]

    soma = 0
    for i, digit in enumerate(reversed(digits)):
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        soma += digit
    if soma % 10 == 0:
        return 'VALID!'
    return 'INVALID!' 
    