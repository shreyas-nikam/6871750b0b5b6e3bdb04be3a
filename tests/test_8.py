import pytest
from definition_cedf89ef023c47108bab677a708a7bca import apply_insurance_mitigation

@pytest.mark.parametrize("loss_series, deductible, cover_limit, expected", [
    ([100, 200, 300], 50, 100, [50, 100, 100]),
    ([10, 20, 30], 50, 100, [0, 0, 0]),
    ([100, 200, 300], 0, 100, [100, 100, 100]),
    ([100, 200, 300], 50, 0, [0, 0, 0]),
    ([50], 50, 50, [0])
])
def test_apply_insurance_mitigation(loss_series, deductible, cover_limit, expected):
    assert apply_insurance_mitigation(loss_series, deductible, cover_limit) == expected
