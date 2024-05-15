def solve_math_problem(problem):
    """
Resuelve problmeas simples de matematicas regrensando la respuesta
    """

    try:
        # Divide el porblmeaa en partes
        parts = problem.split()

        # Verifica el signo de operación usado y conlleva la operación necesaria
        if '+' in parts:
            operator_index = parts.index('+')
            answer = int(parts[operator_index - 1]) + int(parts[operator_index + 1])
        elif '-' in parts:
            operator_index = parts.index('-')
            answer = int(parts[operator_index - 1]) - int(parts[operator_index + 1])
        elif 'x' in parts:
            operator_index = parts.index('x')
            answer = int(parts[operator_index - 1]) * int(parts[operator_index + 1])
        elif '/' in parts:
            operator_index = parts.index('/')
            answer = int(parts[operator_index - 1]) / int(parts[operator_index + 1])
        else:
            return "Invalido porblema matematico checa bien los signos que maneja."

    except (ValueError, ZeroDivisionError):
        # Si no es valido algo en el porblema da resultado de error
        return "Error"

    return answer

# Uso ejemplo
problem = input("Enter the math problem (use '+' for addition, '-' for subtraction, 'x' for multiplication, and '/' for division): ")
answer = solve_math_problem(problem)
print(f"The answer to {problem} is {answer}")
