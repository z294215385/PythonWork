
import re
#编写一个正则表达式,可以检测DD/MM/YYYY格式的日期。假设日期的范围是01-31，月份的范围是01~12，年份的范围是1000~2999。请注意，如果日期或月份是一位数字，前面自动加0。
#''内的正则表达中不能添加空格，不然会被识别为匹配字符
date_rule = re.compile(r'(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[0-2])/([12][0-9]{3})')

test_date = ('21/11/2024')

# re.match(pattern, string)只检查字符串开头是否匹配模型，相当于在模式前加了^锚定符，开头不匹配则会立即返回None，即使字符串中间有匹配的内容也会被忽略
# re.search(string)在整个字符串中搜索第一个匹配项，不要求从头开始匹配，只要任意位置存在即返回匹配对象，如果没有找到任何匹配则返回None
date = re.match(date_rule, test_date)
if date != None:
    day, month, year = date.groups()
    day = int(day)
    month = int(month)
    year = int(year)

    is_valid = True

    if month in [4, 6, 9, 11] and day > 30:
        is_valid = False
    elif month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
        is_valid = False
    elif month == 2:
        if day > 29:
            is_valid = False
        elif day == 29:
            if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0): 
                is_valid = True
            else:
                is_valid = False
        else:
            is_valid = True

    if is_valid:
        print('日期有效')
    else:
        print('日期无效')
else:
    print('日期无效')

