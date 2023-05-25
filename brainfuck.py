import sys

with open("code.bf", "r") as file:
	code = file.read()

TAPE_START = 0
TAPE_END = 2999
MIN_CELL = 0
MAX_CELL = 255

tape = [0 for i in range(TAPE_END + 1)]
pointer = 0

code_i = 0

loop_stack = []

while code_i < len(code):
	command = code[code_i]
	if command == '>':
		pointer += 1
		if pointer > TAPE_END:
			pointer = TAPE_START

	if command == '<':
		pointer -= 1
		if pointer < TAPE_START:
			pointer = TAPE_END

	if command == '+':
		tape[pointer] += 1
		if tape[pointer] > MAX_CELL:
			tape[pointer] = MIN_CELL

	if command == '-':
		tape[pointer] -= 1
		if tape[pointer] < MIN_CELL:
			tape[pointer] = MAX_CELL

	if command == '.':
		print(chr(tape[pointer]), end='')

	if command == ',':
		tape[pointer] = ord(sys.stdin.buffer.read(1))

	if command == '[':
		if tape[pointer] == 0:
			loop_depth = 1
			while loop_depth > 0:
				code_i += 1
				if code[code_i] == '[':
					loop_depth += 1
				elif code[code_i] == ']':
					loop_depth -= 1
		else:
			loop_stack.append(code_i)

	if command == ']':
		if tape[pointer] != 0:
			code_i = loop_stack[-1]
		else:
			loop_stack.pop()

	code_i += 1
