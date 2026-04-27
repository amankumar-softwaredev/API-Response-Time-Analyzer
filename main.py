import requests
import json
import time

ifsc_code = "CNRB0001913"
url = f"https://ifsc.razorpay.com/{ifsc_code}"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
    'Accept': 'application/json',
}

total_time= []

for i in range(1,32):
    start= time.perf_counter()
    response = requests.get(url, headers=headers)
    bank_details = response.json()
    end =time.perf_counter()
    time_ms=(end-start)*1000
    print(f"{ (end-start)*1000} ms")
    total_time.append(time_ms)
    for key , value in bank_details.items():
        print(f"{key} : {value}")


print(total_time)

total_len= len(total_time)
sum_time= sum(total_time)

mean =sum_time/total_len

print(mean)

data_var=[]

for i in total_time:
    n_1=(i-mean)**2
    data_var.append(n_1)

sum_var=sum(data_var)

variance=sum_var/(total_len-1)

print(f"Variance= {sum_var/(total_len-1)}")

print(f"Standard Deviation ={variance**0.5}")

sd=variance**0.5

# now calculate range  confidence interval with 95%   using t distribution because we do not know population of data or  standard variance of population


n_req= 31
df=n_req-1
DegreeOfFreedom= df

t=2.04

# We know  cl formula is x bar +- t x s/root n 

lower = mean-t*(sd/(n_req**0.5))

upper = mean + t * (sd / (n_req**0.5))

print(f"CI Range = [{lower}, {upper}] ms")

print(f"CI Range = [{lower/1000}, {upper/1000}] Second")
