def extraction():
    sn_d = {
        'year' : [],
        'month' : [],
        'day' : [],
        'decimalDate' : [],
        'dailySunspotNumber': [],
        'standardDeviation': [],
        'numberOfObservations': [],
        'indicator': [],
    }

    sn_m = {
        'year' : [],
        'month' : [],
        'decimalDate' : [],
        'monthSunspotNumber': [],
        'standardDeviation': [],
        'numberOfObservations': [],
        'indicator': [],
    }

    with open('sn_d.txt', 'r') as file:
        for line in file:
           sn_d['year'].append(int(line[0:4]))
           sn_d['month'].append(int(line[5:7]))
           sn_d['day'].append(int(line[8:10]))
           sn_d['decimalDate'].append(float(line[11:19]))
           sn_d['dailySunspotNumber'].append(int(line[21:24]))
           sn_d['standardDeviation'].append(float(line[25:30]))
           sn_d['numberOfObservations'].append(int(line[32:35]))
           sn_d['indicator'].append(line[36])

    with open('sn_m.txt', 'r') as file:
        for line in file:
           sn_m['year'].append(int(line[0:4]))
           sn_m['month'].append(int(line[5:7]))
           sn_m['decimalDate'].append(float(line[8:16]))
           sn_m['monthSunspotNumber'].append(float(line[18:23]))
           sn_m['standardDeviation'].append(float(line[24:29]))
           sn_m['numberOfObservations'].append(int(line[31:35]))
           sn_m['indicator'].append(line[36])
    
    return (sn_d, sn_m)

def noSunspotsPerMonth (year):
    result = '\nErro: The year has to be an integer between 1818 and 2018\n'
    if (int(year) >= 1818 or int(year) <= 2018):
        
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']      
        aux = extraction()
        line = len(aux[0]['year'])
        dayNoSunspots =[0,0,0,0,0,0,0,0,0,0,0,0]
        
        for i in range(line):
            if (aux[0]['year'][i] == int(year)):
                for j in range(1,13):
                    if (aux[0]['month'][i] == j):
                            if (aux[0]['dailySunspotNumber'][i] == 0):
                                dayNoSunspots[j-1] += 1

        result ='{}\n'.format('-'*100)
        result += '{:^100}\n'.format('Number of days per month that no sunspot was found in the year of {}'.format(year))
        result +='{}\n'.format('-'*100)
        
        for i in range(12):
            result += '{:<10} : {:<3}{}\n'.format(months[i], dayNoSunspots[i], 'days')
        
        result +='{}\n'.format('-'*100)
    
    return result

def periodNoSunspot():
    aux = extraction()
    line = len(aux[0]['year'])
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    dayNoSunspots =[0,0,0,0,0,0,0,0,0,0,0,0]
    
    years = []
    list_result = [] 
    maximum = 0
    result = ''

    for i in range(line):
        
        if (aux[0]['year'][i]  in years):
            for j in range(1,13):
                if(aux[0]['month'][i] == j):
                    if(aux[0]['dailySunspotNumber'][i] == 0):
                        dayNoSunspots[j-1] += 1
        
        if (aux[0]['year'][i] not in years):
            years.append(aux[0]['year'][i]) 
            list_result.append(dayNoSunspots) 
            dayNoSunspots =[0,0,0,0,0,0,0,0,0,0,0,0] 

    
    for i in range(len(list_result)):
        for j in range(0,12):
            if(list_result[i][j] >= maximum):
                maximum = list_result[i][j]
                i_max = i
                j_max = j
    
    result ='{}\n'.format('-'*100)
    result += '{:^100}\n'.format('The year and month that had the most days without sunspots was the year {} and month of {}'.format(years[i_max-1], months[j_max]))
    result +='{}\n'.format('-'*100)

    return result

def periodMaxSunspots():
    aux = extraction()
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    line = len(aux[1]['year'])
    
    maximum = 0
    result = ''

    for i in range(line):
        if(aux[1]['monthSunspotNumber'][i] >= maximum):
            maximum = aux[1]['monthSunspotNumber'][i]
            i_max = i

    
    result ='{}\n'.format('-'*100)
    result += '{:^100}\n'.format('The year and month that had the most sunspots was the year {} and the month of {}'.format(aux[1]['year'][i_max], months[aux[1]['month'][i_max]-1]))
    result +='{}\n'.format('-'*100)
    
    return result

