import string
import random as rm
full_alphabet_list = list(string.ascii_letters)



def password_generator(pw = input("How long do you want your password to be? Please choose a length that is between 15 and 40 characters long: ")):
  pw = int(pw)
  response = 'y'
  while response == 'y':
    if pw % 2 == 0:
      pw_split_char = int(pw / 2)
      pw_split_int = int(pw / 2)
      int(pw_split_char)
      int(pw_split_int)
    else:
      pw_split_int = int((pw - 1) / 2)
      pw_split_char = int(abs(pw - pw_split_int))
      int(pw_split_char)
      int(pw_split_int)
    type(pw_split_char)
    type(pw_split_int)
    rm_index_char = rm.sample(list(range(1,52)), pw_split_char)
    random_char_list = [str(full_alphabet_list[i]) for i in rm_index_char]
    alpha_pw_string = "".join(random_char_list)
    alpha_pw_list = list(alpha_pw_string)
    zero_ten_int_num_list = list(range(0,pw_split_int))
    random_zero_ten_str_list = [str(rm.randint(0,9)) for i in zero_ten_int_num_list]
    zero_ten_string = "".join(str(i) for i in random_zero_ten_str_list)
    zero_ten_string_list = list(zero_ten_string)
    unmixed_concat_list = (alpha_pw_list + zero_ten_string_list)
    rm.shuffle(unmixed_concat_list)
    final_pw = "".join(unmixed_concat_list)
    print(final_pw)
    response = input("Your randomly generated alphanumeric password is: " + final_pw + " would you like another one? y/n ")
password_generator()