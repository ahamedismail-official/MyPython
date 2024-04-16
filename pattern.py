def generate_ap(n, a, d):
    ap_list = [a + i * d for i in range(n)]
    return ap_list


if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))
    a = int(input("Enter the first term: "))
    d = int(input("Enter the common difference: "))
    ap_sequence = generate_ap(n, a, d)
    print("Generated Arithmetic Progression:")
    print(" ".join(map(str, ap_sequence)))
    sum_of_elements = sum(ap_sequence)
    print("Sum of elements:", sum_of_elements)
