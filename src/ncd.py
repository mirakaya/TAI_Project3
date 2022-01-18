import os

class NCD:
    def __init__(self) -> None:
        pass

    def run():

        compr_concat_files = os.listdir("Compressed_concat_files")

        ncd_list = []

        for i in compr_concat_files:

            aux = i.split("_")

            first_file = aux[0]
            second_file = aux[1]

            concat_size = os.path.getsize("Compressed_concat_files/" + i)

            first_file_size = os.path.getsize("Compressed_files/" + first_file)
            second_file_size = os.path.getsize("Compressed_files/" + second_file)

            ncd = (concat_size - min(first_file_size, second_file_size)) / max(first_file_size, second_file_size)

            ncd_list.append([ncd, first_file,second_file])

        ncd_list = sorted(ncd_list, key = lambda x: x[0])
        print(ncd_list)
        return ncd_list[0]