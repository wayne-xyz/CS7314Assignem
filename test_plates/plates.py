def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len[0].isalpha==False:
        return False
    if len(s)<2 or len(s)>6:
        return False
    if s[0].isdigit() or s[1].isdigit():
        return False
    i=0
    while i<len(s):
        if s[i].isdigit() or s[i].isalpha() :
            if s[i]==" ": return False
            if s[i].isdigit() and i<len(s)-1 and s[i+1].isalpha():return False
        else:
            return False
        if s[i]=="0" and s[i-1].isalpha():
            return False
        i=i+1
    return True

if __name__ == "__main__":
    main()
