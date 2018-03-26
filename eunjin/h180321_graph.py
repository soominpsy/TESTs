import matplotlib.pyplot as plt

height = [180,165,163,174,178,185,175,160,182]
weight = [90,56,53,60,68,88,72,50,78]


#막대그래프
xs = [i for i,_ in enumerate(weight)]
plt.bar(xs,height)
plt.ylabel("height")
plt.xlabel("weight")
plt.title("graph")

plt.xticks(xs,weight)
plt.show()




# 선그래프
xs = [i for i,_ in enumerate(height)]
plt.plot(xs,weight,"b-",label = "w")
plt.plot(xs,height,"r-",label = "h")
plt.legend(loc=9)
plt.xlabel("9 people")
plt.title("height&weight")

plt.show()


#산점도
labels = ['1','2','3','4','5','6','7','8','9']
plt.scatter(weight,height)

for label,w_count,h_count in zip(labels,weight,height):
    plt.annotate(label,xy=(w_count,h_count),xytext = (10,-10),textcoords = "offset points")

plt.axis("equal")
plt.show()