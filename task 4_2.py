#Assign True or False to the variables "small" and "green"
#Write an if/else statement to print out which of these below corresponds to them:
# cherry, pea, watermelon, pumpkin
# ex. cherry =>small
# ex. pea =>small, green

small_set={'cherry', 'pea'}
green_set={'pea', 'watermelon'}
if 'cherry' in small_set:
    print("cherry is small")
else:
    print("cherry is not small")

if 'cherry' in green_set:
    print("cherry is green")
else:
    print("cherry is not green")
print("\n")

if 'pea' in small_set:
    print("pea is small")
else:
    print("pea is not small")

if 'pea' in green_set:
    print("pea is green")
else:
    print("pea is not green")
print("\n")

if 'watermelon' in small_set:
    print("watermelon is small")
else:
    print("watermelon is not small")

if 'watermelon' in green_set:
    print("watermelon is green")
else:
    print("watermelon is not green")
print("\n")

if 'pumpkin' in small_set:
    print("pumpkin is small")
else:
    print("pumpkin is not small")

if 'pumpkin' in green_set:
    print("pumpkin is green")
else:
    print("pumpkin is not green")
