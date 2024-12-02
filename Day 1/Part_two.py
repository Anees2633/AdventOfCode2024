# Function to calculate the similarity score
def calculate_similarity_score(left_list, right_list):
    # Count occurrences of each number in the right list
    right_counts = {}
    for num in right_list:
        if num in right_counts:
            right_counts[num] += 1
        else:
            right_counts[num] = 1

    # Calculate similarity score
    similarity_score = 0
    for num in left_list:
        if num in right_counts:
            similarity_score += num * right_counts[num]
    return similarity_score

# Read input file
file_path = r"D:\Advent of Code\Day 1\input.txt"
with open(file_path, "r") as file:
    data = file.readlines()

# Parse the input into two separate lists
left_list = []
right_list = []
for line in data:
    left, right = map(int, line.strip().split())
    left_list.append(left)
    right_list.append(right)

# Calculate similarity score
similarity_score = calculate_similarity_score(left_list, right_list)

# Print the result
print("Similarity Score:", similarity_score)
