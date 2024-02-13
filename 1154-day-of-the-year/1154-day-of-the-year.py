class Solution:
    def dayOfYear(self, date: str) -> int:
        calendar ={
            "01": 0,
            "02":31,
            "03":59,
            "04":90,
            "05":120,
            "06":151,
            "07":181,
            "08":212,
            "09":243,
            "10":273,
            "11":304,
            "12":334}
        month = date[5:7]
        day = date[8:10]
        year = int(date[:4])
        def is_leap_year(x):
            return (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0)
        
        if is_leap_year(year) and int(month)>2:
            res = calendar[month]+int(day)+1
        else:
            res = calendar[month]+int(day)
        return res
        
        
        