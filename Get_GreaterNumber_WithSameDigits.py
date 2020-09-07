from datetime import datetime


def get_next(number):
    lst_digit = list(str(number))
    flag = True
    end_position = len(lst_digit)
    start_position = end_position - 2
    while start_position >= 0:
        if flag:
            greater_digit = [e for e in lst_digit[start_position + 1:end_position] if e > lst_digit[start_position]]
            if greater_digit:
                index = start_position + lst_digit[start_position:end_position].index(min(greater_digit))
                lst_digit[start_position], lst_digit[index] = lst_digit[index], lst_digit[start_position]
                if end_position - start_position > 2:
                    flag = False
                    continue
                yield int(''.join(lst_digit))
            else:
                start_position -= 1
        else:
            start_position += 1
            smaller_digit = [e for e in lst_digit[start_position + 1:end_position] if e < lst_digit[start_position]]
            if smaller_digit:
                index = start_position + lst_digit[start_position:end_position].index(min(smaller_digit))
                lst_digit[start_position], lst_digit[index] = lst_digit[index], lst_digit[start_position]
            if end_position - start_position == 2:
                flag = True
                yield int(''.join(lst_digit))

                
if __name__ == '__main__':

    n = 125467864325457257957924581757579354792357457957943557
    gen = get_next(n)

    t1 = datetime.now()
    for i in range(1000000):
        next(gen)
    print(datetime.now() - t1)
