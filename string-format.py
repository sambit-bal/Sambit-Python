a = 10
print(f"my name is {a}")

print("****************Float******************")

c = 10.45
d = 16.87
print(f"{c}")
print(f"{c} {d}")
print(f"{d}  {c}")

print("****************String******************")

f_name = "Ram"
l_name = "Prasad"

print(f"{f_name}")
print(f"{f_name} {l_name}")
print(f"{l_name}  {f_name}")

name = "Hari"
age = 10
print(f"Hello My Name is {name}")
print(f"{name} {age}")
print(f"{age} {name}")

print("****************All Format******************")
num = 15
print(f"{num}")
print(f"{num:d}")
print(f"{num:5d}")
print(f"{num:05d}")
print(f"{num:+5d}")
print(f"{num:<5d}")
print(f"{num:*<5d}")
print(f"{num:*>5d}")
print(f"{num:^5d}")

print("****************All Format for float******************")

ne = 17.89
price = 19.672358916
print(f"{ne}")
print(f"{ne:f}")
print(f"{ne:8f}")
print(f"{price:.20f}")
print(f"{ne:8.3f}")
print(f"{ne:+8.2f}")
print(f"{ne:<8.2f}")
print(f"{ne:*<8.2f}")
print(f"{ne:*>8.2f}")
print(f"{ne:^8.2f}")
print(f"{ne:*^8.2f}")

print("****************All Format for string ******************")
fname = "Howrwdeed"
print(f"{fname:.3s}")
print(f"{fname:8.3s}")
print(f"{fname:*<8.3s}")
print(f"{fname:>8.3s}")
print(f"{fname:*>8.3s}")
print(f"{fname:^8.3s}")
print(f"{fname:*^8.3s}")

fprice = 1234567890
print(f"{fprice:,}")
print(f"{fprice:_}")

from datetime import datetime
today = datetime(2020, 9, 17)
print(f"{today}")
print(f"{today:%d/%b/%Y}")
