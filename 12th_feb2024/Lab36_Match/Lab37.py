# Match Function another example

browser = input("Enter your browser name \n")
match browser:
    case "Chrome":
        print("Opening chrome browser")
    case "Firefox":
        print("Opening Firefox browser")
    case _:
        print("No browser found")