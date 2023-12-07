def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return "Value error"
        except Exception as e:
            return f"Undefined exception"

    return inner


def check_input_correctness(
        number_of_params_that_should_be_pass_to_function,
        error_message
):
    def decorator(func):
        def changed_function(*args, **kwargs):
            if len(args[0]) != number_of_params_that_should_be_pass_to_function:
                return error_message
            return func(*args, **kwargs)

        return changed_function

    return decorator


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


@input_error
@check_input_correctness(
    2,
    "Please input the command in the format: add [name] [phone]"
)
def add_or_change_contact(args, contacts):
    name, phone = args

    response = "Contact changed" if name in contacts else "Contact added"
    contacts[name] = phone
    return response


@input_error
@check_input_correctness(
    1,
    "Please input the command in the format: phone [name]"
)
def print_phone_by_name(args, contacts):
    if not args:
        return "Please provide a name to search for."

    name = args[0]
    if name not in contacts:
        return f"No contact found for {name}."

    phone = contacts[name]
    return f"{name}: {phone}"


@input_error
@check_input_correctness(
    0,
    "Please input the command in the format: all"
)
def print_all_contacts(contacts):
    if not contacts:
        return "No contacts available."

    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add" or command == "change":
            print(add_or_change_contact(args, contacts))
        elif command == "phone":
            print(print_phone_by_name(args, contacts))
        elif command == "all":
            print(print_all_contacts(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
