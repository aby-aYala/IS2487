# list of lists, aka nested list
data = [
    [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3]
]

# Date, hi, lo
# [23-11-01, 50,30]


processed_data = []
total_temp = 0
count = 0
# record is the variable used to hold the element in our list called data
for record in data:
    date, hi, lo = record

    # or otherwise written as
    date = [0]
    hi = [1]
    lo = [2]

    avg_temp = (hi + lo) / 2

    processed_data.appnd([date, hi, lo, avg_temp])
    total_temp += avg_temp
    count += 1
print()
newInput = input("")
