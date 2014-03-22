def merge_files(file_to_read1, file_to_read2, file_to_write):
    file_read1 = open(file_to_read1, "r")
    file_write = open(file_to_write, "w")
    file_read2 = open(file_to_read2, "r")
    content1 = file_read1.read()
    content2 = file_read2.read()
    data = content1 + content2
    file_write.write(data)
    file_read1.close()
    file_read2.close()
    file_write.close()
    return data
