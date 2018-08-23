from hypothesis import given

from torch_attention import TransformerEncoder
from tests import *


@given(
    batch=BATCH,
    channel=CHANNEL,
    num_layers=NUM_LAYERS,
    model_features=TINY_FEATURES,
    num_heads=NUM_HEADS,
    dropout=st.floats(0., 1.),
    window_sizes=WINDOW_SIZES,
    bias=st.booleans(),
    device=DEVICE,
)
def test_transformer_encoder(
        batch, channel, num_layers, model_features,
        num_heads, dropout, window_sizes, bias, device):
    in_features = num_heads * model_features
    encoder = TransformerEncoder(
        num_layers=num_layers, in_features=in_features, num_heads=num_heads,
        dropout=dropout, window_sizes=window_sizes, bias=bias)
    x = torch.rand(batch, channel, in_features)

    encoder = encoder.to(device)
    x = x.to(device)

    assert encoder(x).size() == (batch, channel, in_features)
