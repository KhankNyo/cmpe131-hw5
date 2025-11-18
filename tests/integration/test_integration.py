from src.order_io import *;
import pytest;

def test_order_integration(tmp_path):
    input_file = tmp_path / "order.csv"
    input_file.write_text(
        "widget,$10.00\n"
        + "gizmo,5.50\n"
        + "nisno,7.50\n", 
        encoding="utf-8"
    )

    total_price = float(bulk_total([10.0, 5.5, 7.5]));

    items = load_order(input_file)
    write_receipt(tmp_path / "receipt.txt", items)
    output_text = (tmp_path / "receipt.txt").read_text(encoding="utf-8")

    assert "widget: $10.00" in output_text
    assert "gizmo: $5.50\n" in output_text
    assert "nisno: $7.50\n" in output_text
    assert f"TOTAL: ${total_price:0.2f}" in output_text

def test_order_integration_lines_12_15(tmp_path):
    input_file = tmp_path / "order.csv"
    input_file.write_text(
        "widget,$10.00\n"
        + "gizmo,5.50\n\n"  # testing ln.strip, line 12
        + "nisno",          # testing raise ValueError, line 15
        encoding="utf-8"
    )
    with pytest.raises(ValueError): 
        load_order(input_file)

