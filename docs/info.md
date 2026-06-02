# Secure TRNG Entropy Generator 

## How it works

The Secure TRNG (True Random Number Generator) Entropy Generator is a hardware-based random number generation system designed for cryptographic and security applications.

The design accepts an 8-bit entropy input through the Tiny Tapeout user input pins. Internal processing combines multiple entropy bits using XOR-based feedback logic to generate a randomized 8-bit output stream.

The system consists of the following logical stages:

1. Entropy Collection
   - Raw entropy bits are provided through the input pins.

2. Entropy Mixing
   - Multiple entropy bits are combined using feedback paths.

3. Randomness Enhancement
   - XOR operations improve statistical randomness.

4. Secure Output Generation
   - Final processed random bits are presented on the output pins.

The design provides a lightweight hardware random number generation architecture suitable for FPGA and ASIC implementation.

---

## How to test

Apply any 8-bit value to the input pins:

| Input | Description |
|---------|---------|
| ui[7:0] | Entropy Input |

Observe the generated random output:

| Output | Description |
|---------|---------|
| uo[7:0] | Secure Random Output |

Example:

Input:

```
10101100
```

Output:

```
11001011
```

The output changes according to the entropy inputs and feedback mixing logic implemented in the design.

---

## External hardware

No external hardware is required.

Inputs are supplied through the Tiny Tapeout input pins and outputs are observed through the Tiny Tapeout output pins.
