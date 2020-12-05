import re

def validate_1(passport : str) -> bool:
    result = False

    if "ecl:" in passport and "pid:" in passport and "eyr:" in passport and "hcl:" in passport and \
            "byr:" in passport and "iyr:" in passport and "hgt:" in passport:
        result = True

    return result


def validate_2(passport: str) -> bool:
    return check_ecl(passport) and check_pid(passport) and check_eyr(passport) and check_hcl(passport) \
           and check_byr(passport) and check_iyr(passport) and check_hgt(passport)


def check_hgt(passport: str) -> bool:
    hgt = extract("hgt:", passport)
    result = False
    if hgt.endswith("cm"):
        value = hgt.split("cm")[0]
        result = (int(value) >= 150) and (int(value) <= 193)
    if hgt.endswith("in"):
        value = hgt.split("in")[0]
        result = (int(value) >= 59) and (int(value) <= 76)
    return result


def check_iyr(passport: str) -> bool:
    iyr = extract("iyr:", passport)
    return (int(iyr) >= 2010) and (int(iyr) <= 2020)


def check_byr(passport: str) -> bool:
    byr = extract("byr:", passport)
    return (int(byr) >= 1920) and (int(byr) <= 2002)


def check_hcl(passport: str) -> bool:
    hcl = extract("hcl:", passport)
    return re.match(r'^#[a-f0-9]{6}$', hcl)


def check_eyr(passport: str) -> bool:
    eyr = extract("eyr:", passport)
    return (int(eyr) >= 2020) and (int(eyr) <= 2030)


def check_pid(passport: str) -> bool:
    pid = extract("pid:", passport)
    return pid.isdigit() and (len(pid) == 9)


def check_ecl(passport: str) -> bool:
    ecl = passport.split("ecl:")[1].split(" ")[0]
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl","oth"]


def extract(passport_field: str, input_str: str) -> str:
    return input_str.split(passport_field)[1].split(" ")[0]


def read_file(input_file_name: str) -> []:

    result_list = []
    jobber = ""
    with open(input_file_name, 'r') as input_file:
        for line in input_file:
            if line == '\n':
                result_list.append(jobber)
                jobber = ""
            jobber = jobber + " " + line.strip()
    input_file.close()
    result_list.append(jobber)
    return result_list


def question_one():
    print("---- Question 1 ----")
    count = 0
    for passport in list_of_passports:
        if validate_1(passport):
            count += 1
    print("valid passports: ", count)


def question_two():
    print("---- Question 2 ----")
    count = 0
    for passport in list_of_passports:
        if validate_1(passport):
            if validate_2(passport):
                count += 1
    print("valid passports: ", count)


if __name__ == '__main__':
    list_of_passports = read_file("input.txt")
    question_one()
    question_two()
    print((2020 <= int("2024")) and (2030 >= int("2024")))