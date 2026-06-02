# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):

    dut._log.info("Starting TRNG Test")

    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0

    await ClockCycles(dut.clk, 10)

    dut.rst_n.value = 1

    # Test Input
    dut.ui_in.value = 0b10101100

    await ClockCycles(dut.clk, 1)

    # Expected output according to project.v logic

    feedback_path_a = ((0b10101100 >> 7) & 1) ^ ((0b10101100 >> 5) & 1)
    feedback_path_b = ((0b10101100 >> 3) & 1) ^ ((0b10101100 >> 1) & 1)

    expected = 0

    for i in range(8):
        bit = (0b10101100 >> i) & 1

        if i % 2 == 0:
            newbit = bit ^ feedback_path_a
        else:
            newbit = bit ^ feedback_path_b

        expected |= (newbit << i)

    dut._log.info(f"Expected Output = {expected}")
    dut._log.info(f"Actual Output   = {int(dut.uo_out.value)}")

    assert int(dut.uo_out.value) == expected
