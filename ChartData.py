class ChartData(object):
    @staticmethod
    def get_sales(method):
        result = []
        for i in method:
            result.append(int(i[3]))
        return result

    @staticmethod
    def get_weight(method):
        normal = 0
        over = 0
        obese = 0
        under = 0
        for i in method:
            if i[4] == 'Normal':
                normal += 1
            elif i[4] == 'Overweight':
                over += 1
            elif i[4] == 'Obesity':
                obese += 1
            elif i[4] == 'Underweight':
                under += 1
        return [normal, over, obese, under]

    @staticmethod
    def get_gender(method):
        m = 0
        f = 0
        for i in method:
            if i[1] == 'M':
                m += 1
            elif i[1] == 'F':
                f += 1
        return [m, f]
