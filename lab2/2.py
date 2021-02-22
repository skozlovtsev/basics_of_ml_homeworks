import sklearn.preprocessing as sp

input_labels = ["red", "black", "red", "green", "black", "yellow", "white"]

encoder = sp.LabelEncoder()
encoder.fit(input_labels)
text_labels = ["green", "red", "black"]
encoded_values = encoder.transform(text_labels)

print("\nLabels =", text_labels)
print("Encoded values =", list(encoded_values))

encoded_values = [3, 0, 4, 1]
decoded_list = encoder.inverse_transform(encoded_values)

print("\nEncoded values =", encoded_values)
print("\nDecoded labels =", list(decoded_list))