from tkinter import filedialog, messagebox

S = ''

PLACEHOLDER = "[name]"
name_dir_file = ''
letter_dir_file = ''
output_dir = ''
name_dir = messagebox.askyesno(title='Guess names', message='Do you have the list of invited guess')
if name_dir:
    name_dir_file = filedialog.askopenfilename(title='Invited Guess List File', typevariable=None)

letter_dir = messagebox.askyesno(title='Letter Template', message='Do you have the mail template file?')
if letter_dir:
    letter_dir_file = filedialog.askopenfilename(title='Select Letter Template', typevariable=None)

save_dir = messagebox.askyesno(title='Save File To', message='Where would you like to save the new mail?')
if save_dir:
    output_dir = filedialog.askdirectory(title='Save File To')


with open(name_dir_file, mode='r') as file:
    names = file.readlines()

with open(letter_dir_file, mode='r') as letter:
    mail_contents = letter.read()
    for name in names:
        stripped_name = name.strip()
        placeholder_to_name = mail_contents.replace(PLACEHOLDER, stripped_name)
        with open(f'{output_dir}/letter_for_{stripped_name}.txt', mode='w') as output_letter:
            output_letter.write(placeholder_to_name)
