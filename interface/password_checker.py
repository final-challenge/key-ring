from password_strength import PasswordPolicy

policy = PasswordPolicy.from_names(
    length=9,  # min length: 9
    uppercase=2,  # need min. 2 uppercase letters
    numbers=2,  # need min. 2 digits
    special=1,  # need min. 2 special characters
)

