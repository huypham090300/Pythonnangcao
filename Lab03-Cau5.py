f = open('E:/HUY/PythonNC/Pythonnangcao/Lab03/Chuong10/hebron.txt')
def smallest_value_skip(reader):
    line = f.skip_header(reader).strip()
    if line != '':
        smallest = int(line)
    for line in reader:
        line = line.strip()
        if line != '-':
            value = int(line)
            smallest = min(smallest, value)
    return smallest
if __name__ == '__main__':
    print(smallest_value_skip(f))
    f.close()
