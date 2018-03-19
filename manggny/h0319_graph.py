import matplotlib.pyplot as plt

height = [180, 165, 163, 174, 178, 185, 175, 160, 182]
weight =  [90, 56, 53, 60, 68, 88, 72, 50, 78]
labels = ['a','b','c','d','e','f','g','h','i']

plt.scatter(height,weight)

#레이블을 달자 !
for label, height_count, weight_count in zip(labels,height,weight):
    plt.annotate(label,xy=(height_count,weight_count),xytext=(5,-5),textcoords='offset points')

plt.title("height vs. weight")
plt.xlabel("height")
plt.ylabel("weight")
plt.show() # 산점도는 같이 증가하는 여부 보기 적당, 개인적으로 경향을 보기 가장 적당한 그래프라고 생각

## 밑에는 선그래프
xs = [i for i, _ in enumerate(height)]
plt.plot(xs,height,"g-",label = 'height')
plt.plot(xs,weight,"r:",label = 'weight')
plt.legend(loc=9)
plt.title("height vs. weight")
plt.show() # 몸무게와 키의 단위가 달라서 선그래프로 비교하기 별로임

## 밑에는 막대그래프
def sort_with(x,y): # 우선 같이 정렬되는 함수 구현, 즉 x는 작은것부터 큰 순서대로 정렬, y는 x순서에따라 같이 정렬
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i]>x[j]:
                k1 = x[i]
                x[i] = x[j]
                x[j] = k1
                k2 = y[i]
                y[i] = y[j]
                y[j] = k2
            else:
                continue

sort_with(height,weight)

group = ['low','mid','high'] #키를 작음, 중간, 높음으로 설정
value = [(weight[i]+weight[i+1]+weight[i+2])/3 for i in range(0,9,3)] # 세 그룹으로 나눠 그룹 값 평균
xs2 = [i+0.1 for i, _ in enumerate(value)] #바가 들어갈 위치 지정
plt.bar(xs2,value)
plt.ylabel("mean weight")
plt.title("weight vs. height")
plt.xticks(xs2,group)
plt.show()
'''
결론: 키와 몸무게의 증가 간에 상관관계 혹은 회귀분석을 위해서는 산점도가 우수하나,
만약 도출하고 싶은 결과가 키 큰 그룹일 수록 몸무게가 무겁다는 통계 분석을 원한다면
그룹을 나눠서 하는 막대그래프가 유리할 수 있다, 그러나 귀찮.. 
'''