def parse_and_validate_email(email_address):
    username, domain = email_address.split("@")
    if domain != "ing.com":
        raise ValueError("external e-mail address.")
    return username, domain


if __name__ == "__main__":
    emails = [
        "ana.ionescu@ing.com",
        "matei.georgescu",
        "admin@ing.com",
        "test@gmail.com",
        "test@@my_domain",
    ]
    for email in emails:
        try:
            user_name, domain_name = parse_and_validate_email(email)
        except (ValueError, TypeError) as ex:
            print(f"Could not parse {email} because of {ex} ({type(ex)})")
        except NameError as ex:
            print(ex)
        else:
            print(f"Successfully parsed {email}")
        finally:
            print("Executes every time - closes context\n")
