/*
 * Copyright (c) 2026 Likitha
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_likitha_trng (
    input  wire [7:0] ui_in, 
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,

    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

wire feedback_path_a;
wire feedback_path_b;

assign feedback_path_a =
       ui_in[7] ^
       ui_in[5];

assign feedback_path_b =
       ui_in[3] ^
       ui_in[1];

assign uo_out[0] = ui_in[0] ^ feedback_path_a;
assign uo_out[1] = ui_in[1] ^ feedback_path_b;
assign uo_out[2] = ui_in[2] ^ feedback_path_a;
assign uo_out[3] = ui_in[3] ^ feedback_path_b;
assign uo_out[4] = ui_in[4] ^ feedback_path_a;
assign uo_out[5] = ui_in[5] ^ feedback_path_b;
assign uo_out[6] = ui_in[6] ^ feedback_path_a;
assign uo_out[7] = ui_in[7] ^ feedback_path_b;

assign uio_out = 8'b0;
assign uio_oe  = 8'b0;

wire _unused = &{ena, clk, rst_n, uio_in, 1'b0};

endmodule
