bank_value = input()

last = bank_value[:-1]
second_to_last = bank_value[:-2] + bank_value[-1]

print(max(int(bank_value), int(last), int(second_to_last)))