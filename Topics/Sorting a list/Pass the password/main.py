# the follwing line reads the list from the input, do not modify it, please
passwords = input().split()

for password in sorted(passwords, key=len):
    print(password, len(password))
