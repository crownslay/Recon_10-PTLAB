decimal = [f"0x{i:x}.a.hackycorp.com" for i in range(256)]

# Write the output to a file
with open("output.txt", "w") as file:
    for address in decimal:
        file.write(address + "\n")

print("Output written to 'output.txt'")