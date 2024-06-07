def main():
    total_jacks = 100
    remaining_jacks = total_jacks
    set_size = 10

    while remaining_jacks > 0:
        print(f"Remaining jumping jacks: {remaining_jacks}")
        response = input("Are you tired? (yes/no): ").lower()

        if response in ["yes", "y"]:
            skip_remaining = input("Do you want to skip the remaining sets? (yes/no): ").lower()
            if skip_remaining in ["yes", "y"]:
                print(f"You completed a total of {total_jacks - remaining_jacks} jumping jacks.")
                break
        else:
            remaining_jacks -= set_size

    if remaining_jacks == 0:
        print("Congratulations! You completed the workout.")

if __name__ == "__main__":
    main()
