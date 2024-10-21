def loading_bar(progress_number: int) -> str:
    if progress_number == 100:
        return '100% Complete!\n[%%%%%%%%%%]'
    elif progress_number < 100:
        loaded_percents_as_digit = progress_number // 10
        not_loaded_percents_as_digit = 10 - loaded_percents_as_digit
        return f"{progress_number}% [{'%' * loaded_percents_as_digit}{'.' * not_loaded_percents_as_digit}]\nStill " \
               f"loading... "
    loaded_percents_as_digit = progress_number // 10
    not_loaded_percents_as_digit = 10 - loaded_percents_as_digit
    return f"{progress_number}% [{'%'*loaded_percents_as_digit}{'.'* not_loaded_percents_as_digit}]"


number = int(input())
print(loading_bar(number))
