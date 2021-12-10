class num_generator:
    def __init__(self,name):
        self.lower_bound = 0
        self.upper_bound= 0
        self.n = 0
        flag = int(input(str(name)+" :  Enter 1 for finite and any other key for infinite series  "))
        if flag == 1:
            self.finite_series()
        else:
            self.infinite_series()
            
    def display(self,name,series,n):
        print("##"*50)
        print("-----"+str(name)+" -----")
        print("n value is : ",n)
        print(name ,":","\n",series)
        flag = int(input("Do you want to calculate mean[1] or median[2]? if not type [0]?  "))
        if flag==1:
            self.mean()
        elif flag==2:
            self.Median()
        else:
            print(" ")
        print("##"*50)
    def get_range(self):
        if self.upper_bound ==0:
            self.lower_bound = int(input("please enter the lower bound:  "))
            self.upper_bound = int(input("please enter the upper bound:  "))
        else:
            return
    def get_median(series):
        n = len(series)
        if n%2!=0:
            index = int(n/2)
            return series[index]
        elif n%2==0:
            median = int(n/2)
            n1 = series[median]
            n2 = series[median-1]
            median = (n1+n2)/2
            return median

    def get_mean(series):
        n = len(series)
        if n!=0:
            return round(sum(series)/n,2)
        else:
            print("The series is empty")