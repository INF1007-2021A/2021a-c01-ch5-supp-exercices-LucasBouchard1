#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name: str, data: tuple) -> str:
	num_len = lambda num : len(str(num))
	sous_total = round(sum([info[1]*info[2] for info in data]),2)
	taxes = round(sous_total * 0.15,2)
	total = round(sous_total + taxes,2)
	lenght = num_len(total) + 5

	return f"""{name}
SOUS TOTAL{" "*(lenght - num_len(sous_total))}{sous_total} $
TAXES     {" "*(lenght - num_len(taxes))}{taxes} $
TOTAL     {" "*5}{total} $"""


def format_number(number: float, num_decimal_digits: int) -> str:
	return str(int(number * 10**num_decimal_digits + 0.5*(-1)**bool(number<0)) /10**num_decimal_digits)

def get_triangle(num_rows):
	_horizontal_border = "+"*(num_rows*2+1)
	return _horizontal_border+"\n"+"\n".join(["+"+" "*(num_rows-x-1)+"A"*(2*x+1)+" "*(num_rows-x-1)+"+" for x in range(num_rows)])+"\n"+_horizontal_border


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 100, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
