def read_lines(filename:str)->list[str]:
    lines:list[str] = []
    with open(filename, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line != '':
                lines.append(line)
    return lines

def parse_line(line:str)->tuple[str, list[int]]:
    grades:list[int] = []
    subject, str_grades = line.split(':')
    for grade in str_grades.split(','):
        grades.append(int(grade))
    return subject, grades

def average(values:list[int])->float|None:
    if len(values) == 0:
        return None
    sum=0
    for i in values:
        sum+=i
    average=sum / len(values)
    return average

def load_grades(filename:str):
    lines = read_lines(filename)
    for line in lines:
        parse_line(line)
    #TODO

if __name__ == '__main__':
# print(read_lines(r'C:\Users\lukim\Desktop\skola\znamky\znamky.txt'))
    # print(parse_line('CJ:5, 4, 1, 3'))
    print(average([1,2,3]))