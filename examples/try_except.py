def parse_email(email_address):
    username, domain = email_address.split("@")
    return username, domain


if __name__ == "__main__":
    emails = [
        "ana.ionescu@gmail.com",
        "matei.georgescu",
        "admin@mydomain.ro",
        "test@@my_domain",
    ]
    for email in emails:
        try:
            user_name, domain_name = parse_email(email)
        except (ValueError, TypeError) as ex:
            print(f"Could not parse {email} because of {ex} ({type(ex)})")
        except NameError:
            print("Error!")
        except Exception:
            print("Any exception!")
        else:
            print(f"Successfully parsed {email}")
        finally:
            print("Executes every time - closes context")
