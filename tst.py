at = 10  # Your initial value of 'at'
ax = 10  # The value to add to 'at' in each iteration
ax_counter = 0  # Counter for 'ax'

while at < 200:
    at += ax
    ax_counter += ax

    if ax_counter >= 20:
        at -= 1
        ax_counter = 0

    # If 'at' exceeds 200, set it to 200
    if at > 200:
        at = 200

    print(at)

print("Reached 200")
