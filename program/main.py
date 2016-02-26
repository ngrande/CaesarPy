
class CaeserEncryption:

    _alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, key):
        self.key = key
        self.key = self._remove_duplicates(key)
        self.key_alphabet = self._generate_key_alphabet(self.key)

    def _remove_duplicates(self, input):
        input = input.upper()
        return "".join(sorted(set(input), key=input.index))

    def _generate_key_alphabet(self, unique_input):
        unique_input = unique_input.upper()
        length = len(unique_input)
        alphabet_length = len(self._alphabet)
        diff = alphabet_length - length

        reversed_alphabet = self._alphabet[::-1]

        i = 0
        while len(unique_input) < 26:
            if not reversed_alphabet[i] in unique_input:
                unique_input += reversed_alphabet[i]
            # else:
            i += 1

        return unique_input
