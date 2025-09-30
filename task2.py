import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return  np.sin(x ** 2) + 0.5 * x

a = 1  # Нижня межа
b = 4  # Верхня межа

def monte_carlo_integration(func, a, b, num_samples=100000):
    samples = np.random.uniform(a, b, num_samples)
    sample_values = func(samples)
    integral = (b - a) * np.mean(sample_values)
    return integral

# Обчислення інтеграла
result, error = spi.quad(f, a, b)

print("Інтеграл: ", result, error)

mc_result = monte_carlo_integration(f, a, b)
print("Інтеграл (метод Монте-Карло): ", mc_result)

# Створення діапазону значень для x
x = np.linspace(-0.5, 4.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = sin(x^2) + 0.5x від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
