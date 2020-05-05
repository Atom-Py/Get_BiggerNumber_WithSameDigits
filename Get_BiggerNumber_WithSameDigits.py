def get_next(positive_number):
    try:
        lst_digit = list(map(int, str(positive_number)))
    except Exception:
        return None

    relay = True
    end_pos = len(lst_digit)
    start_pos = end_pos - 2
    while start_pos >= 0:
        if relay:
            biger = [e for e in lst_digit[start_pos + 1:end_pos] if e > lst_digit[start_pos]]
            if biger:
                index = start_pos + lst_digit[start_pos:end_pos].index(min(biger))
                lst_digit[start_pos], lst_digit[index] = lst_digit[index], lst_digit[start_pos]
                if end_pos - start_pos > 2:
                    relay = False
                    continue
                return int(''.join(str(e) for e in lst_digit))
            else:
                start_pos -= 1
        else:
            start_pos += 1
            smaller = [e for e in lst_digit[start_pos + 1:end_pos] if e < lst_digit[start_pos]]
            if smaller:
                index = start_pos + lst_digit[start_pos:end_pos].index(min(smaller))
                lst_digit[start_pos], lst_digit[index] = lst_digit[index], lst_digit[start_pos]
            if end_pos - start_pos == 2:
                relay = True
                return int(''.join(str(e) for e in lst_digit))
    return None

numb = '12345678901234567899999999676234615764756456250685780524585745785748675469790257904579045436547658687987655443'
# print 10000 numbers
for i in range(0,10000):
    numb = get_next(numb)
    print(numb)