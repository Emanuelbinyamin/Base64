import base64

# Step 1: Encode a string into Base64

my_text = "Hello world"
my_text = my_text.encode("ascii")  # Convert the string into bytes using ASCII encoding
print(my_text)  # Outputs the byte representation of the string

my_text_encode_b64 = base64.b64encode(my_text)
# Base64 encode the byte string. Note that Base64 is not encryption;
# it's a way to convert binary data to text, making it safe for transmission over text-based protocols.
# There is no secret key involved, so anyone can decode it back.

print(my_text_encode_b64)  # Outputs the Base64 encoded string in bytes

# Step 2: Decode the Base64 string back to its original form

my_text_decode_b64 = base64.b64decode(my_text_encode_b64)
# Decode the Base64 encoded string back to its original byte form

print(my_text_decode_b64)  # Outputs the decoded byte string (original "Hello world")

# Step 3: Working with binary data (e.g., an image file)

# Read an image file in binary mode ('rb' mode)
with open("image_NueralNine.png", "rb") as f:
    data = f.read()  # Read the image data as bytes

# Create a copy of the image by writing the binary data to a new file
with open("copyOf_image_NueralNine.png", "wb") as f:
    f.write(data)  # Write the binary data to a new file in 'wb' mode (write binary)

# Optional: You could print the binary data to see what it looks like
# print(data)  # Example output: b'\xff\xd8\xff\xe0\x00\x10JFIF...'

# Step 4: Encode the binary data into Base64

# Base64 encode the binary data (image)
transmitted_data = base64.b64encode(data)# Example output: b'iVBORw0KGgoAAAANSUhEUgAAA...'

# Decode the transmitted Base64 data back to its original binary form
original_data = base64.b64decode(transmitted_data)
print(original_data)  # Outputs the original binary data of the image file