def periodMaxAndMinSunspots(period):
    result = '\nErro: invalid period\n'
    if(period[2] == '-' and period[7] == '/' and period[10] == '-'):
        try:

            month_min = int(period[0:2])
            year_min = int(period[3:7])
            month_max = int(period[8:10])
            year_max = int(period[11:])

            if(month_min > 12 or month_min < 1 or month_max > 12 or month_max < 1):
                result = '\nErro: invalid period\n'
            elif( year_min > 2020 or year_min < 1749 or year_max > 2020 or year_max < 1749):
                result = '\nErro: invalid period\n'
            elif(year_min > year_max):
                return  '\nErro: invalid period\n'
            elif(year_min == year_max and month_min >= month_max):
                return  '\nErro: invalid period\n'
            elif(year_max == 2020 and month_max > 5):
                return  '\nErro: invalid period\n'
            elif(year_min == 2020 and month_min > 5):
                return  '\nErro: invalid period\n'
            else:

                months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
                aux = extraction()
                line = len(aux[1]['year'])
                result = ''
                index = aux[1]['year'].index(year_min)
                maximum = minimum = aux[1]['monthSunspotNumber'][index]
                
                for i in range(line):
                    if(aux[1]['year'][i] >= year_min and aux[1]['year'][i] <= year_max):
                        if(aux[1]['month'][i] >= month_min and aux[1]['month'][i] <= month_max):
                            if(aux[1]['monthSunspotNumber'][i] >= maximum):
                                maximum = aux[1]['monthSunspotNumber'][i]
                                i_max = i
                            if(aux[1]['monthSunspotNumber'][i] <= minimum):
                                minimum = aux[1]['monthSunspotNumber'][i]
                                i_min = i
                            
                result ='{}\n'.format('-'*100)
                result += '{:^100}\n'.format('Between {} {} to {} {} the maximum sunspot was {} and the minimum sunspot was {}'.format(months[month_min-1], year_min, months[month_max-1], year_max, maximum, minimum))
                result +='{}\n'.format('-'*100)

        except ValueError:
            result ='\nErro: invalid period\n'
    
    return result

    
def monthlyAverage(year):

    result = '\nErro: The year has to be an integer between 1818 and 2018\n'
    if (int(year) >= 1818 or int(year) <= 2018):
        aux = extraction()
        line = len(aux[0]['year'])
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


        result = ''
        result +='{}\n'.format('-'*100)
        result += '{:^100}\n'.format('The average number of sunspots per month in the year {}'.format(year))
        result +='{}\n'.format('-'*100)
        
        sum = 0.0
        cont = 0
        cont_day = []
        sum_month = []
        for j in range(1,13):
            for i in range(line):
                if (aux[0]['year'][i] == int(year)):
                    if(aux[0]['month'][i] == j):
                            sum += aux[0]['dailySunspotNumber'][i] 
                            cont += 1   
                
            sum_month.append(sum)
            sum = 0.0
            cont_day.append(cont)
            cont = 0

        if( int(year) != 2018):
            for i in range(12):
                result += '{:<10} : {:<5.2f}{}\n'.format(months[i], sum_month[i]/cont_day[i], ' sunspots per day') 
        if( int(year) == 2018):
            for i in range(10):
                result += '{:<10} : {:<5.2f}{}\n'.format(months[i], sum_month[i]/cont_day[i], ' sunspots per day') 
        
        result +='{}\n'.format('-'*100)
    
    return result


def monthlyStandardDeviation():
    aux = extraction()
    line = len(aux[1]['year'])
    sum = 0.0

    result = ''
    result +='{}\n'.format('-'*100)
    result += '{:^100}\n'.format('The standard deviation of the number of sunspots per month')
    result +='{}\n'.format('-'*100)
    
    for j in range(line):
        sum += aux[1]['monthSunspotNumber'][j]
    
    average = sum/line
    aux2  = 0.0

    for j in range(line):    
        aux2 += (abs(aux[1]['monthSunspotNumber'][j] - average))**2
    
    standardDeviation = (aux2/line)**0.5

    result += '{:<10} : {:<5.3}{}\n'.format('Standard Deviation', standardDeviation, 'sunspots')
    
    return result

def userInterface():
    result = ''
    result += '{}\n'.format('-'*100)
    result += '{:^100}\n'.format('Welcome to the sunspot database')
    result += '{}\n'.format('-'*100)
    
    result += '1: Show the number of sunspots in a given year;\n'
    result += '2: Show the year and month that had the most days without sunspots;\n'
    result += '3: Show the year and month that had the most sunspots;\n'
    result += '4: Show the maximum and minimum sunspots in a given period;\n'
    result += '5: Show the monthly average for each month, for a given year;\n'
    result += '6: Show the standard deviation of daily observations;\n'
    result += '7: Exit.\n'
    
    result += '{}\n'.format('-'*100)
    result += '{:^100}\n'.format('Please, select an option')
    result += '{}\n'.format('-'*100)
    
    result += 'Option: '
    option = input(result)
    
    return (result, option)

def main():
    aux = userInterface()
    result = ''
    
    try:
        option = int(aux[1])
        if(option == 1):
            print('Year: ')
            year = input()
            result += noSunspotsPerMonth(year)
        
        elif(option == 2):
            result += periodNoSunspot()
        
        elif(option == 3):
            result += periodMaxSunspots()
        
        elif(option == 4):
            print('Period: ')
            period = input()
            result += periodMaxAndMinSunspots(period)
        
        elif(option == 5):
            print('Year: ')
            year = input()
            result += monthlyAverage(year)
        
        elif(option == 6):
            result += monthlyStandardDeviation()
        
        elif(option == 7):
            result += '{}\n'.format('\nGoodbye!')
        
        else:
            result += '\n{}\n'.format('Invalid option')
    
    except ValueError:
        result = '\n{}\n'.format('Invalid option')

    print(result)



main()