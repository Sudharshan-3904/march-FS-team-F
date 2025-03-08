def get_user_input():
    user_data = {}

    try:
        user_data["ID"] = int(input("Enter ID (Integer): "))
        user_data["Name"] = input("Enter Name (String): ")
        user_data["Age"] = int(input("Enter Age (Integer): "))

        print("\nCollected Data:")
        for key, value in user_data.items():
            print(f"{key}: {value}")

    except ValueError:
        print("Invalid input! Please enter integers for ID and Age.")

# Run the function
get_user_input()
