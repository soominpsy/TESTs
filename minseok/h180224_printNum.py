import matplotlib. pyplot6 as plt

movies=['Annie','Ben-hur','Casablanca','gandhi','west side story']
num_oscars = [5,11,3,8,10]

xs = [i+0.1 for i, _ in enumerate(movies)]

plt.bar(xs.num_oscars)
plt.ylabel("# of academy awards")
plt.title("My favarite movies")

plt.xticks([i+0.1 for i, _ in enumerate(movies)],movies)
plt.show()