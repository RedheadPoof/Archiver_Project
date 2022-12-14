
def zip_string(processed_string):
    symbol_of_string_number = 0
    additional_sequence = {}
    number_additional_sequence = 256
    compress_list_bytes = bytearray()
    while symbol_of_string_number < len(processed_string):
        compressed_sequence = processed_string[symbol_of_string_number]
        while symbol_of_string_number + 1 < len(processed_string):
            processed_sequence = compressed_sequence + processed_string[symbol_of_string_number + 1]
            if processed_sequence in additional_sequence:
                compressed_sequence = processed_sequence
                symbol_of_string_number += 1
            else:
                if number_additional_sequence < 256 * 256:
                    additional_sequence[processed_sequence] = str(number_additional_sequence)
                    number_additional_sequence += 1
                break
        if len(compressed_sequence) != 1:
            compress_sequense = int(additional_sequence[compressed_sequence])
        else:
            compress_sequense = ord(compressed_sequence)
            if compress_sequense >= 256:
                print(f"Text encoding is not UTF-8, compression is not performed: '{compressed_sequence}'")
                compress_list_bytes = ""
                return compress_list_bytes
        compress_bytes = compress_sequense.to_bytes(2, byteorder="big")
        compress_list_bytes += compress_bytes
        symbol_of_string_number += 1
    return compress_list_bytes


def unzip_string(processed_list_bytes):
    processed_list = list(processed_list_bytes)
    additional_sequence = {}
    number_additional_sequence = 256
    processed_sequence = chr(processed_list[0] * 256 + processed_list[1])
    uncompressed_string = processed_sequence
    for counter_list in range(2, len(processed_list), 2):
        processed_counter = processed_list[counter_list] * 256 + processed_list[counter_list + 1]
        if processed_counter < 256:
            uncompressed_sequence = chr(processed_counter)
        else:
            if processed_counter < number_additional_sequence:
                uncompressed_sequence = additional_sequence[processed_counter]
            elif processed_counter == number_additional_sequence:
                uncompressed_sequence = processed_sequence + processed_sequence[0]
            else:
                print(processed_counter)
                continue
        processed_sequence += uncompressed_sequence[0]
        uncompressed_string += uncompressed_sequence
        if (processed_sequence not in additional_sequence) & (number_additional_sequence < 256 * 256):
            additional_sequence[number_additional_sequence] = processed_sequence
            number_additional_sequence += 1
        processed_sequence = uncompressed_sequence
    return uncompressed_string
