def decode(message_file):
    # Open text file and read in lines
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Organize words into hash map
    pyramid = {}
    for line in lines:
        number, word = line.strip().split()
        number = int(number)
        if number not in pyramid:
            pyramid[number] = []
        pyramid[number].append(word)
    
    
    # Construct string by appending the the last index of the row
    pyramid_length = len(pyramid)
    decoded_message = []
    row = 1
    count = 0

    while count < pyramid_length:
        count = count + row
        decoded_message.extend(pyramid[count])
        row += 1

    return ' '.join(decoded_message)

message_file = "coding_qual_input.txt"
message = decode(message_file)
print("Hidden Message:" , message)