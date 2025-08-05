def validate_input(prompt: str, cast_type, validator_fn, error_msg: str):
    while True:
        try:
            amount = cast_type(input(prompt))

            if not validator_fn(amount):
                print(error_msg)
            else:
                return amount
        except ValueError as e:
            print(f"{str(e).capitalize()}, please try again.")