def grading_system():
    try:
        user_score = int(input('Enter a score: '))
    except ValueError:
        print('That input is not a number.')
    else:
        if 70 <= user_score <= 100:
            print(f'{user_score}: A')
        elif 60 <= user_score <= 69:
            print(f'{user_score}: B')
        elif 50 <= user_score <= 59:
            print(f'{user_score}: C')
        elif 45 <= user_score <= 49:
            print(f'{user_score}: D')
        elif 40 <= user_score <= 49:
            print(f'{user_score}: E')
        elif user_score <= 39:
            print(f'{user_score}: F')
        else:
            print('invalid score')

grading_system()