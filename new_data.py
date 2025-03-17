# Call this in a jupyter notebook!
# %pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

import torch
import numpy as np

# New underlying pattern (radial wave pattern)
x_data = np.linspace(-5, 5, 1100)  # Change range
y_data = np.linspace(-5, 5, 1100)
X, Y = np.meshgrid(x_data, y_data)

pattern = np.sin(np.sqrt(X**2 + Y**2))  # Radial sine wave instead of sin(X) + cos(Y)

# Define new dataset dimensions
N, D_in, H, D_out = 2000, 2, 50, 1  # Changed N

# Creating the input data
x = torch.randn(N, D_in) * 2  # Scale down to different range
y = torch.sin(torch.sqrt(x[:, 0]**2 + x[:, 1]**2)).unsqueeze(1)  # Radial function instead of sum of sine/cosine

# Add asymmetric noise to introduce variation
noise = torch.randn(N, D_out) * 0.3  # Increased noise level
y += noise

# Extract values for plotting
x_values = x.numpy()[:, 0]
y_values = x.numpy()[:, 1]
color_values = y.numpy().flatten()