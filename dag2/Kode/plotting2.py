from pylab import arange, sin, cos, plot, show, xlim, xlabel, ylabel, title

x = arange(0, 8, 0.1)
y = sin(x)
z = cos(x)

print(x)
print(y)
print(z)

plot(x, y)
plot(x, z)
xlim(0, 7.9)
xlabel("Tid")
ylabel("Høyde")
title("Posisjon til pendel som funksjon av tid")
show()