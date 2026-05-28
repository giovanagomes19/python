
import math

from flask import render_template, request


def calcular():
    try:
        num1 = float(request.form["num1"])
        operacao = request.form["operacao"]

        # =========================
        # RAIZ QUADRADA
        # =========================
        if operacao == "sqrt":

            if num1 < 0:
                resultado = "Erro"
                etapas = f"Não existe raiz real de {num1}."

            else:
                resultado = math.sqrt(num1)
                etapas = f"√{num1} = {resultado}"

        # =========================
        # LOGARITMO
        # =========================
        elif operacao == "log":

            if num1 <= 0:
                resultado = "Erro"
                etapas = "O logaritmo só existe para números positivos."

            else:
                resultado = math.log(num1)
                etapas = f"log({num1}) = {resultado}"

        # =========================
        # BHASKARA
        # =========================
        elif operacao == "bhaskara":

            b_valor = request.form.get("num2", "").strip()
            c_valor = request.form.get("num3", "").strip()

            if not b_valor or not c_valor:
                return render_template(
                    "calculadora.html",
                    etapas="Informe os valores de B e C.",
                    resultados=""
                )

            b = float(b_valor)
            c = float(c_valor)

            delta = (b ** 2) - (4 * num1 * c)

            if delta < 0:
                resultado = "Erro"
                etapas = f"Delta = {delta}. Não existem raízes reais."

            else:
                x1 = (-b + math.sqrt(delta)) / (2 * num1)
                x2 = (-b - math.sqrt(delta)) / (2 * num1)

                resultado = f"x1 = {x1} | x2 = {x2}"

                etapas = (
                    f"Δ = b² - 4ac\n"
                    f"Δ = ({b})² - 4·({num1})·({c})\n"
                    f"Δ = {delta}"
                )

        # =========================
        # OUTRAS OPERAÇÕES
        # =========================
        else:

            num2_valor = request.form.get("num2", "").strip()

            if not num2_valor:
                return render_template(
                    "calculadora.html",
                    etapas="Informe o segundo número para esta operação.",
                    resultados="",
                )

            num2 = float(num2_valor)

            # SOMA
            if operacao == "+":
                resultado = num1 + num2
                etapas = f"{num1} + {num2} = {resultado}"

            # SUBTRAÇÃO
            elif operacao == "-":
                resultado = num1 - num2
                etapas = f"{num1} - {num2} = {resultado}"

            # MULTIPLICAÇÃO
            elif operacao == "*":
                resultado = num1 * num2
                etapas = f"{num1} × {num2} = {resultado}"

            # DIVISÃO
            elif operacao == "/":

                if num2 == 0:
                    resultado = "Erro"
                    etapas = "Não é possível dividir por zero."

                else:
                    resultado = num1 / num2
                    etapas = f"{num1} ÷ {num2} = {resultado}"

            # POTÊNCIA
            elif operacao == "**":
                resultado = math.pow(num1, num2)
                etapas = f"{num1}^{num2} = {resultado}"

            else:
                resultado = "Erro"
                etapas = "Operação inválida."

        return render_template(
            "calculadora.html",
            etapas=etapas,
            resultados=resultado
        )

    except ValueError:
        return render_template(
            "calculadora.html",
            etapas="Digite valores numéricos válidos.",
            resultados=""
        )