# Hezekiah Branch
# May 16, 2020

# Calculate IQR
# This was a fun challenge to calculate the Interquartile Range (IQR) # which is a topic covered in elementary statistics.

print("Let's calculate the IQR!\n")

data = []
observation = " "

print("Enter the numbers from your data set")
print("To stop adding observations, type 'END'\n")

# Get the input for data
while (observation.lower() != "end"):
    observation = input("Add a number: ")
    if (observation.lower() != "end"):
        data.append(float(observation))

# Sort the data from least to greatest -> O(n)
data.sort()

# Find the median
def find_median(data):
    length = len(data)
    median_index = int((length / 2))
    if (length % 2 == 0):
        median1 = data[median_index]
        median2 = data[median_index - 1]
        median = ((median1) + (median2)) / 2
    else:
        median = data[median_index]
    return median

# Find the upper and lower median
upper = []
lower = []
median = find_median(data)
for observation in data:
    if (observation > median):
        upper.append(observation)
    elif (observation < median):
        lower.append(observation)

Q3 = find_median(upper)
Q1 = find_median(lower)

# Calculate and display the IQR
IQR = Q3 - Q1
print("\nIQR: ", IQR)
print("25th Percentile: ", Q1)
print("50th Percentile: ", median)
print("75th Percentile: ", Q3)

