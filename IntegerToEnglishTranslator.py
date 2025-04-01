class Solution:
    def digit(self, num):
        if num == "1":
            return "One"
        if num == "2":
            return "Two"
        if num == "3":
            return "Three"
        if num == "4":
            return "Four"
        if num == "5":
            return "Five"
        if num == "6":
            return "Six"
        if num == "7":
            return "Seven"
        if num == "8":
            return "Eight"
        if num == "9":
            return "Nine"
        return ""
    
    def double_digit(self, num):
        if num[0] == "0":
            return self.digit(num[1])
        if num[0] == "1":
            if num[1] == "0":
                return "Ten"
            if num[1] == "1":
                return "Eleven"
            if num[1] == "2":
                return "Twelve"
            if num[1] == "3":
                return "Thirteen"
            if num[1] == "4":
                return "Fourteen"
            if num[1] == "5":
                return "Fifteen"
            if num[1] == "6":
                return "Sixteen"
            if num[1] == "7":
                return "Seventeen"
            if num[1] == "8":
                return "Eighteen"
            if num[1] == "9":
                return "Nineteen"
        if num[0] == "2":
            return "Twenty " + self.digit(num[1])
        if num[0] == "3":
            return "Thirty " + self.digit(num[1])
        if num[0] == "4":
            return "Forty " + self.digit(num[1])
        if num[0] == "5":
            return "Fifty " + self.digit(num[1])
        if num[0] == "6":
            return "Sixty " + self.digit(num[1])
        if num[0] == "7":
            return "Seventy " + self.digit(num[1])
        if num[0] == "8":
            return "Eighty " + self.digit(num[1])
        if num[0] == "9":
            return "Ninety " + self.digit(num[1])
        return ""
    
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        word = ""
        
        num = str(num)
        index = len(num)

        while index > 0:
            temp = ""

            if index > 24 and index < 28 and (index != 27 or num[len(num)-27:len(num)-24] != "000"):
                if num[len(num)-24:] == "000000000000000000000000":
                    temp += " Septillion"
                else:
                    temp += " Septillion "
            if index > 21 and index < 25 and (index != 24 or num[len(num)-24:len(num)-21] != "000"):
                if num[len(num)-21:] == "000000000000000000000":
                    temp += " Sextillion"
                else:
                    temp += " Sextillion "
            if index > 18 and index < 22 and (index != 21 or num[len(num)-21:len(num)-18] != "000"):
                if num[len(num)-18:] == "000000000000000000":
                    temp += " Quintillion"
                else:
                    temp += " Quintillion "
            elif index > 15 and index < 19 and (index != 18 or num[len(num)-18:len(num)-15] != "000"):
                if num[len(num)-15:] == "000000000000000":
                    temp += " Quadrillion"
                else:
                    temp += " Quadrillion "
            elif index > 12 and index < 16 and (index != 15 or num[len(num)-15:len(num)-12] != "000"):
                if num[len(num)-12:] == "000000000000":
                    temp += " Trillion"
                else:
                    temp += " Trillion "
            elif index > 9 and index < 13 and (index != 12 or num[len(num)-12:len(num)-9] != "000"):
                if num[len(num)-9:] == "000000000":
                    temp += " Billion"
                else:
                    temp += " Billion "
            elif index > 6 and index < 10 and (index != 9 or num[len(num)-9:len(num)-6] != "000"):
                if num[len(num)-6:] == "000000":
                    temp += " Million"
                else:
                    temp += " Million "
            elif index > 3 and index < 7 and (index != 6 or num[len(num)-6:len(num)-3] != "000"):
                if num[len(num)-3:] == "000":
                    print(index)
                    temp += " Thousand"
                else:
                    temp += " Thousand "
            
            if index % 3 == 0:
                chunk = num[len(num)-index:len(num)-index+3]
                index -= 3
            else:
                chunk = num[:index%3]
                index -= index % 3
            
            if len(chunk) == 1:
                temp = self.digit(chunk) + temp
            else:
                if chunk[len(chunk)-1] == "0" and chunk[len(chunk)-2] != "1":
                    temp2 = self.double_digit(chunk[len(chunk)-2:])
                    temp = temp2[:len(temp2)-1] + temp
                else:
                    temp = self.double_digit(chunk[len(chunk)-2:]) + temp

            if len(chunk) == 3 and chunk[0] != "0":
                if chunk[1:] == "00":
                    temp = self.digit(chunk[0]) + " Hundred" + temp
                else:
                    temp = self.digit(chunk[0]) + " Hundred " + temp

            word += temp
        
        return word
