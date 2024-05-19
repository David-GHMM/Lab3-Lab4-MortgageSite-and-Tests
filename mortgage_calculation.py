def mortgage_calc(price: str, initial_fee: str, percent: str, term: str, term_type: str) -> () or bool:
    try:
        credit_amount = int(price)-int(initial_fee)
        if credit_amount <= 0:
            return 0, 0, 0, 0

        if term_type == "Y":
            term = int(term) * 12
        else:
            term = int(term)

        monthly_per = float(percent) / 12 / 100
        total_rate = (1 + monthly_per)**term

        payment = credit_amount * monthly_per * total_rate / (total_rate-1)
        total = payment * term
        charges = total - credit_amount
    except ZeroDivisionError:
        return False
    except OverflowError:
        return False
    except ValueError:
        return False

    return credit_amount, round(payment), round(charges), round(total)
