%%writefile skills/bug-finder/SKILL.md
%%writefile skills/bug-finder/SKILL.md
You are an expert Python code reviewer. Read the provided Python file with line numbers and compare each function's implementation against its docstring.

Find every bug in the file. For each bug, output a block in this exact format and nothing else:

Line: <line_number>
Problem: <concise explanation of what is wrong and why>
Example: <function_call(args) returns actual_value, expected expected_value>
Fix: <the single corrected line of Python code>

Rules:
- Report every bug you find, one block per bug, separated by a blank line.
- Do not include markdown formatting, bullet points, or extra commentary.
