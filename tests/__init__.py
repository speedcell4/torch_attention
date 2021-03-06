import os

import torch
from hypothesis import strategies as st

BATCH = st.integers(1, 7)
BATCHES = st.lists(BATCH, min_size=1, max_size=5)

CHANNEL = st.integers(1, 5)

TINY_FEATURES = st.integers(5, 20)
SMALL_FEATURES = st.integers(20, 50)
NORMAL_FEATURES = st.integers(50, 100)

NUM_HEADS = st.integers(2, 5)
NUM_LAYERS = st.integers(1, 10)

WINDOW_SIZE = st.sampled_from([1, 3, 5, 7])
WINDOW_SIZES = st.lists(WINDOW_SIZE, min_size=1, max_size=5)

BIAS = st.booleans()

if torch.cuda.is_available():
    if 'PYTEST_DEVICE' in os.environ:
        device = os.environ['PYTEST_DEVICE']
        torch.cuda.set_device(int(device))
        DEVICE = st.sampled_from([torch.device(f'cuda:{device}'), torch.device('cpu')])
        del device
else:
    DEVICE = st.sampled_from([torch.device('cpu')])
