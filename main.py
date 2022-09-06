import tkinter as tk
from generator import generate_password


def password_length_validator():
	"""Checks that value in ent_pas_len is correct"""
	length = parameters['length'].get()

	if not length.isdigit() or int(length) < 1:
		length = '1'

	ent_pas_len.delete(0, tk.END)
	ent_pas_len.insert(0, length)

def generate():
	"""Generate a password using generate_password function"""
	password_length_validator()

	password_params = {key: value.get() for key, value in parameters.items()}
	if True not in password_params.values():
		cbx_nums.select()
		password_params['nums'] = True

	password_params['length'] = int(password_params['length'])

	password = generate_password(**password_params)

	ent_new_pas.delete(0, tk.END)
	ent_new_pas.insert(0, password)

def copy():
	"""Copies password to clipboard"""
	window.clipboard_clear()
	window.clipboard_append(ent_new_pas.get())

def increase_password_length():
	"""Increase password length"""
	password_length_validator()

	length = int(parameters['length'].get())
	parameters['length'].set(length + 1)

def decrease_password_length():
	"""Decrease password length"""
	password_length_validator()

	length = int(parameters['length'].get())
	if length > 1:
		parameters['length'].set(length - 1)


window = tk.Tk()
window.title("Генератор Паролей")
window.resizable(width=False, height=False)

parameters = {
	'length': tk.StringVar(window, '12'),
	'first_cap': tk.BooleanVar(window, True),
	'upper_chars': tk.BooleanVar(window, True),
	'lower_chars': tk.BooleanVar(window, True),
	'nums': tk.BooleanVar(window, True),
	'spec_symbs': tk.BooleanVar(window, False),
	'sim_chars': tk.BooleanVar(window, False),
}


# Block of password generation parameters

# Main frame
lbl_frm_params = tk.LabelFrame(window, text="Параметры генерации пароля")
lbl_frm_params.pack(padx=10, pady=10)

# Password length
lbl_pas_len = tk.Label(lbl_frm_params, text="Длина пароля:")
frm_pas_len = tk.Frame(lbl_frm_params)

lbl_pas_len.grid(row=0, column=0, sticky='w', padx=8, pady=2)
frm_pas_len.grid(row=0, column=1, sticky='w', padx=8, pady=2)

btn_dec_len = tk.Button(frm_pas_len, text="-", command=decrease_password_length)
ent_pas_len = tk.Entry(frm_pas_len, width=20, bd=0, textvariable=parameters['length'])
btn_inc_len = tk.Button(frm_pas_len, text="+", command=increase_password_length)

btn_dec_len.pack(side=tk.LEFT, ipadx=7)
ent_pas_len.pack(side=tk.LEFT, fill=tk.BOTH)
btn_inc_len.pack(side=tk.LEFT, ipadx=7)

# Use of special symbols
lbl_spec_symbs = tk.Label(lbl_frm_params, text="Использовать символы:")
cbx_spec_symbs = tk.Checkbutton(
	lbl_frm_params,
	text="(Например: !@#$...)",
	variable=parameters['spec_symbs'],
	onvalue=True,
	offvalue=False
)

lbl_spec_symbs.grid(row=1, column=0, sticky='w', padx=8, pady=2)
cbx_spec_symbs.grid(row=1, column=1, sticky='w', padx=8)

# Use of numbers
lbl_nums = tk.Label(lbl_frm_params, text="Использовать цифры:")
cbx_nums = tk.Checkbutton(
	lbl_frm_params,
	text="(Например: 12345...)",
	variable=parameters['nums'],
	onvalue=True,
	offvalue=False
)

lbl_nums.grid(row=2, column=0, sticky='w', padx=8, pady=2)
cbx_nums.grid(row=2, column=1, sticky='w', padx=8)

# Use of lowercase letters
lbl_lower_chars = tk.Label(lbl_frm_params, text="Использовать прописные буквы:")
cbx_lower_chars = tk.Checkbutton(
	lbl_frm_params,
	text="(Например: abcdefg...)",
	variable=parameters['lower_chars'],
	onvalue=True,
	offvalue=False
)

lbl_lower_chars.grid(row=3, column=0, sticky='w', padx=8, pady=2)
cbx_lower_chars.grid(row=3, column=1, sticky='w', padx=8)

# Use of capital letters
lbl_upper_chars = tk.Label(lbl_frm_params, text="Использовать заглавные буквы:")
cbx_upper_chars = tk.Checkbutton(
	lbl_frm_params,
	text="(Например: ABCDEFG...)",
	variable=parameters['upper_chars'],
	onvalue=True,
	offvalue=False
)

lbl_upper_chars.grid(row=4, column=0, sticky='w', padx=8, pady=2)
cbx_upper_chars.grid(row=4, column=1, sticky='w', padx=8)

# Use oof similar letters
lbl_sim_chars = tk.Label(lbl_frm_params, text="Использовать похожие буквы:")
cbx_sim_chars = tk.Checkbutton(
	lbl_frm_params,
	text="(Например: oO0iI...)",
	variable=parameters['sim_chars'],
	onvalue=True,
	offvalue=False
)

lbl_sim_chars.grid(row=5, column=0, sticky='w', padx=8, pady=2)
cbx_sim_chars.grid(row=5, column=1, sticky='w', padx=8)

# First letter is capital
lbl_first_cap = tk.Label(lbl_frm_params, text="Первая буква - заглавная:")
cbx_first_cap = tk.Checkbutton(
	lbl_frm_params,
	text="(Напрмер: Abfda7)",
	variable=parameters['first_cap'],
	onvalue=True,
	offvalue=False
)

lbl_first_cap.grid(row=6, column=0, sticky='w', padx=8, pady=2)
cbx_first_cap.grid(row=6, column=1, sticky='w', padx=8)


# Block of password generation

# Main frame
frm_generation = tk.Frame(window)
frm_generation.pack(expand=True, fill=tk.X, pady=(0, 10), padx=12)
frm_generation.grid_columnconfigure([0, 1], weight=1)

# New password field
lbl_new_pas = tk.Label(frm_generation, text="Ваш новый пароль:")
ent_new_pas = tk.Entry(frm_generation)

lbl_new_pas.grid(row=0, column=0, sticky='w', padx=8, pady=2)
ent_new_pas.grid(row=0, column=1, sticky='we', padx=8)

# Generation
frm_buttons = tk.Frame(frm_generation)
frm_buttons.grid(row=1, column=1, sticky='we', padx=8, pady=2)
frm_buttons.grid_columnconfigure([0, 1], weight=1)

btn_copy = tk.Button(frm_buttons, text="Скопировать", command=copy)
btn_generate = tk.Button(frm_buttons, text="Сгенерировать", command=generate)

btn_copy.grid(row=0, column=0, sticky='we', padx=(0, 4))
btn_generate.grid(row=0, column=1, sticky='we', padx=(4, 0))


window.mainloop()
